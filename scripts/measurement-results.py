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
        if len(measurement) >= 2:
            expected: str = measurement[0].strip().rstrip('0123456789').upper()
            actual: str = measurement[1].strip()
            
            if (actual == "BBR(Maybe)"):
                actual = "BBR"
            if (actual == "NAN - NO FEATURES"):
                actual = "Error"
            if (actual == "TOO MUCH MSE ERROR"):
                actual = "Error"
            if (actual.startswith("Outlier with degree fit =")):
                actual = "Unbekannt - Grad " + actual.split(" = ")[1]
                
            if (expected == actual):
                actual = "Korrekt"

            results[actual][expected] += 1

# Farben für bestimmte Ergebnisse festlegen
colors = {
    'Error': 'red',                  # Rot für 'Error'
    'Korrekt': 'black',              # Schwarz für 'Korrekt'
    'Unbekannt - Grad 1': '#FFA07A', # Hellorange für Unbekannt - Grad 1
    'Unbekannt - Grad 2': '#FF8C00', # Dunkelorange für Unbekannt - Grad 2
    'Unbekannt - Grad 3': '#FF4500', # Mittelorange für Unbekannt - Grad 3
    'BBR': '#7570b3',      # Violett
    'BIC': '#1f77b4',      # Blau
    'SCALABLE': '#ff7f0e', # Orange
    'YEAH': '#2ca02c',     # Grün
    'DCTCP': '#e6ab02',    # Goldgelb
    'HIGHSPEED': '#9467bd',# Lila
    'LP': '#8c564b',       # Braun
    'WESTWOOD': '#e377c2', # Pink
    'RENO': '#7f7f7f',     # Grau
    'HTCP': '#bcbd22',     # Olivgrün
    'VENO': '#17becf',     # Türkis
    'CUBIC': '#aec7e8',    # Hellblau
    'CUBICQ': '#1b9e77',   # Blaugrün
}

df = pd.DataFrame(results).fillna(0)
df = df.astype(int)

# Sortiere rows alphabetisch
df = df.sort_index()

color_list = [colors.get(col, 'grey') for col in df.columns]

ax = df.plot(kind='bar', stacked=True, figsize=(10, 6), color=color_list)

plt.xlabel('Wirklicher CCA')
plt.ylabel('Analyseergebnisse')
plt.title('Nebby Analyseergebnisse für Kontroll-Messungen')
plt.legend(title='Erkannter CCA', bbox_to_anchor=(1,1), loc='upper left')
plt.xticks(rotation=45)
plt.tight_layout()


# Berechnen der Anzahl der korrekten Ergebnisse
correct = 0
error = 0
false = 0

for actual in results:
    for expected in results[actual]:
        if (actual == "Korrekt"):
            correct += results[actual][expected]
        elif ("Error" in actual):
            error += results[actual][expected]
        else:
            false += results[actual][expected]

total = correct + error + false

print(f"Total: {total}")
print(f"Correct: {correct} ({correct / total * 100:.2f}%)")
print(f"Correct without Error: {correct} ({correct / (total - error) * 100:.2f}%)")
print(f"Error: {error} ({error / total * 100:.2f}%)")
print(f"False: {false} ({false / total * 100:.2f}%)")
print(f"False without Error: {false} ({false / (total - error) * 100:.2f}%)")

plt.show()
