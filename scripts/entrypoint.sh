#!/bin/bash

# on gere les OPTIONS
while getopts ":f:" FLAG
do
    case $FLAG in
        f) script_python=$OPTARG  ;; # le nom du script python
        :) echo "Il manque un argument à '-$OPTARG'" ; exit 1 ;;
        \?) echo "L'option $OPTARG invalide" ; exit 1 ;;
    esac
done

# on gere les COMMANDES
shift $((OPTIND-1))
if [[ $# -gt 1 ]]; then
    echo "Il y a une commande en trop"
    exit 1
fi

if [[ -z $script_python ]]; then
    echo "Veuillez spécifier un script Python avec l'option -f"
    exit 1
fi

if [[ -f ${script_python} ]]; then
  echo "python ${script_python}"
  /usr/bin/env python3 ${script_python}
else
  echo "erreur de fichier"
  echo "${script_python}"
  exit 1
fi

