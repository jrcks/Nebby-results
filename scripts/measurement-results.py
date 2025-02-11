import matplotlib.pyplot as plt
import pandas as pd
import sys
from collections import defaultdict

if (len(sys.argv) != 2):
    print("Usage: python3 measurement-results.py <results-file>")
    sys.exit(1)

file = sys.argv[1]
results = defaultdict(lambda: defaultdict(int))

with open(file, 'r') as f:
    for line in f:
        measurement = line.split(' | ')
        if len(measurement) == 2:
            expected: str = measurement[0].strip().rstrip('0123456789')
            actual: str = measurement[1].strip()
            
            expected = expected.upper()
            
            if (actual == "BBR(Maybe)"):
                actual = "BBR"
            if (actual == "NAN - NO FEATURES"):
                actual = "Unbekannt"
            if (actual == "TOO MUCH MSE ERROR"):
                actual = "Unbekannt"
            if (actual.startswith("Outlier with degree fit =")):
                actual = "Unbekannt - Grad " + actual.split(" = ")[1]

            results[actual][expected] += 1

df = pd.DataFrame(results).fillna(0)
df = df.astype(int)

ax = df.plot(kind='bar', stacked=True, figsize=(10, 6))

plt.xlabel('Wirklicher CCA')
plt.ylabel('Analyseergebnisse')
plt.title('Nebby Analyseergebnisse für Kontroll-Messungen')
plt.legend(title='Erkannter CCA', bbox_to_anchor=(1,1), loc='upper left')
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()
