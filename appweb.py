import os
import csv
import uuid
import tkinter as tk 
from tkinter import ttk
from tkinter import messagebox, simpledialog, Toplevel, Label, Entry, Button
import matplotlib.pyplot as plt

# Initialisation des listes globales pour les candidats et les offres d'emploi
candidats = []
offres_emploi = []

# Charger les candidats depuis un fichier CSV
def charger_candidats_depuis_csv():
    file_path = 'candidats.csv'  
    if os.path.exists(file_path):
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                candidats.append(row)
    else:
        messagebox.showwarning("Erreur", "Le fichier CSV des candidats n'existe pas.")

# Charger les offres d'emploi depuis un fichier CSV
def charger_offres_depuis_csv():
    file_path = 'offres_emploi.csv' 
    if os.path.exists(file_path):
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                offres_emploi.append(row)
    else:
        messagebox.showwarning("Erreur", "Le fichier CSV des offres d'emploi n'existe pas.")

# Afficher les candidats dans un tableau
def voir_candidats():
    if not candidats:
        messagebox.showinfo("Aucun Candidat", "Aucun candidat enregistré.")
        return

    fenetre_candidats = Toplevel()
    fenetre_candidats.title("Liste des Candidats")

    # Création du tableau avec des en-têtes
    table = ttk.Treeview(fenetre_candidats, columns=("ID", "Nom", "Prénom", "Niveau d'Éducation", "Expérience", "Compétences", "Score", "Source"), show="headings")
    table.heading("ID", text="ID")
    table.heading("Nom", text="Nom")
    table.heading("Prénom", text="Prénom")
    table.heading("Niveau d'Éducation", text="Niveau d'Éducation")
    table.heading("Expérience", text="Expérience")
    table.heading("Compétences", text="Compétences")
    table.heading("Score", text="Score")
    table.heading("Source", text="Source")

    # Insérer les candidats dans le tableau
    for c in candidats:
        table.insert("", "end", values=(c["id_candidat"], c["nom"], c["prenom"], c["niveau_education"], c["experience"], c["competences"], c["score_entretien"], c["source_candidature"]))

    table.pack(fill="both", expand=True)

# Afficher les offres d'emploi dans un tableau
def voir_offres():
    if not offres_emploi:
        messagebox.showinfo("Aucune Offre", "Aucune offre d'emploi enregistrée.")
        return

    fenetre_offres = Toplevel()
    fenetre_offres.title("Liste des Offres d'Emploi")

    # Création du tableau avec des en-têtes
    table = ttk.Treeview(fenetre_offres, columns=("ID", "Intitulé", "Département", "Niveau d'Expérience", "Salaire"), show="headings")
    table.heading("ID", text="ID")
    table.heading("Intitulé", text="Intitulé")
    table.heading("Département", text="Département")
    table.heading("Niveau d'Expérience", text="Niveau d'Expérience")
    table.heading("Salaire", text="Salaire")

    # Insérer les offres dans le tableau
    for o in offres_emploi:
        table.insert("", "end", values=(o["id_poste"], o["intitule_poste"], o["departement"], o["niveau_experience_requis"], o["salaire"]))

    table.pack(fill="both", expand=True)
    
 

