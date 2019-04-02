import csv
import types
from tkinter import *


def creer_liste_csv(nom_fichier, champs): #Lis le csv et retourne un dictionnaire
	tentatives = {}
	for champ in champs:
		tentatives[champ] = []
	with open(nom_fichier) as fichier:
		reader = csv.DictReader(fichier)
		for line in reader:
			for champ in champs:
				tentatives[champ].append(line[champ])
	return tentatives;


def creer_liste_champ_unique(my_dict, champ):			#retourne une liste d'un champ spécifique du dictionnaire
	liste = []
	for line in my_dict[champ]:
		if(line not in liste):
			liste.append(line)
	return liste;


#Les Groupes
#Question 1
def etudiants_par_groupe():		#retourne une liste au format [ ["Groupe1", "Nombre d'étudiants"], ["Groupe2", "Nombre d'étudiants"], ...]
	my_dict = creer_liste_csv('essais.csv', ["ETUDIANT", "GROUPE"])		
	etudiants = []						#cette liste permet de ne pas enregistrer 2 fois un étudiant
	groupes = []

	for groupe in creer_liste_champ_unique(my_dict, 'GROUPE'):
		groupes.append([groupe])

	for i in range(len(my_dict['ETUDIANT'])):
		if(my_dict['ETUDIANT'][i] not in etudiants):
			etudiants.append(my_dict['ETUDIANT'][i])
			for groupe in groupes:
				if groupe[0] == my_dict['GROUPE'][i]:
					groupe.append(my_dict['ETUDIANT'])
	return groupes;

	
#Question 2			#retourne une liste au format [ ["Groupe1", "Nombre d'essais"], ["Groupe2", "Nombre d'essais"], ...]
def conteur_essais_groupe():
	my_dict = creer_liste_csv('essais.csv', ["GROUPE"])	
	groupes = []
	for i in creer_liste_champ_unique(my_dict, 'GROUPE'):
		groupes.append([i,0])
	for line in my_dict["GROUPE"]:
		for groupe in groupes:
			if groupe[0] == line:
				groupe[1] = groupe[1] + 1;
	return groupes;



#Question 3				
def groupe_tentatives_max():		#retoure les 3 groupes ayant réalisés le plus d'essais avec le nombre d'essais	
	max = [0, 0, 0]
	groupeMax = [-1, -1, -1]
	groupes = conteur_essais_groupe()
	for groupe in groupes:
		index_max_a_changer = max.index(min(max))
		if int(groupe[1]) > int(max[index_max_a_changer]):
			max[index_max_a_changer] = groupe[1]
			groupeMax[index_max_a_changer] = groupe[0]
	return max[0], groupeMax[0], max[1], groupeMax[1], max[2], groupeMax[2]
	


#Les Etudiants
def conteur_essais_etudiant():			#retourne une liste au format [ ["Groupe1", ["Etudiant 1", "Nombres d'essais"] ], ["Groupe1", ["Etudiant 2", "Nombres d'essais"] ], ...]
	my_dict = creer_liste_csv('essais.csv', ["GROUPE", "ETUDIANT"])
	etudiants = []
	groupes = []
	for groupe in creer_liste_champ_unique(my_dict, 'GROUPE'):
		groupes.append([groupe])

	for i in range(len(my_dict['ETUDIANT'])):
		if(my_dict['ETUDIANT'][i] not in etudiants):
			etudiants.append(my_dict['ETUDIANT'][i])
			for groupe in groupes:
				if groupe[0] == my_dict['GROUPE'][i]:
					groupe.append([my_dict['ETUDIANT'][i],0])

	for i in range(len(my_dict['ETUDIANT'])):
		for groupe in groupes:
			for etudiant in groupe:
				if etudiant[0] == my_dict['ETUDIANT'][i]:
					etudiant[1] = etudiant[1] + 1;
	return groupes;


def moyenne_essais():		#retourne la moyenne du nombre d'essais par etudiant
	groupes = conteur_essais_etudiant()
	diviseur = 0
	count = 0
	for groupe in groupes:
		for etudiant in groupe:
			if isinstance(etudiant, list):
				count = count + etudiant[1]
				diviseur = diviseur + 1
	count = count / diviseur
	return count


