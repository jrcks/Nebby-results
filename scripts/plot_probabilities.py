import os
import pickle
import numpy as np
from sklearn.naive_bayes import GaussianNB
import matplotlib.pyplot as plt
from typing import Dict

pickle_dir = os.path.dirname(os.path.realpath(__file__)) + "/pickles"

scaled_vals: dict = pickle.load(open(pickle_dir + "/scaled_vals.txt","rb"))
classifiers: dict = pickle.load(open(pickle_dir + "/classifiers.txt","rb"))
count_to_mp: dict = pickle.load(open(pickle_dir + "/count_to_mp.txt","rb"))
degrees = [1,2,3]

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

results: Dict[str, ExtendedResult] = pickle.load(open(pickle_dir + "/a_results_extended.txt","rb"))

for degree in degrees:
    # TODO: Data and Probs für Outliers
    results_with_degree = [result for result in results.values() if result.degree == degree and result.bbr == "NO" and len(result.data) != 0]

    if (len(results_with_degree) == 0):
        print("No data for degree", degree)
        continue
    
    data = [res.data for res in results_with_degree]
    labels = [res.label for res in results_with_degree]
    
    clf: GaussianNB = classifiers[degree]
    
    if degree == 2:
        # Erstellen von 2D-Daten
        x = np.linspace(-3, 3, 100)
        y = np.linspace(-3, 3, 100)
        xx, yy = np.meshgrid(x, y)
        X_2d = np.c_[xx.ravel(), yy.ravel()]
        
        data = np.array(data)

        # Vorhersage der Klassen
        preds = clf.predict(X_2d)
        preds = preds.reshape(xx.shape)

        # Erstellen eines Farb-Mappings für die Kategorien
        unique_preds = np.unique(preds)
        color_map = {pred_id: i for i, pred_id in enumerate(unique_preds)}  # Mapping von IDs zu Farben
        colors = np.array([color_map[pred] for pred in preds.ravel()]).reshape(preds.shape)

        # Erstelle eine Farbkarte
        cmap = plt.get_cmap('RdBu', len(unique_preds))

        plt.figure(figsize=(10, 8))
        # Konturplot für die Klassen
        contour = plt.contourf(xx, yy, colors, levels=np.arange(len(unique_preds) + 1) - 0.5, cmap=cmap, alpha=0.7)

        # group the data by the labels/filenames (actual CCAs)
        grouped_data = {}
        for i in range(len(labels)):
            actual = labels[i].rstrip().rstrip('0123456789')
            if actual not in grouped_data:
                grouped_data[actual] = []
            grouped_data[actual].append(data[i])

        # Scatterplot der Datenpunkte
        for cca in grouped_data:
            grouped_data[cca] = np.array(grouped_data[cca])
            # TODO: Color
            color = 'black'
            plt.scatter(grouped_data[cca][:, 0], grouped_data[cca][:, 1], s=5, alpha=1, color=color, label=cca.upper())
        
        plt.title('Degree 2 Clustering')

        # Platz für die Namenslegende erstellen
        for pred_id in unique_preds:
            plt.scatter([], [], label=count_to_mp[degree][pred_id].upper(), color=cmap(color_map[pred_id]))
            
        plt.legend(title='CCAs')
        plt.xlabel('c')
        plt.ylabel('b')
        plt.show()