#!/bin/sh

# Attendre que PostgreSQL soit prêt
python wait_for_postgres.py

# Lancer les scripts d'importation
python import_csv.py
python import_parquet.py

