import csv
import os
import psycopg2

from core.coreLog import log
from core.settings import Settings

def import_myreport_reseau_full():
    log("Connexion à PostgreSQL")
    conn = psycopg2.connect(Settings.POSTGRES_URL)
    cur = conn.cursor()

    log("extract myreport_reseau_full")
    filename = "/data/logServer/myreport_reseau_full.csv"
    if os.path.isfile(filename):
        with open(filename, 'r', encoding='utf-8-sig') as f:
            reader = csv.DictReader(f, delimiter=',', quoting=csv.QUOTE_MINIMAL)
            next(reader)
            for row in reader:
                if not row[reader.fieldnames[2]]:
                    continue
                if any("Moyennes" in value for value in row.values()):
                    continue
                if any("Sommes" in value for value in row.values()):
                    continue
                cur.execute("""INSERT INTO myreport_reseau (
                        Date, heureDate_RAW,
                        Somme_Volume, Somme_Volume_RAW,  Somme_Debit, Somme_Debit_RAW,
                        Trafic_Entrant_Volume, Trafic_Entrant_Volume_RAW, Trafic_Entrant_Debit, Trafic_Entrant_Debit_RAW,
                        Trafic_Sortant_Volume, Trafic_Sortant_Volume_RAW, Trafic_Sortant_Debit, Trafic_Sortant_Debit_RAW,
                        Paquets_Volume, Paquets_Volume_RAW, Paquets_Debit, Paquets_Debit_RAW,
                        Paquets_Refus_Volume, Paquets_Refus_Volume_RAW, Paquets_Refus_Debit, Paquets_Refus_Debit_RAW,
                        Paquets_Envoyes_Volume, Paquets_Envoyes_Volume_RAW, Paquets_Envoyes_Debit, Paquets_Envoyes_Debit_RAW,
                        Monodiffusion_entrante_Volume, Monodiffusion_entrante_Volume_RAW,
                        Monodiffusion_entrante_Debit, Monodiffusion_entrante_Debit_RAW,
                        Monodiffusion_sortante_Volume, Monodiffusion_sortante_Volume_RAW,
                        Monodiffusion_sortante_Debit, Monodiffusion_sortante_Debit_RAW,
                        Paquets_non_monodiffusion_entrants_Volume, Paquets_non_monodiffusion_entrants_Volume_RAW,
                        Paquets_non_monodiffusion_entrants_Debit, Paquets_non_monodiffusion_entrants_Debit_RAW,
                        Paquets_non_monodiffusion_sortants_Volume, Paquets_non_monodiffusion_sortants_Volume_RAW,
                        Paquets_non_monodiffusion_sortants_Debit, Paquets_non_monodiffusion_sortants_Debit_RAW,
                        Erreurs_entrantes_Volume, Erreurs_entrantes_Volume_RAW,
                        Erreurs_entrantes_Debit, Erreurs_entrantes_Debit_RAW,
                        Erreurs_sortantes_Volume, Erreurs_sortantes_Volume_RAW,
                        Erreurs_sortantes_Debit, Erreurs_sortantes_Debit_RAW,
                        Entrants_rejets_Volume, Entrants_rejets_Volume_RAW,
                        Entrants_rejets_Debit, Entrants_rejets_Debit_RAW,
                        Sortants_rejets_Volume, Sortants_rejets_Volume_RAW,
                        Sortants_rejets_Debit, Sortants_rejets_Debit_RAW,
                        Protocoles_inconnus_entrants_Volume, Protocoles_inconnus_entrants_Volume_RAW,
                        Protocoles_inconnus_entrants_Debit, Protocoles_inconnus_entrants_Debit_RAW,
                        Temps_mort, Temps_mort_RAW, Couverture, Couverture_RAW
                    ) VALUES (
                        %s, %s, %s, %s, 
                        %s, %s, %s, %s,
                        %s, %s, %s, %s,
                        %s, %s, %s, %s,
                        %s, %s, %s, %s,
                        %s, %s, %s, %s,
                        %s, %s, %s, %s,
                        %s, %s, %s, %s,
                        %s, %s, %s, %s,
                        %s, %s, %s, %s,
                        %s, %s, %s, %s,
                        %s, %s, %s, %s,
                        %s, %s, %s, %s,
                        %s, %s, %s, %s,
                        %s, %s, %s, %s,
                        %s, %s, %s, %s,
                        %s, %s
                    )
                """, tuple(row.values()))
        log("extract myreport_reseau_full [ok]")
        conn.commit()

    cur.close()
    conn.close()
    log("fermeture de la connexion PostgreSQL")