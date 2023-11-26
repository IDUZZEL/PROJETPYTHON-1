from prettytable import PrettyTable
import Livre
Menu ='''
1_ajoute un etudiant 
2_afficher la liste des etudiant avec leur infos
3_suspendre un compte d'etudiant
4_active un compte d'etudiant
5_ajoute un livre 
6_supprime un livre
7_affiche la liste des etudiant qui depasse leur periode
0_exit
'''
def getNextID(file):
    with open(file, "r") as file:
        lines = file.readlines()
        if lines:
            last_line = lines[-1].strip().split(',')
            last_id = int(last_line[0])
            return last_id + 1
        else:
            return 1
def ajoutEtudiant():
    with open("etudiants.txt", "a+") as file:
        id_input = str(getNextID("etudiants.txt"))
        nom_input = input("nom: ")
        prenom_input = input("prenom: ")
        email_input = input("email: ")
        login_input = input("login: ")
        password_input = input("password: ")
        new_student = f"{id_input},{nom_input},{prenom_input},{email_input},{login_input},{password_input},False\n"
        file.write(new_student)
        print("Student added successfully!")

def afficheEtudiant():
	file = open("etudiants.txt","r")
	table = PrettyTable(["id","nom","prenom","email","login","password","suspended"])
	for line in file.readlines():
		etudiant=line.strip().split(',')
		table.add_row([etudiant[0], etudiant[1], etudiant[2],etudiant[3], etudiant[4], etudiant[5],etudiant[6]])
	print(table)
	file.close()

def AdminLogin(Login, Pass):
    with open("admins.txt", "r") as file:
        for line in file.readlines():
            admin = line.strip().split(',')
            if Login == admin[0] and Pass == admin[1]:
                return True
    return False

#fonction pour desactive un compte
def suspendAccount(student_id):
    with open("etudiants.txt", "r") as file:
        lines = file.readlines()
    with open("etudiants.txt", "w") as file:
        for line in lines:
            student_info = line.strip().split(',')
            if student_info[0] == student_id:
                student_info[6] = 'True'  # Assuming 'suspended' is at index 6 in your format
                line = ','.join(student_info) + '\n'
            file.write(line)
            
def ativateAccount(student_id):
    with open("etudiants.txt", "r") as file:
        lines = file.readlines()
    with open("etudiants.txt", "w") as file:
        for line in lines:
            student_info = line.strip().split(',')
            if student_info[0] == student_id:
                student_info[6] = 'False'  
                line = ','.join(student_info) + '\n'
            file.write(line)
    return True


def ajouterLivre():
    with open("livres.txt", "a+") as file:
        id_input = getNextID("livres.txt")
        titre_input = input("Titre: ")
        auteur_input = input("Auteur: ")
        editeur_input = input("Éditeur: ")
        isbn_input = input("ISBN: ")
        nb_exemplaires_input = input("Nombre d'exemplaires: ")
        annee_input = input("Année: ")
        livre = f"{id_input},{titre_input},{auteur_input},{editeur_input},{isbn_input},{nb_exemplaires_input},{annee_input}\n"
        file.write(livre)
        print("Livre ajouté avec succès!")

def supprimerLivre(id_livre):
    deleted=False
    with open("livres.txt", "r") as file:
        lines = file.readlines()
    with open("temp.txt", "w") as file2:
        for line in lines:
            livre_info = line.strip().split(',')
            if livre_info[0] == id_livre:
                deleted=True
            else:
                file2.write(line)
        if deleted:
            print(f"Livre avec l'ID {id_livre} supprimé avec succès!")
        else:
            print(f"Aucun livre avec l'ID {id_livre} n'a été trouvé.")
    file.close()
    file2.close()

def AdminMain():
    loggedIn = False
    while not loggedIn:
        Login = input("Enter your login: ")
        Pass = input("Enter your password: ")
        loggedIn = AdminLogin(Login, Pass)
        if loggedIn:
            print("Login successful!")
            exit=0
            while(exit !=1):
                 choix = input(Menu)
                 if choix == '1':
                      ajoutEtudiant()
                 elif choix == '2':
                      afficheEtudiant()
                 elif choix == '3':
                      student_id=input("saisie Le ID d'etudiant: ")
                      suspendAccount(student_id)
                      afficheEtudiant()
                 elif choix == '4':
                      student_id=input("saisie Le ID d'etudiant: ")
                      ativateAccount(student_id)
                      afficheEtudiant()
                 elif choix =='5':
                    ajouterLivre()
                    Livre.afficheLivre()
                 elif choix =='6':
                    id_livre=input("write the id of the book")
                    supprimerLivre(id_livre)
                    Livre.afficheLivre()
                 elif choix =='0':
                     exit=1
                 else:
                      print("Choix introuvable ...")
        else:
            print("Incorrect login or password. Please try again.")

