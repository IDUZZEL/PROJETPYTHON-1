def EtudiantLogin(Login, Pass):
    with open("etudiants.txt", "r") as file:
        for line in file.readlines():
            etudiant = line.strip().split(',')
            if Login == etudiant[4] and Pass == etudiant[5]:
                return True, etudiant[0]  # Returning True and the ID if login is successful
    return False, None  # Returning False and None if login fails

def EtudiantMain():
    loggedIn = False
    student_id = None
    while not loggedIn:
        Login = input("Entrez votre login : ")
        Pass = input("Entrez votre mot de passe : ")
        loggedIn, student_id = EtudiantLogin(Login, Pass)
        if loggedIn:
            print(f"Login successful! Student ID: {student_id}")
