# Projet n°7 : smartETL "DOR"

## 1. Pile logicielle 

- conda
- docker 
- git
- linux / unix / macos 
- python 3.12
- postgresql 17.2

## 2. Pré-requis 

2.1 exporter le dépot 
```
git clone git@gitlab-student.centralesupelec.fr:PI7/smartETL.git
```

2.2 mettre les fichiers de log dans le répertoire smartETL/data


## 3. Run

P our lancer l'application : 
```
cd smartETL
docker compose build
docker compose up -d 
```

Pour quitter le docker 

```
docker down
```
