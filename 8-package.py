#paquage est un ensemble de module organiser:

#=========================
#Math. clic sur tab et tu verra tous les fonctionpossible
#=========================
import math
x=3
print(math.pi)
print(math.cos(x))
print(math.exp(x))
print("==========================")
#=========================
#statistic. clic sur tab et tu verra tous les fonctionpossible
#=========================
import statistics
liste=[2,44,6,77,0]
print(statistics.mean(liste)) #mean donne la moyenne
print(statistics.variance(liste))

#=========================
#Random. clic sur tab et tu verra tous les fonctionpossible
#=========================
print("==========================")
import random
print(random.choice(liste)) #retourne un element aleatoir de la liste
#random.seed(0) #seed permet de fixer la valeur aleatoir retourner
print(random.random())#génere un float aleatoir
print(random.randint(5,10))#retourne des entier aleratoir entre 5 et 10
print(random.randrange(40))#retourne  aleratoir entre 0 et 40
print(random.sample(range(30),5))# crée une liste de 5 element dont tous est entre 0et 30
print(random.sample(range(30),random.randrange(6)))#ici le nb d'elemnt sera aléatoir de 0 à 6

print(liste)  
random.shuffle(liste)#suffle permet de mélanger les élement de la liste
print(liste)
print("==========================")
#=========================
#os. operating systeme clic sur tab et tu verra tous les fonctionpossible
#=========================
import os
print(os.getcwd())# module retourne l'adresse de ce projet 

#=========================
#glob. operating systeme clic sur tab et tu verra tous les fonctionpossible
#=========================
import glob
print(glob.glob("*"))#le module glob retourne tous les fichier existant dans le dossier avec ce projet
# etoile *=all
print('*                end of glob                              *')
print(glob.glob("*.txt"))#retourne les fichier .txt 

print("\t programme qui lit tous les fichier txt: ")
filefound=glob.glob("*.txt")#on cherche les fichier txt
for fichier in filefound: #on entre dans tous les fichier donner pare filefound
    with open(fichier,'r') as f: #on ouvre tous ces fichier et on lit leur contenus
        print(f.read())