# Sauvegarder les candidats dans le fichier CSV
def sauvegarder_candidats_vers_csv():
    with open('candidats.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['id_candidat', 'prenom', 'nom', 'niveau_education', 'experience', 'competences', 'score_entretien', 'source_candidature'])
        writer.writeheader()
        for candidat in candidats:
            writer.writerow(candidat)

# Sauvegarder les offres d'emploi dans le fichier CSV
def sauvegarder_offres_vers_csv():
    with open('offres_emploi.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['id_poste', 'intitule_poste', 'departement', 'niveau_experience_requis', 'salaire'])
        writer.writeheader()
        for offre in offres_emploi:
            writer.writerow(offre)
# Fonction pour ajouter un candidat avec un formulaire dans une fenêtre
def ajouter_candidat():
    def soumettre_candidat():
        nom = entry_nom.get()
        prenom = entry_prenom.get()
        niveau_education = entry_education.get()
        experience = entry_experience.get()
        competences = entry_competences.get()
        score_entretien = entry_score.get()
        source_candidature = entry_source.get()

        if nom and prenom and niveau_education and experience and competences and score_entretien and source_candidature:
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
            sauvegarder_candidats_vers_csv()  # Sauvegarder les candidats
            messagebox.showinfo("Candidat Ajouté", f"{prenom} {nom} a été ajouté avec succès!")
            fenetre_ajout.destroy()
        else:
            messagebox.showwarning("Erreur", "Tous les champs doivent être remplis.")

    fenetre_ajout = Toplevel()
    fenetre_ajout.title("Ajouter un Candidat")

    # Labels et champs de saisie
    Label(fenetre_ajout, text="Nom:").grid(row=0, column=0, padx=5, pady=5)
    entry_nom = Entry(fenetre_ajout)
    entry_nom.grid(row=0, column=1, padx=5, pady=5)

    Label(fenetre_ajout, text="Prénom:").grid(row=1, column=0, padx=5, pady=5)
    entry_prenom = Entry(fenetre_ajout)
    entry_prenom.grid(row=1, column=1, padx=5, pady=5)

    Label(fenetre_ajout, text="Niveau d'Éducation:").grid(row=2, column=0, padx=5, pady=5)
    entry_education = Entry(fenetre_ajout)
    entry_education.grid(row=2, column=1, padx=5, pady=5)

    Label(fenetre_ajout, text="Expérience (ans):").grid(row=3, column=0, padx=5, pady=5)
    entry_experience = Entry(fenetre_ajout)
    entry_experience.grid(row=3, column=1, padx=5, pady=5)

    Label(fenetre_ajout, text="Compétences:").grid(row=4, column=0, padx=5, pady=5)
    entry_competences = Entry(fenetre_ajout)
    entry_competences.grid(row=4, column=1, padx=5, pady=5)

    Label(fenetre_ajout, text="Score d'entretien:").grid(row=5, column=0, padx=5, pady=5)
    entry_score = Entry(fenetre_ajout)
    entry_score.grid(row=5, column=1, padx=5, pady=5)

    Label(fenetre_ajout, text="Source de la Candidature:").grid(row=6, column=0, padx=5, pady=5)
    entry_source = Entry(fenetre_ajout)
    entry_source.grid(row=6, column=1, padx=5, pady=5)

    # Bouton de soumission
    Button(fenetre_ajout, text="Soumettre", command=soumettre_candidat).grid(row=7, columnspan=2, pady=10)

# Fonction pour ajouter une offre d'emploi avec un formulaire dans une fenêtre
def ajouter_offre():
    def soumettre_offre():
        intitule_poste = entry_intitule.get()
        departement = entry_departement.get()
        niveau_experience_requis = entry_niveau.get()
        salaire = entry_salaire.get()

        if intitule_poste and departement and niveau_experience_requis and salaire:
            id_offre = str(uuid.uuid4())
            offres_emploi.append({
                'id_offre': id_offre,
                'intitule_poste': intitule_poste,
                'departement': departement,
                'niveau_experience_requis': niveau_experience_requis,
                'salaire': salaire
            })
            sauvegarder_offres_vers_csv() 
            messagebox.showinfo("Offre Ajoutée", f"L'offre '{intitule_poste}' a été ajoutée avec succès!")
            fenetre_ajout.destroy()
        else:
            messagebox.showwarning("Erreur", "Tous les champs doivent être remplis.")

    fenetre_ajout = Toplevel()
    fenetre_ajout.title("Ajouter une Offre d'Emploi")

    # Labels et champs de saisie
    Label(fenetre_ajout, text="Intitulé du Poste:").grid(row=0, column=0, padx=5, pady=5)
    entry_intitule = Entry(fenetre_ajout)
    entry_intitule.grid(row=0, column=1, padx=5, pady=5)

    Label(fenetre_ajout, text="Département:").grid(row=1, column=0, padx=5, pady=5)
    entry_departement = Entry(fenetre_ajout)
    entry_departement.grid(row=1, column=1, padx=5, pady=5)

    Label(fenetre_ajout, text="Niveau d'Expérience Requis:").grid(row=2, column=0, padx=5, pady=5)
    entry_niveau = Entry(fenetre_ajout)
    entry_niveau.grid(row=2, column=1, padx=5, pady=5)

    Label(fenetre_ajout, text="Salaire:").grid(row=3, column=0, padx=5, pady=5)
    entry_salaire = Entry(fenetre_ajout)
    entry_salaire.grid(row=3, column=1, padx=5, pady=5)

    # Bouton de soumission
    Button(fenetre_ajout, text="Soumettre", command=soumettre_offre).grid(row=4, columnspan=2, pady=10)



# Suivi des candidatures (à développer)
def suivi_candidatures():
    messagebox.showinfo("Suivi des Candidatures", "Fonctionnalité à développer.")

# Afficher les statistiques de recrutement
def statistiques_recrutement():
    nombre_candidats = len(candidats)
    nombre_offres = len(offres_emploi)
    messagebox.showinfo("Statistiques", f"Nombre de Candidats: {nombre_candidats}\nNombre d'Offres d'Emploi: {nombre_offres}")

# Afficher un graphique des candidats par source
def afficher_graphique():
    if not candidats:
        messagebox.showinfo("Aucun Candidat", "Aucun candidat enregistré.")
        return
    
    # Compter les candidats par source
    sources = {}
    for candidat in candidats:
        source = candidat['source_candidature']
        if source in sources:
            sources[source] += 1
        else:
            sources[source] = 1
    
    # Créer un graphique à partir des données
    plt.figure(figsize=(10, 6))
    plt.bar(sources.keys(), sources.values(), color='skyblue')
    plt.xlabel('Source de Candidature')
    plt.ylabel('Nombre de Candidats')
    plt.title('Nombre de Candidats par Source de Candidature')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Créer la barre de menu
def creer_menu(root):
    menu_bar = tk.Menu(root)
    
    menu_candidats = tk.Menu(menu_bar, tearoff=0)
    menu_candidats.add_command(label="Voir les Candidats", command=voir_candidats)
    menu_candidats.add_command(label="Ajouter un Candidat", command=ajouter_candidat)
    menu_bar.add_cascade(label="Candidats", menu=menu_candidats)
    
    menu_offres = tk.Menu(menu_bar, tearoff=0)
    menu_offres.add_command(label="Voir les Offres d'Emploi", command=voir_offres)
    menu_offres.add_command(label="Ajouter une Offre d'Emploi", command=ajouter_offre)
    menu_bar.add_cascade(label="Offres d'Emploi", menu=menu_offres)
    
    menu_stats = tk.Menu(menu_bar, tearoff=0)
    menu_stats.add_command(label="Statistiques de Recrutement", command=statistiques_recrutement)
    menu_stats.add_command(label="Graphique des Candidats", command=afficher_graphique)
    menu_bar.add_cascade(label="Statistiques", menu=menu_stats)
    
    menu_suivi = tk.Menu(menu_bar, tearoff=0)
    menu_suivi.add_command(label="Suivi des Candidatures", command=suivi_candidatures)
    menu_bar.add_cascade(label="Suivi", menu=menu_suivi)
    
    root.config(menu=menu_bar)

# Configuration de la fenêtre principale
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Application de Gestion de Recrutement")
    root.geometry("600x400")

  # Charger l'image d'arrière-plan
    image_fond = tk.PhotoImage(file="image.png")  # Mettez ici le chemin de votre image
    canvas = tk.Canvas(root, width=600, height=400)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, anchor="nw", image=image_fond)
    
    charger_candidats_depuis_csv()
    charger_offres_depuis_csv()
    
    creer_menu(root)
    
    root.mainloop()