def moyenne_essais_par_groupe():		#retourne la moyenne du nombre d'essais par groupe et par etudiant
	groupes = conteur_essais_etudiant()
	diviseur = -1
	count = 0
	total = 0
	nb_etudiants = 0
	for groupe in groupes:
		for etudiant in groupe:
			if isinstance(etudiant, list):
				count = count + etudiant[1]
				nb_etudiants = nb_etudiants + 1
			
			elif nb_etudiants > 0:	
				diviseur = diviseur + 1
				total = total + (count / nb_etudiants)
				print()
				print("Groupe ", nom_groupe, " : ", count / nb_etudiants, " essais par étudiant")
				nb_etudiants = 0
				count = 0
				nom_groupe = etudiant
			else:
				nom_groupe = etudiant

	diviseur = diviseur + 1
	total = (total + count) / diviseur
	return total


#Les Exercices
#Les Echecs
#Exercice 1
def tentatives_par_groupe():		#retourne une liste contenant chaque groupe associé aux exercices effectués par ce groupe
					#format [ ["Groupe1", "Exercice 1", "Exercice 2"], ["Groupe2", "Exercice 1", "Exercice 3"], ...]
	my_dict = creer_liste_csv('essais.csv', ["GROUPE", "EXO"])
	groupes = []
	for i in creer_liste_champ_unique(my_dict, 'GROUPE'):
		groupes.append([i,[]])
	for i in range(len(my_dict['EXO'])):
		for groupe in groupes:
			if(my_dict['EXO'][i] not in groupe[1]):
				groupe[1].append(my_dict['EXO'][i])

	return groupes


#Exercice 2
def tentatives_par_exercice():	#retourne une liste des exercices tentés associé a sa reussite ou non. Format [ ["Exercice 1", 1], ["Exercice 2", 0], ...]
	my_dict = creer_liste_csv('essais.csv', ["EXO", "ERREURS", "ECHECS"])
	exercices = []
	for i in creer_liste_champ_unique(my_dict, 'EXO'):
		exercices.append([i, 0])
	for i in range(len(my_dict['EXO'])):
		if(my_dict['ERREURS'][i] == "0" and my_dict['ECHECS'][i] == "0"):
			for exercice in exercices:
				if(exercice[0] == my_dict['EXO'][i]):
					exercice[1] = exercice[1] + 1
	return exercices


#Les Réussites
#Exercice 1
def moy_temps_reussite():
	my_dict = creer_liste_csv('essais.csv', ["EXO", "ERREURS", "ECHECS", "HORODATEUR"])
	exercices = [["ex1", 2, 1]]
	for i in range(len(my_dict['EXO'])):
		in_list = 0
		for exercice in exercices:
			if(exercice[0] == my_dict['EXO'][i]):
				in_list = 1
				exercice[1] = "ok"
			if(in_list == 0):
				exercices.append([my_dict['EXO'][i], -1, -1])
	return exercices


