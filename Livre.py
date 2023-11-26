from datetime import datetime, timedelta
from prettytable import PrettyTable

def afficheLivre():
	file = open("livres.txt","r")
	table = PrettyTable(["id","Titre","Auteur","Éditeur","ISBN","Nombre d'exemplaires","Année"])
	for line in file.readlines():
		livre=line.strip().split(',')
		table.add_row([livre[0], livre[1], livre[2],livre[3], livre[4], livre[5],livre[6]])
	print(table)
	file.close()
     
def livreDisponible(id_livre):
    # Vérifiez si le livre est disponible en vérifiant s'il a déjà été emprunté
    with open("emprunts.txt", "r") as fichier:
        for ligne in fichier:
            enregistrement = ligne.strip().split(',')
            if enregistrement[1] == id_livre:
                # Le livre a déjà été emprunté
                return False
    # Le livre n'a pas été emprunté, il est disponible
    return True
def peutEmprunterPlusDeLivres(id_etudiant):
    # Vérifiez si l'étudiant a déjà emprunté trois livres
    livres_empruntes = 0
    with open("emprunts.txt", "r") as fichier:
        for ligne in fichier:
            enregistrement = ligne.strip().split(',')
            if enregistrement[0] == id_etudiant:
                livres_empruntes += 1
    return livres_empruntes < 3

def empruntLivre(id_etudiant):
    creerfichier=open("emprunts.txt", "a+")
    creerfichier.close()
    id_livre = input("Entrez l'identifiant du livre : ")
    date_emprunt = datetime.now().strftime("%Y-%m-%d")

    # Vérifiez si l'étudiant a déjà emprunté trois livres
    if not peutEmprunterPlusDeLivres(id_etudiant):
        print("Vous avez atteint la limite maximale d'emprunts (3 livres).")
        return

    # Vérifiez si le livre est disponible pour l'emprunt
    if livreDisponible(id_livre):
        # Ajoutez l'enregistrement d'emprunt au fichier
        enregistrement_emprunt = f"{id_etudiant},{id_livre},{date_emprunt}\n"
        with open("emprunts.txt", "a") as fichier:
            fichier.write(enregistrement_emprunt)
        print("Livre emprunté avec succès !")
    else:
        print("Le livre n'est pas disponible pour l'emprunt.")



