import Livre
import Etudiant
from prettytable import PrettyTable
class Administrateur:
    def __init__(self ,id, nom, prenom, email, login, mdp):
        self.id=id
        self.nom = nom
        self.prenom = prenom
        self.email = email
        self.login = login
        self.mdp = mdp
def ajoutEtudiant():
	file = open("users.txt","a+")
	id_input = input("id: ")
	nom_input = input("nom: ")
	prenom_input = input("prenom: ")
	email_input = input("email: ")
	login_input = input("login: ")
	password_input = input("password: ")
	x = Etudiant(id_input, nom_input, prenom_input, email_input, login_input, password_input)
	print(x.__str__())
	file.write(x.__str__())
	file.close()

def afficheEtudiant():
	file = open("users.txt","r")
	table = PrettyTable(["id","nom","prenom","email","login","password","suspended"])
	for line in file.readlines():
		etudiant=line.strip().split(',')
		table.add_row([etudiant[0], etudiant[1], etudiant[2],etudiant[3], etudiant[4], etudiant[5],etudiant[6]])
	print(table)
	file.close()
