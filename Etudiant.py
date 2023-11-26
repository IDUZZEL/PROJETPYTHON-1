import Livre
def EtudiantLogin(Login, Pass):
    with open("etudiants.txt", "r") as file:
        for line in file.readlines():
            etudiant = line.strip().split(',')
            if Login == etudiant[4] and Pass == etudiant[5]:
                if etudiant[6] =="True":
                    print("Votre compte est suspendu. Veuillez contacter l'administrateur.")
                    return False, None ,None
                return True, etudiant[0],etudiant[2]  # Returning True and the ID if and name
            
    return False, None ,None # Returning False and None if login fails



     
def EtudiantMain():
    loggedIn = False
    student_id = None
    student_name = None
    while not loggedIn:
        Login = input("Entrez votre login : ")
        Pass = input("Entrez votre mot de passe : ")
        loggedIn, student_id, student_name= EtudiantLogin(Login, Pass)
        if loggedIn:
            print(f"Login successful! \n Bonjour Mr/Mme {student_name} \n vous pouvez ecrire id du livre que vous souhaite empriente")
            Livre.afficheLivre()
            Livre.empruntLivre(student_id)
