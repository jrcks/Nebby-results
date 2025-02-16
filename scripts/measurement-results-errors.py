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
            
            if (actual == "NAN - NO FEATURES"):
                actual = "Error - Features"
            elif (actual == "TOO MUCH MSE ERROR"):
                actual = "Error - MSE"
            else:
                actual = "OK"
            
            if (expected in ["BIC", "SCALABLE", "YEAH", "VEGAS"]):
                expected += " (1)"
            if (expected in ["DCTCP", "HIGHSPEED", "LP", "WESTWOOD", "RENO"]):
                expected += " (2)"
            if (expected in ["HTCP", "VENO", "CUBIC", "CUBICQ"]):
                expected += " (3)"

            results[actual][expected] += 1

# Farben für bestimmte Ergebnisse festlegen
colors = {
    'Error - Features': 'red',
    'Error - MSE': 'orange',
    'OK': 'grey'
}

df = pd.DataFrame(results).fillna(0)
df = df.astype(int)

# Sortiere rows alphabetisch
df = df.sort_index()

color_list = [colors.get(col, 'grey') for col in df.columns]

ax = df.plot(kind='bar', stacked=True, figsize=(10, 6), color=color_list)

plt.xlabel('Wirklicher CCA (Grad)')
plt.ylabel('Analyseergebnisse')
plt.title('Nebby Fehler-Analyseergebnisse für Kontroll-Messungen')
plt.legend(title='Analysierbar', bbox_to_anchor=(1,1), loc='upper left')
plt.xticks(rotation=45)
plt.tight_layout()

# Anzahl der Fehler
feature_errors = 0
mse_errors = 0
ok = 0
for key in results:
    if key == "Error - Features":
        feature_errors = sum(results[key].values())
    elif key == "Error - MSE":
        mse_errors = sum(results[key].values())
    else:
        ok = sum(results[key].values())

total = feature_errors + mse_errors + ok
print(f"Total: {total}")
print(f"Feature Errors: {feature_errors} ({feature_errors / total * 100:.2f}%)")
print(f"MSE Errors: {mse_errors} ({mse_errors / total * 100:.2f}%)")
print(f"OK: {ok} ({ok / total * 100:.2f}%)")

plt.show()
