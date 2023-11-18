from prettytable import PrettyTable  ##(pip install prettytable) la commande pour installer PrettyTable pour afficher les livres dans un tableau


class Livre:
    def __init__(self, id, auteur, titre, editeur, ISBN, nbr_exemplaire): #constructeur
        self.id = int(id)
        self.auteur = auteur
        self.titre = titre
        self.editeur = editeur
        self.ISBN = ISBN
        self.nbr_exemplaire = int(nbr_exemplaire)

    @property
    def __str__(self):  # affichage du livre string method
        return f' {self.id} + {self.auteur} + {self.titre}+{self.editeur} + {self.ISBN} + {self.nbr_exemplaire}'
        #c = Livre(2,'adam','hh','gh',123, 123)
        #print(c.__str__)
        #affichage -> 2 + adam+hh+....

    @classmethod
    def ajouter_un_livre(cls): #demander a l'utilisateur de saisir les informations du livre
        id = int(input('id :'))
        auteur = input('auteur : ')
        titre = input('titre :')
        editeur = input('editeur :')
        ISBN = input('ISBN :')
        nbr_exemplaire = int(input('nbr_exemplaire :'))
        return cls(id, auteur, titre,editeur, ISBN, nbr_exemplaire)

    def affichage_livres(self):
        table = PrettyTable(['id', 'auteur', 'titre', 'editeur', 'ISBN', 'nbr_exemplaire']) #table header
        table.add_row([self.id, self.auteur, self.titre,self.editeur, self.ISBN, self.nbr_exemplaire]) #ajouter les informations du livre
        print(table)


livre = Livre.ajouter_un_livre()

livre.affichage_livres()

