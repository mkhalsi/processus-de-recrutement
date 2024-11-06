import tkinter as tk
from tkinter import messagebox, simpledialog
import csv
import os
import uuid
import matplotlib.pyplot as plt

# Lists to store candidates and job offers
candidats = []
offres_emploi = []

# Load candidates from CSV file
def charger_candidats_depuis_csv():
    file_path = 'candidats.csv'  # Update this path if necessary

    if os.path.exists(file_path):
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                candidats.append(row)
    else:
        messagebox.showwarning("Erreur", "Le fichier CSV des candidats n'existe pas.")

# Load job offers from CSV file
def charger_offres_depuis_csv():
    file_path = 'offres_emploi.csv'  # Update this path if necessary

    if os.path.exists(file_path):
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                offres_emploi.append(row)
    else:
        messagebox.showwarning("Erreur", "Le fichier CSV des offres d'emploi n'existe pas.")

# Function to view candidates
def voir_candidats():
    if not candidats:
        messagebox.showinfo("Aucun Candidat", "Aucun candidat enregistré.")
        return
    
    candidats_str = "\n".join([
        f"ID: {c['id_candidat']}\nNom: {c['prenom']} {c['nom']}\nNiveau d'Éducation: {c['niveau_education']}\n"
        f"Expérience: {c['experience']} ans\nCompétences: {c['competences']}\nScore: {c['score_entretien']}\n"
        f"Source: {c['source_candidature']}\n" + "-" * 20 
        for c in candidats
    ])
    
    messagebox.showinfo("Liste des Candidats", candidats_str)

# Function to view job offers
def voir_offres():
    if not offres_emploi:
        messagebox.showinfo("Aucune Offre", "Aucune offre d'emploi enregistrée.")
        return
    
    offres_str = "\n".join([
        f"ID: {o['id_poste']}\nIntitulé: {o['intitule_poste']}\nDépartement: {o['departement']}\n"
        f"Niveau d'Expérience: {o['niveau_experience_requis']}\nSalaire: {o['salaire']} €\n" + "-" * 10 
        for o in offres_emploi
    ])
    
 # offres_str = "\n".join([
  # f"ID: {o.get('id_poste', 'N/A')}\nIntitulé: {o.get('intitule_poste', 'N/A')}\nDépartement: {o.get('departement', 'N/A')}\n"
   
#   f"Niveau d'Expérience: {o.get('niveau_experience_requis', 'N/A')}\nSalaire: {o.get('salaire', 'N/A')} €\n" + "-" * 10
 #   for o in offres_emploi
#]) 

    messagebox.showinfo("Liste des Offres d'Emploi", offres_str)

# Function to manually add a candidate
def ajouter_candidat():
    nom = simpledialog.askstring("Nom du Candidat", "Entrez le nom du candidat:")
    prenom = simpledialog.askstring("Prénom du Candidat", "Entrez le prénom du candidat:")
    niveau_education = simpledialog.askstring("Niveau d'Éducation", "Entrez le niveau d'éducation (ex: Licence, Master):")
    experience = simpledialog.askinteger("Expérience", "Entrez le nombre d'années d'expérience:")
    competences = simpledialog.askstring("Compétences", "Entrez les compétences du candidat (ex: SQL, Java):")
    score_entretien = simpledialog.askinteger("Score d'entretien", "Entrez le score d'entretien du candidat:")
    source_candidature = simpledialog.askstring("Source de la Candidature", "Entrez la source de la candidature (ex: LinkedIn):")
    
    if nom and prenom and niveau_education and experience is not None and competences and score_entretien is not None and source_candidature:
        id_candidat = str(uuid.uuid4())
        candidats.append({
            'id_candidat': id_candidat,
            'nom': nom,
            'prenom': prenom,
            'niveau_education': niveau_education,
            'experience': experience,
            'competences': competences,
            'score_entretien': score_entretien,
            'source_candidature': source_candidature
        })
        messagebox.showinfo("Candidat Ajouté", f"{prenom} {nom} a été ajouté avec succès!")
    else:
        messagebox.showwarning("Erreur", "Tous les champs doivent être remplis.")

