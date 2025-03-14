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
## Config
### Grafana 
C'est ici que sont stockés les modèles des différents dashboards, la connexion à la base Postgres et un exemple d'alerte. Le plus simple pour éditer ces fichiers est de la faire directement dans Grafana et les exporter à nouveau pour enregistrer les modificiations.

### Airflow
Fichiers de config d'airflow, transparents pour l'utilisateur. Le paramètrage des jobs d'Airflow est situé dans :
- ./python/dags/test_dag.py (un dag de test pour tester le conteneur)
- ./python/dags/fusion_dag.py (le dag qui met à jour la table dataset dans Postgres toutes les heures avec les données intégrées par Kafka)

### Postgres
Fichier de configuration de Postgres. 

---
## Notebook
Historiquement, on a commencé l'analyse 