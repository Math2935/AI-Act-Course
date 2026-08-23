---
license: mit
language:
- fr
datasets:
- iris
metrics:
- accuracy
- f1
pipeline_tag: tabular-classification
---

## Model Details

    Model name : iris_classifier
    Author : math2935_for_liora_course
    Date : 2026 08 18
    Version : 1.0
    Model type : RandomForestClassifier (scikit-learn)
    License : MIT


## Intended Use

    Intended Use Cases : Ce modèle sert à classer des iris et est destiné à tous ceux qui s'intéressent à ces fleurs, pour un usage domestique pour identifier les différentes variétés d'iris.

    Out-of-scope Use : Ce modèle n'est pas destiné pour un usage en production ni pour prendre des décisions à fort enjeu.


## Factors (Facteurs)

    La précision de la mesure de la longueur et de la largeur des sépales et pétales influe sur les performances du modèle.

    L'équilibre des classes dans les données d'entrainement est globalement respecté mais ce jeu de données d'entrainement est de petite taille.


## Metrics (Métriques)

    Les métriques qui ont été utilisées pour évaluer le modèles sont les suivantes :
    - la precision : le modèle a-t-il raison quand il prédit une classe ? Utile si le coût des faux positifs est élevé. C'est sur la base de la précision que le modèle a été entrainé.
    - le recall : parmi tous les vrai exemple d'une classe, combien le modèle en a-t-il retrouvé ? Utile si rater un cas est coûteux.
    - le f1-score : compromis entre les deux précédents, utile aussi en cas de déséquilibre des classes (ce qui n'est pas le cas ici).


## Training Data (Données d'entraînement)

    Nom du dataset d'entrainement : Iris flower dataset.
    
    Source : sklearn.datasets.load_iris.
    
    Taille : 120 exemples utilisés pour l'entrainement, représentant les classes à prédire de manière équilibrée.
    
    Variables d'entrées : 
        - sepal length (cm) ; 
        - sepal width (cm) ; 
        - petal length (cm) ; 
        - petal width (cm).
    
    Cibles :
        - setosa ;
        - versicolor ;
        - virginica.


## Evaluation Data (Données d'évaluation)

    Source : même dataset que pour l'entraînement (Iris), obtenu par train_test_split
    
    Taille : 30 exemples utilisés pour l'évaluation, représentant les classes à prédire de manière équilibrée.
    
    Méthode de séparation : sklearn.model_selection.train_test_split avec 20% des données pour l'évaluation et une graine aléatoire de 42.
    
    Prétraitement : aucun.


## Quantitative Analyses (Analyses quantitatives)

    Les performances obtenues sont homogènes pour les 3 classes à prédire et pour l'ensemble des métriques.


## Ethical Considerations (Considérations éthiques)

    Risques d'usage : le modèle a été réalisé dans un but pédagogique, sur un petit jeu de données et ne devrait pas être utilisé dans un contexte à fort enjeu.

    Biais potentiels : seules trois variétés d'iris apparaissent dans le dataset et ce dernier a été entrainé sur peu d'exemples obtenus dans des conditions inconnues (viennent-ils tous d'une même région ? etc...) Un iris de l'une des variétés identifiée dans le dataset mais poussant dans des conditions différentes, une variété d'iris n'apparaissant pas dans le dataset, une autre plante mal identifée comme iris par l'utilisateur pourrait retourner une mauvaise identification.


## Caveats and Recommendations (Limites et recommandations)

    Le jeu d'entrainement étant très petit, ne déployez pas ce modèle avant une robuste validation supplémentaire.

    Le jeu de test étant très petit, il est fortement recommandé de collecter des données de tests supplémentaires obtenues dans des conditions variées.


## Reproductibility

    Git commit (git_sha): 9f566874721bb97867316b8f539aafa2813c434e
    MLflow run_id: N/A (non utilisé dans ce chapitre)
    Dataset hash: N/A (non utilisé dans ce chapitre)