# Function to manually add a job offer
def ajouter_offre():
    intitule_poste = simpledialog.askstring("Intitulé du Poste", "Entrez l'intitulé du poste:")
    departement = simpledialog.askstring("Département", "Entrez le département:")
    niveau_experience_requis = simpledialog.askstring("Niveau d'Expérience Requis", "Entrez le niveau d'expérience requis:")
    salaire = simpledialog.askinteger("Salaire", "Entrez le salaire proposé:")
    
    if intitule_poste and departement and niveau_experience_requis and salaire is not None:
        id_offre = str(uuid.uuid4())
        offres_emploi.append({
            'id_offre': id_offre,
            'intitule_poste': intitule_poste,
            'departement': departement,
            'niveau_experience_requis': niveau_experience_requis,
            'salaire': salaire
        })
        messagebox.showinfo("Offre Ajoutée", f"L'offre '{intitule_poste}' a été ajoutée avec succès!")
    else:
        messagebox.showwarning("Erreur", "Tous les champs doivent être remplis.")

# Function to follow applications
def suivi_candidatures():
    messagebox.showinfo("Suivi des Candidatures", "Fonctionnalité à développer.")

# Function to view recruitment statistics
def statistiques_recrutement():
    nombre_candidats = len(candidats)
    nombre_offres = len(offres_emploi)
    messagebox.showinfo("Statistiques", f"Nombre de Candidats: {nombre_candidats}\nNombre d'Offres d'Emploi: {nombre_offres}")

# Function to display recruitment data visualization
def afficher_graphique():
    if not candidats:
        messagebox.showinfo("Aucun Candidat", "Aucun candidat enregistré.")
        return
    
    # Count candidates by source
    sources = {}
    for candidat in candidats:
        source = candidat['source_candidature']
        if source in sources:
            sources[source] += 1
        else:
            sources[source] = 1

    # Prepare data for plotting
    labels = list(sources.keys())
    values = list(sources.values())

    # Create a bar chart
    plt.bar(labels, values, color='blue')
    plt.xlabel('Sources de Candidature')
    plt.ylabel('Nombre de Candidats')
    plt.title('Nombre de Candidats par Source de Candidature')
    plt.xticks(rotation=45)
    plt.tight_layout()  # Adjust layout to make room for rotated labels
    plt.show()

# Function to quit the application
def quitter_application():
    root.quit()

# Main application window
root = tk.Tk()
root.title("Application de Recrutement")

# Load data from CSV files at startup
charger_candidats_depuis_csv()
charger_offres_depuis_csv()

# Create buttons
btn_ajouter_candidat = tk.Button(root, text="Ajouter un Candidat", command=ajouter_candidat)
btn_ajouter_candidat.pack(pady=10)

btn_voir_candidats = tk.Button(root, text="Voir les Candidats", command=voir_candidats)
btn_voir_candidats.pack(pady=10)

btn_ajouter_offre = tk.Button(root, text="Ajouter une Offre d'Emploi", command=ajouter_offre)
btn_ajouter_offre.pack(pady=10)

btn_voir_offres = tk.Button(root, text="Voir les Offres d'Emploi", command=voir_offres)
btn_voir_offres.pack(pady=10)

btn_suivi_candidatures = tk.Button(root, text="Suivi des Candidatures", command=suivi_candidatures)
btn_suivi_candidatures.pack(pady=10)

btn_statistiques = tk.Button(root, text="Statistiques de Recrutement", command=statistiques_recrutement)
btn_statistiques.pack(pady=10)

btn_graphique = tk.Button(root, text="Afficher Graphique", command=afficher_graphique)
btn_graphique.pack(pady=10)

btn_quitter = tk.Button(root, text="Quitter", command=quitter_application)
btn_quitter.pack(pady=10)

# Run the main loop
root.mainloop()
