import pandas as pd
import os
from sklearn.manifold import trustworthiness

def evaluate_methods():
    # 1. Chargement des données originales pour la comparaison
    print("--- Évaluation des méthodes de réduction de dimension ---")
    data_path = 'data/city_lifestyle_dataset.csv'
    df_orig = pd.read_csv(data_path)
    X_original = df_orig.drop(['city_name', 'country'], axis=1)

    # 2. Liste des méthodes à tester (basée sur la structure demandée)
    methods = {
        "PCA": "outputs/pca_emb_2d.csv",
        "SVD": "outputs/truncated_svd_emb_2d.csv",
        "UMAP": "outputs/umap_emb_2d.csv"
    }

    results = []

    for name, path in methods.items():
        if os.path.exists(path):
            # Chargement des données réduites
            X_reduced = pd.read_csv(path)
            
            # Calcul de la métrique trustworthiness (Voisinage préservé)
            # Valeur entre 0 et 1 : proche de 1 = excellente préservation locale
            score = trustworthiness(X_original, X_reduced, n_neighbors=10)
            results.append({"Méthode": name, "Trustworthiness": round(score, 4)})
        else:
            results.append({"Méthode": name, "Trustworthiness": "Fichier manquant"})

    # 3. Affichage des résultats
    report = pd.DataFrame(results)
    print("\n", report.to_string(index=False))
    print("\nNote: Un score proche de 1 indique une meilleure préservation locale des données.")

if __name__ == "__main__":
    evaluate_methods()