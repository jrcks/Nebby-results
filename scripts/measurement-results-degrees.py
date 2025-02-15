import matplotlib.pyplot as plt
import pandas as pd
import sys
from collections import defaultdict

# Mögliche Ergebnisse:
# Degree 1
#    1 bic
#    2 scalable
#    3 yeah
# Degree 2
#    1 dctcp
#    2 highspeed
#    3 lp
#    4 westwood
#    5 reno
# Degree 3
#    1 htcp
#    2 veno
#    3 cubic
#    4 cubicQ
# Unknown
#    1 Outlier with degree fit = 1
#    2 Outlier with degree fit = 2
#    3 Outlier with degree fit = 3
# Error
#    1 Error

if (len(sys.argv) != 2):
    print("Usage: python3 measurement-results.py <results-file>")
    sys.exit(1)

file = sys.argv[1]
results = defaultdict(lambda: defaultdict(int))

with open(file, 'r') as f:
    for line in f:
        measurement = line.split(' | ')
        if len(measurement) == 2:
            expected: str = measurement[0].strip().rstrip('0123456789').upper()
            actual: str = measurement[1].strip()
            
            # Add degree to expected label
            if (expected in ["BIC", "SCALABLE", "YEAH", "VEGAS"]):
                expected += " (1)"
            if (expected in ["DCTCP", "HIGHSPEED", "LP", "WESTWOOD", "RENO"]):
                expected += " (2)"
            if (expected in ["HTCP", "VENO", "CUBIC", "CUBICQ"]):
                expected += " (3)"
            
            # Ignore BBR
            if (expected == "BBR"):
                continue
            # Ignore BBR(Maybe) and use the "normally" detected CCA
            if (actual == "BBR(Maybe)"):
                actual = measurement[2].strip().upper()
            
            if (actual == "NAN - NO FEATURES"):
                actual = "Error - Features"
            if (actual == "TOO MUCH MSE ERROR"):
                actual = "Error - MSE"
            if (actual.startswith("Outlier with degree fit =")):
                actual = "Degree " + actual.split(" = ")[1].strip()
            
            if (actual in ["BIC", "SCALABLE", "YEAH"]):
                actual = "Degree 1"
            if (actual in ["DCTCP", "HIGHSPEED", "LP", "WESTWOOD", "RENO"]):
                actual = "Degree 2"
            if (actual in ["HTCP", "VENO", "CUBIC", "CUBICQ"]):
                actual = "Degree 3"

            if (actual[-1].isnumeric() and actual[-1] in expected):
                actual = "Korrekt"
            
            results[actual][expected] += 1

# Farben für bestimmte Ergebnisse festlegen
colors = {
    'Error - Features': 'red',        # Rot
    'Error - MSE': 'orange',        # Orange
    'Korrekt': 'black',    # Grün
    'BBR': '#7f7f7f',      # Grau
    'Degree 1': '#1f77b4', # Blau
    'Degree 2': 'green',   # Orange
    'Degree 3': '#9467bd'  # Lila
}

df = pd.DataFrame(results).fillna(0)
df = df.astype(int)

# Sortiere rows alphabetisch
df = df.sort_index()

color_list = [colors.get(col, 'yellow') for col in df.columns]

ax = df.plot(kind='bar', stacked=True, figsize=(10, 6), color=color_list)

plt.xlabel('Wirklicher CCA (Grad)')
plt.ylabel('Grad-Analyseergebnisse')
plt.title('Nebby Grad-Analyseergebnisse für Kontroll-Messungen')
plt.legend(title='Erkannter Grad', bbox_to_anchor=(1,1), loc='upper left')
plt.xticks(rotation=45)
plt.tight_layout()

# Berechnen der Anzahl der korrekten Ergebnisse
correct = 0
bbr = 0
error_feat = 0
error_mse = 0
false = 0


for actual in results:
    for expected in results[actual]:
        if expected == "BBR":
            continue
        if (actual == "Korrekt"):
            correct += results[actual][expected]
        elif (actual == "BBR"):
            bbr += results[actual][expected]
        elif (actual == "Error - Features"):
            error_feat += results[actual][expected]
        elif (actual == "Error - MSE"):
            error_mse += results[actual][expected]
        else:
            false += results[actual][expected]

total = correct + bbr + error_feat + false
print("Ergebnisse:", total)
print("Korrekt: ", correct, " (", correct/total * 100, "%)", sep="")
print("Korrekt ohne BBR und Error: ", correct, " (", correct/(total - bbr - error_feat) * 100, "%)", sep="")
print("BBR: ", bbr, " (", bbr/total * 100, "%)", sep="")
print("Error-Feat: ", error_feat, " (", error_feat/total * 100, "%)", sep="")
print("Error-MSE: ", error_mse, " (", error_mse/total * 100, "%)", sep="")
print("Error-MSE ohne BBR und Error: ", error_mse, " (", error_mse/(total - bbr - error_feat) * 100, "%)", sep="")
print("Falsch: ", false, " (", false/total * 100, "%)", sep="")
print("Falsch ohne BBR und Error: ", false, " (", false/(total - bbr - error_feat) * 100, "%)", sep="")

plt.show()
