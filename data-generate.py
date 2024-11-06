import pandas as pd
import random
from faker import Faker

# Initialisation
fake = Faker()
Faker.seed(0)

# Configuration de la quantité de données à générer
num_candidates = 100
num_jobs = 10
num_applications = 150

# Génération de la Table Candidats
candidats_data = []
for _ in range(num_candidates):
    candidats_data.append({
        "id_candidat": fake.unique.uuid4(),
        "nom": fake.last_name(),
        "prenom": fake.first_name(),
        "niveau_education": random.choice(["Licence", "Master", "Doctorat"]),
        "experience": random.randint(0, 15),
        "competences": ", ".join(random.sample(["Python", "SQL", "Java", "C++", "Machine Learning", "Data Analysis"], 3)),
        "score_entretien": random.randint(0, 100),
        "source_candidature": random.choice(["LinkedIn", "Indeed", "Monster", "Recrutement Interne", "Autre"])
    })

candidats_df = pd.DataFrame(candidats_data)

# Génération de la Table Offres d'Emploi
jobs_data = []
for _ in range(num_jobs):
    jobs_data.append({
        "id_poste": fake.unique.uuid4(),
        "intitule_poste": random.choice(["Data Scientist", "Développeur Python", "Analyste", "Chef de Projet", "Consultant"]),
        "departement": random.choice(["Informatique", "Ressources Humaines", "Finance", "Marketing", "Opérations"]),
        "niveau_experience_requis": random.choice(["Junior", "Intermédiaire", "Senior"]),
        "date_publication": fake.date_this_year(),
        "salaire": random.randint(30000, 80000)
    })

jobs_df = pd.DataFrame(jobs_data)

# Génération de la Table Suivi Candidatures
applications_data = []
for _ in range(num_applications):
    applications_data.append({
        "id_candidat": random.choice(candidats_df["id_candidat"]),
        "id_poste": random.choice(jobs_df["id_poste"]),
        "etape": random.choice(["Pré-sélection", "Entretien", "Offre envoyée", "Rejeté"]),
        "date_entree_etape": fake.date_this_year()
    })

applications_df = pd.DataFrame(applications_data)

# Affichage des premières lignes des tables
print("Table Candidats:")
print(candidats_df.head())
print("\nTable Offres d'Emploi:")
print(jobs_df.head())
print("\nTable Suivi Candidatures:")
print(applications_df.head())
candidats_df.to_csv("candidats.csv", index=False)
jobs_df.to_csv("offres_emploi.csv", index=False)
applications_df.to_csv("suivi_candidatures.csv", index=False)
