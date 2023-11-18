class Etudiant:
	def __init__(self,id, nom, prenom, email, login ,password,suspended=False):
		self.id = id
		self.nom = nom
		self.prenom = prenom
		self.email = email
		self.login = login
		self.password = password
		self.suspended = suspended
	def __str__(self):
		return f"{self.id},{self.nom},{self.prenom},{self.email},{self.login},{self.password},{self.suspended} \n"
