import Etudiant
import Administrateur as Admin
MenuChoix = input("""Saisissez votre choix 1/2 \n
                  1_ Login en tant qu'administrateur
                  2_ Login en tant qu'étudiant\n""")

match MenuChoix:
    case '1':
        Admin.AdminMain()
    case '2':
        Etudiant.EtudiantMain()
    case _:
        print("Choix introuvable ...")

