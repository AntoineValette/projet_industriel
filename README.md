# Projet n°7 : smartETL "DOR"

## 1. Pre requis 

- conda
- docker 
- git
- linux / unix / macos 
- python 3.12
- postgresql 17.2

## 2. usage 

Pour utiliser l'application, il faut exporter le code source à l'aide de git

```
git clone git@gitlab-student.centralesupelec.fr:PI7/smartETL.git
```

Puis utiliser docker composer pour lancer l'application
```
cd smartETL
docker compose build
docker compose up -d 
```

Pour quitter le docker 

```
docker down
```
