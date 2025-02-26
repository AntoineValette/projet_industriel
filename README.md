# Projet n°7 : smartETL "DOR"

## 💡 Description

---

## ⚠️ Pré-requis 

--- 
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


## 👩‍💻 Developpement

------

```
conda create -n smartETL-dev
conda activate smartETL-dev
conda install python=3.12.8
conda install sqlalchemy pandas psycopg2 
conda install jupyterlab matplotlib seaborn scikit-learn numpy
```
Regénérer le fichier requirements-dev.txt
```
pip list --format=freeze > requirements.txt 
```

## 🚀 Run

---

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
conda install sqlalchemy pandas psycopg2 

pip list --format=freeze > requirements.txt 
```