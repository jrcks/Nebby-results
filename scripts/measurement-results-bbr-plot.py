import matplotlib.pyplot as plt
import pandas as pd
import sys, os
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

print_plot = True

if print_plot and not os.path.exists("plots"):
    os.makedirs("plots")

with open(file, 'r') as f:
    for line in f:
        measurement = line.split(' | ')
        if len(measurement) >= 2:
            expected: str = measurement[0].strip().rstrip('0123456789').upper()
            actual: str = measurement[1].strip()

            if (actual == "BBR(Maybe)"):
                actual = "BBR | " + measurement[2].strip().upper()
            if (actual == "NAN - NO FEATURES"):
                actual = "Error"
            if (actual == "TOO MUCH MSE ERROR"):
                actual = "Error"
            if (actual.startswith("Outlier with degree fit =")):
                actual = "Unbekannt - Grad " + actual.split(" = ")[1]
            
            results[actual][expected] += 1

# Remove results which do not contain BBR
results = {k: v for k, v in results.items() if "BBR" in k}

df = pd.DataFrame(results).fillna(0)
df = df.astype(int)

# Sortiere rows alphabetisch
df = df.sort_index()

ax = df.plot(kind='bar', stacked=True, figsize=(10, 6))

plt.xlabel('Wirklicher CCA')
plt.ylabel('Analyseergebnisse')
plt.title('Detailansicht der BBR-Ergebnisse')
plt.legend(title='Erkannter CCA', bbox_to_anchor=(1,1), loc='upper left')
plt.xticks(rotation=45)
plt.tight_layout()

if print_plot:
    plt.savefig(f"plots/bbr.png")
else:
    plt.show()
plt.close()
