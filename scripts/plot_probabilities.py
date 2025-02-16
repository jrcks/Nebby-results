import os, sys
import pickle
import numpy as np
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from typing import Dict

if (len(sys.argv) != 2):
    print(f"Usage: python3 {__file__} <results-file>")
    sys.exit(1)

file = sys.argv[1]

print_plot = False

if print_plot and not os.path.exists("plots"):
    os.makedirs("plots")

pickle_dir = os.path.dirname(os.path.realpath(__file__)) + "/pickles"

scaled_vals: dict = pickle.load(open(pickle_dir + "/scaled_vals.txt","rb"))
classifiers: dict = pickle.load(open(pickle_dir + "/classifiers.txt","rb"))
count_to_mp: dict = pickle.load(open(pickle_dir + "/count_to_mp.txt","rb"))
inverse_count_to_mp = {d: {v: k for k, v in item.items()} for d, item in count_to_mp.items()}

degrees = [1,2,3]

coeffs_instead_of_scaled = False

class ExtendedResult:
    def __init__(self):
        self.file: str = ""
        self.label: str = ""
        self.bbr: str = ""
        self.result: str = ""
        self.degree: int = 0
        self.degree_coeff: list = []
        self.degree_error: float = 0
        self.probs: np.ndarray = [] # Probabilites for CCA within the given degree
        self.data: list = [] # data given to the classifier
        
    def __str__(self):
        return f"File: {self.file}, BBR: {self.bbr}, Result: {self.result}, Degree: {self.degree}, Coeff: {self.degree_coeff}, Error: {self.degree_error}"

results: Dict[str, ExtendedResult] = pickle.load(open(file, "rb"))

for degree in degrees:
    # TODO: Data and Probs für Outliers
    results_with_degree = [result for result in results.values() if result.degree == degree and result.bbr == "NO" and len(result.data) != 0]

    if (len(results_with_degree) == 0):
        print("No data for degree", degree)
        continue
    
    if coeffs_instead_of_scaled:
        data = [res.degree_coeff[0:degree] for res in results_with_degree]
    else:
        data = [res.data for res in results_with_degree]
    
    data = np.array(data)
    labels = [res.label for res in results_with_degree]
    
    clf: GaussianNB = classifiers[degree]
    
    if degree == 1:
        # Beispiel für 1D-Daten
        X_1d = np.linspace(-3, 3, 100).reshape(-1, 1)  # 100 Punkte zwischen -3 und 3
        #pred = classifiers[1].predict(X_1d)
        probs = classifiers[1].predict_proba(X_1d)

        fig, ax = plt.subplots(figsize=(10, 8))
        # Plotte die Wahrscheinlichkeiten der Klassen
        if not coeffs_instead_of_scaled:
            ax.plot(X_1d, probs[:, 0], color='blue', label=f'{count_to_mp[degree][1].upper()}', lw=2) # bic
            ax.plot(X_1d, probs[:, 1], color='red', label=f'{count_to_mp[degree][2].upper()}', lw=2) # scalable
            ax.plot(X_1d, probs[:, 2], color='green', label=f'{count_to_mp[degree][3].upper()}', lw=2) # yeah

        # group the data by the labels/filenames (actual CCAs)
        grouped_data = {}
        for i in range(len(labels)):
            actual = labels[i].rstrip().rstrip('0123456789')
            if actual not in grouped_data:
                grouped_data[actual] = []
            grouped_data[actual].append(data[i])

        outliers = []

        # Scatterplot der Datenpunkte
        for cca in grouped_data:
            grouped_data[cca] = np.array(grouped_data[cca])
            # Farben für CCAs festlegen
            if (cca.lower() not in inverse_count_to_mp[degree]):
                color = 'black'
                outliers.append(cca)
            else:
                pred_id = inverse_count_to_mp[degree][cca.lower()]
                if (pred_id == 1):
                    color = 'blue'
                elif (pred_id == 2):
                    color = 'red'
                elif (pred_id == 3):
                    color = 'green'
                else:
                    color = 'black'
            print("Scatter", cca, color)
            ax.scatter(grouped_data[cca], [0.5 for i in range(0, len(grouped_data[cca][:,0]))], s=40, color=color, edgecolors='black')
        
        ax.set_title('Degree 1 Clustering')
        ax.set_xlabel('c')
        ax.set_ylabel('Probability')
        ax.legend()
        ax.grid()
        plt.show()
    
    if degree == 2:
        # Erstellen von 2D-Daten
        x = np.linspace(-3, 3, 100)
        y = np.linspace(-3, 3, 100)
        xx, yy = np.meshgrid(x, y)
        X_2d = np.c_[xx.ravel(), yy.ravel()]
        
        # Vorhersage der Klassen
        preds = clf.predict(X_2d)
        preds = preds.reshape(xx.shape)

        # Erstellen eines Farb-Mappings für die Kategorien
        unique_preds = np.unique(preds)
        color_map = {pred_id: i for i, pred_id in enumerate(unique_preds)}  # Mapping von IDs zu Farben
        colors = np.array([color_map[pred] for pred in preds.ravel()]).reshape(preds.shape)

        # Erstelle eine Farbkarte
        cmap = plt.get_cmap('RdBu', len(unique_preds))
    
        fig, ax = plt.subplots(figsize=(10, 8))
        # Konturplot für die Klassen
        if not coeffs_instead_of_scaled:
            contour = ax.contourf(xx, yy, colors, levels=np.arange(len(unique_preds) + 1) - 0.5, cmap=cmap, alpha=0.7)

        # group the data by the labels/filenames (actual CCAs)
        grouped_data = {}
        for i in range(len(labels)):
            actual = labels[i].rstrip().rstrip('0123456789')
            if actual not in grouped_data:
                grouped_data[actual] = []
            grouped_data[actual].append(data[i])

        outliers = []

        # Scatterplot der Datenpunkte
        for cca in grouped_data:
            grouped_data[cca] = np.array(grouped_data[cca])
            # Farben für CCAs festlegen
            if (cca.lower() not in inverse_count_to_mp[degree]):
                color = 'black'
                outliers.append(cca)
            else:
                pred_id = inverse_count_to_mp[degree][cca.lower()]
                color = cmap(color_map[pred_id])
            ax.scatter(grouped_data[cca][:, 0], grouped_data[cca][:, 1], s=40, color=color, edgecolors='black')#, label=cca.upper())
        
        ax.set_title('Degree 2 Clustering')
        
        # Legende befüllen
        for pred_id in unique_preds:
            ax.scatter([], [], label=count_to_mp[degree][pred_id].upper(), color=cmap(color_map[pred_id]))
    
        if (len(outliers) > 0):
            str_outliers = "Wrong Degree: " + ', '.join(outliers)
            ax.scatter([], [], label=str_outliers.upper(), color='black')
                
        ax.legend(title='CCAs')
        ax.set_xlabel('c')
        ax.set_ylabel('b')
        
        # Fokus auf den Kernbereich
        ax.set_xlim(left=-3.5, right=3.5)
        ax.set_ylim(ymin=-3.5, ymax=3.5)
        
        if print_plot:
            plt.savefig(f"plots/probabilities-D{degree}.png")
        else:
            plt.show()
        plt.close(fig)
        