#Interface
class Interface(Frame):
    
	"""Notre fenêtre principale.
	Tous les widgets sont stockés comme attributs de cette fenêtre."""
	def __init__(self, fenetre, **kwargs):
		Frame.__init__(self, fenetre, width=768, height=576, **kwargs)
		self.pack(fill=BOTH)
		self.nb_clic = 0

		# Création des widgets
		self.message = Label(self, text="Choisissez les données à afficher")
		self.message.pack(side="right")

		#Les Groupes
		#Question 1
		self.bouton_1 = Button(self, text="Nombre d'étudiants par groupe", fg="red", command=self.groupes1)
		self.bouton_1.pack()

		#Question 2
		self.bouton_2 = Button(self, text="Nombre d'essais par groupe", fg="red", command=self.groupes2)
		self.bouton_2.pack()

		#Question 3
		self.bouton_3 = Button(self, text="Groupe ayant réalisé le plus d'essais", fg="red", command=self.groupes3)
		self.bouton_3.pack()
		
		#Les Etudiants
		self.bouton_4 = Button(self, text="Nombre d'essais des étudiants", fg="red", command=self.etudiants1)
		self.bouton_4.pack()

		self.bouton_5 = Button(self, text="Moyenne d'essais par étudiant", fg="red", command=self.etudiants2)
		self.bouton_5.pack()

		self.bouton_6 = Button(self, text="Moyenne d'essais par groupe", fg="red", command=self.etudiants3)
		self.bouton_6.pack()

		#Les Exercices
		#Les Echecs
		#Exercice 1
		self.bouton_7 = Button(self, text="Exercices tentés par chaque groupe", fg="red", command=self.echecs1)
		self.bouton_7.pack()

		#Exercice 2
		self.bouton_8 = Button(self, text="Exercices tentés mais pas réussis par chaque groupe", fg="red", command=self.echecs2)
		self.bouton_8.pack()


		#Les Réussites
		#Exercice 1
		self.bouton_9 = Button(self, text="Temps par exercice entre la première tentative et la réussite", fg="red", command=self.reussites1)
		self.bouton_9.pack()

		#Exercice 2
		self.bouton_10 = Button(self, text="Exercices les mieux réussis", fg="red", command=self.reussites2)
		self.bouton_10.pack()

		#Exercice 3
		self.bouton_11 = Button(self, text="Etudiants ayant réussi des exercices en un seul essai", fg="red", command=self.reussites3)
		self.bouton_11.pack()


		
	#Fonctions d'affichage

	#Les Groupes
	#Question 1
	def groupes1(self):
		string = ""
		groupes = etudiants_par_groupe()
		for groupe in groupes:
			count = -1
			for etudiant in groupe:
				count = count + 1;
			string = string + "\nGroupe {} : {} étudiants".format(groupe[0], count)
		print(string)
		self.message["text"] = string

	
	#Question 2		
	def groupes2(self):		#fonction d'affichage
		string = ""
		groupes = conteur_essais_groupe()
		for groupe in groupes:
			string = string + "\nGroupe {} : {} essais".format(groupe[0], groupe[1])
		print(string)
		self.message["text"] = string


	#Question 3				A SIMPLIFIER ET MODIFIER!!
	def groupes3(self):
		max1, groupeMax1, max2, groupeMax2, max3, groupeMax3 = groupe_tentatives_max()
		string = "\nPlus grand nombre de tentatives : \n{} pour le groupe {}\n{} pour le groupe {}\n{} pour le groupe {}\n".format(max1, groupeMax1,max2, groupeMax2,max3, groupeMax3)
		self.message["text"] = string


	#Les Etudiants
	def etudiants1(self):		#affiche proprement la liste créée par conteur_essais_etudiant()
		string = ""
		groupes = conteur_essais_etudiant()
		count = 0
		for groupe in groupes:
			for etudiant in groupe:
				if isinstance(etudiant, list):
					string = string + "\nEtudiant {} : {} essais".format(etudiant[0], etudiant[1])
					print("Etudiant ", etudiant[0], " : ", etudiant[1], "essais")
					count = count + etudiant[1]
			
				else:
					string = string + "Total : {} essais\n\n".format(count)
					print("Total : ", count, " essais")
					print()
					string = string + "Groupe {}".format(etudiant)
					print("Groupe ", etudiant)
					count = 0
		string = string + "Total : {} essais\n\n".format(count)
		print("Total : ", count, " essais")
		#self.message["text"] = string

	#Question 1	
	def etudiants2(self):
		print()
		print("Moyenne de ", moyenne_essais(), " essais par étudiant")

	#Question 2	
	def etudiants3(self):
		print()
		print("\nMoyenne de ", moyenne_essais_par_groupe(), " essais par groupe et par étudiant")


	#Les Exercices
	#Les Echecs
	#Exercice 1
	def echecs1(self):
		print("Loading, please wait")
		groupes = tentatives_par_groupe()
		for groupe in groupes:
			print("Groupe ", groupe[0], " : ")
			for exercice in groupe[1]:
				print(exercice)

	#Exercice 2
	def echecs2(self):
		exercices = tentatives_par_exercice()
		cas_aucun = 0
		for exercice in exercices:
			if(exercice[1] == 0):
				print("Aucun succes pour l'exercice ", exercice[0])
				cas_aucun = 1
		if(cas_aucun == 0):
			print("Tous les exercices qui ont étés tentés ont étés réussis au moins une fois")


	#Les Reussites
	#Exercice 1

	def reussites1(self):
		exercices = moy_temps_reussite()
		print(exercices)

	def reussites2(self):
		exercices = tentatives_par_exercice()

	def reussites3(self):
		exercices = tentatives_par_exercice()


fenetre = Tk()
interface = Interface(fenetre)

interface.mainloop()
interface.destroy()

