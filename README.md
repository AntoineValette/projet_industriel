# Projet n°7 : smartETL "DOR"

## 💡 Description

- Projet industriel Smart ETL qui a pour objectif de valoriser les logs des ETLs pour l'équipe Data de Primever. 
---

## ⚠️ Pré-requis 

- conda
- docker 
- git
- linux / unix / macos 
- python 3.12
- postgresql 17.2

---
```
git clone git@gitlab-student.centralesupelec.fr:PI7/smartETL.git
```

Déplacer les fichiers logs dans le répertoire ./data du repertoire cloné

------
## 👩‍💻 Developpement

```
conda create -n smartETL-dev
conda activate smartETL-dev
conda install python=3.12.8
conda install sqlalchemy pandas psycopg2 fastparquet
conda install jupyterlab matplotlib seaborn scikit-learn numpy  plotly lxml   pyarrow apache-airflow confluent-kafka    
```
Regénérer le fichier requirements-dev.txt
```
pip list --format=freeze > requirements.txt 
```
---
## 🚀 Run

Pour lancer l'application : 
```
# construit les images docker 
docker compose build 

# lance le docker compose 
docker compoose up -d

# supprime le docker compose mais garde le volume 
docker compose down 

# supprime le docker compose avec les volumes 
docker compose down -v 
```

NB: pour générer le fichier conda pour la prod : 
```
git clone git@gitlab-student.centralesupelec.fr:PI7/smartETL.git
cd smartETL
conda create -n smartETL
conda activate smartETL
conda install python=3.12.8
conda install sqlalchemy pandas psycopg2  fastparquet

pip list --format=freeze > requirements.txt 
```
---
## 🌳 Arborescence du projet

L'arborescence ci-dessous présente la structure complète du projet. Chaque section est commentée pour indiquer son rôle ou son contenu principal.
```
smartETL
├── conf
│    ├── airflow                         # fichiers de config pour airflow (il existe un volume pour les plugins). Les jobs sont définis dans ./python/dags/
│    │    └── plugins     
│    ├── grafana                         # fichiers de config pour Grafane
│    │    ├── dashboards                  # ensemble des moidèles des dashboards - à modifier directement dans Grafana, mais à sauvegarder ici pour éviter une suppression accidentelle avec un docker compose down -v 
│    │    └── provisioning                # config de la source de données (connexion à Postgres automatique avec ID commun) + un exemple d'un fichier d'alerting + un fichier de config dashboard annexe
│    └── postgresql                      # paramètrage de Postgres - modifier user et mdp
├── data                                # ensemble des fichiers .csv et .parquet qui sont utilisées par l'appli : à priori les paths seront à modifier pour correspondre à l'arborescence de la VM
│    ├── ...
├── doc                                 # des schémas et une arborescence détaillée
│    ├── ...
├── docker                              # ensemble des dockerfiles, requirements et entrypoints (si besoin) pour les images qui sont personnalisées
│    ├── airflow
│    ├── kafka
│    └── python
├── notebook                            # un historique des notebooks utilisées pendant les premières phases du projet. Pas nécessaire au bon fonctionnement de l'appli, mais utile pour les curieux.
│    └── ...
├── postgresql                          # Fichier de configuration des tables de Postgres. 
└── python                              # ensemble des scripts (scripts d'initilisation et jobs orchestrés par Airflow)
    ├── ETL                             # ensemble des scripts de chargement des logs à l'initialisation
    │    └── ...
    ├── core                            # fonctions et méthodes communes (notamment un script de classification des erreurs)
    │    └── ...
    ├── dags                            # configuation des jobs (un job test et ub job fusion) orchestré par Airflow + des fonctions de transformations de datafraame
    │    └── ...
    ├── init                            # init standard
    ├── kfk                             # scripts pour le streaming avec Kafka
    │    ├── consumer
    │    └── producer
    └── waiting                         # fonctions de synchronisation (pemet d'attendre la fin du lancement/execution de certains services/scripts qui n'est pas possible avec la parmètrage isHealthy de Docker Compose)
    └── consumer.py                     # produit (envoie) des messages vers un ou plusieurs topics Kafka
    └── producer.py                     # s’abonne à un ou plusieurs topics, et lit en continu les messages qui y sont publiés

```

---
## 📓 Notebooks
Historiquement, on a commencé l'analyse des différents fichiers .csv de logs avec des notebooks jupyter. Ces notebooks sont plutôt bien commenté.
Pour les curieux, le notebook ./notebook/fusion/fusion_log-logerreur.ipynb est très similaire à ./python/dags/fusion_dag.py. Le notebook est à l'origine de l'aggregation des sources pour créer la VO de dataset. NB : la table dataset finale dans Postgres est légèrement différente au finale. 

---
## 💡 Tips & Tricks 

### Grafana 
Pour éditer les dashboards, le plus simple est de le faire directement dans Grafana. En les enregistrant via l'interface de Grafana, les dashboards modifiés seront enregistrés dans un volume.

⚠️ ATTENTION : avec une suppression des volumes (docker compose down -v), les modifications de dashboards existants et la création de nouveaux dashboards seraient perdues. 

⚠️ Il est donc fortement, fortement conseillé d'enregister les dashboards ET de les ***exporter en JSON*** à nouveau dans ./conf/grafana/dahboards. 

### Airflow
Le paramètrage des jobs d'Airflow est situé dans :
- ./python/dags/test_dag.py : un dag de test pour tester le conteneur et le fonctionement d'Airflow. Ce job n'a pas d'autre utilité
- ./python/dags/fusion_dag.py : le dag qui met à jour la table dataset dans Postgres toutes les heures avec les données intégrées par Kafka

Les autres jobs peuvent êtres créés ici. 
