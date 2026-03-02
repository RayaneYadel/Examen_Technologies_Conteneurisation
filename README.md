# Examen — Technologies de Conteneurisation (Docker)

## Projet : réduction de dimension (**PCA / TruncatedSVD / UMAP**) + comparaison via la métrique **trustworthiness** + Utilisation de **Docker**.

## Membres du groupes:
Rayane YADEL
Louis VANDAME
Othman ASLOUN

---

## Démarrage rapide

### 1) Initialisation (venv)
À lancer une seule fois :

```bash
bash init.sh
```

> `init.sh` crée un environnement virtuel Python (`venv`) et installe les dépendances (via `requirements.txt`).

---

## Structure du projet

- `data/`
  - `city_lifestyle_dataset.csv` (dataset)
  - `kaggle_readme.md`
- `notebooks/`
  - `pca.ipynb`
  - `truncated_svd.ipynb`
  - `UMAP_analysis.ipynb`
- `outputs/`
  - `pca_emb_2d.csv`
  - `truncated_svd_emb_2d.csv`
  - `umap_emb_2d.csv`
- `evaluate.py` : calcule la trustworthiness pour chaque méthode
- `requirements.txt`
- `Dockerfile`
- `init.sh`

---

## Exigences (énoncé)

### I. Réduction de dimension (par méthode)
Chaque notebook doit :
1) projeter les données en **2D** et afficher un graphique 2D  
2) écrire une **courte observation** sur la structure obtenue  
3) **exporter** les données 2D dans `outputs/`

### II. Comparaison des méthodes
`evaluate.py` doit :
- charger les exports 2D (`outputs/*.csv`)
- calculer **trustworthiness** pour chaque méthode (valeur entre 0 et 1)
- afficher les résultats (plus proche de 1 = voisinages mieux préservés)

---



## 🐳 Utilisation de Docker

Le projet est entièrement conteneurisé pour garantir la reproductibilité des résultats.

### Instructions :
1. *Build de l'image* :
   ```bash
   docker build -t examen-conteneur .
   ```
2. *Lancement de l'évaluation* :
   ```bash
   docker run examen-conteneur
   ```

### Interprétation des résultats :
On observe une égalité de score entre *PCA* et *SVD* (0.8609). Cela s'explique par la nature linéaire de ces deux méthodes qui utilisent une décomposition mathématique similaire sur ce dataset. L'*UMAP* obtient un score très proche (0.8599), montrant une excellente conservation globale des voisinages.

