#Programation oriontÃ© objet:
#ndim=dimention:
#1D=Ligne
#2D=Ligne,colonne
#3D=Ligne,colonne,diago

# class qui cree des tableau la class numpy.nd array
import numpy as np #on importe la classe numpy pour creer un tableau

#constructeur de la class numpy--> np._______ :
#array, zeros,ones,full,random,eye,arange,linspace




tab= np.array([2,3,5]) #array est le constructeur de la classe numpy 
 #dans array l'objet est un tableau [ ]
print(tab.size)#size est un attribut (fonction de la classe)
print(tab.ndim)#ndim donne le nb de dimention ici on a un tableau a ligne seulement donc dim=1
print(tab.shape)#shaper retourne le nb d'element dans chaque dimention (3,) on a 3 élemnt dans la 1ere dimention
print(tab)
print("================1===================")

z=np.zeros((3,2))# zeros return un tableau remplis de zero ici matrice 3ligne , 2colonne
print(z) 
print(type(z.shape))#shape est un tuple on peut donc retourner les elment qu'on veut
print("================2===================")

o=np.ones((2,3))# one return un tableau remplis de 1 ici matrice 2ligne , 3colonne
print(o) 
print(o.size)#size= ligne*colonne =2*3
print("================3===================")

f=np.full((4,4),10)# full return un tableau remplis de la valeur voulus ici 10
print(f) 
print("================4===================")

r=np.random.randn(3,3)#random est un construceteur et rand est un module du constructeur
np.random.seed(0)#la fonction seed permet de garder les nombre randome trouver dans le 1er essaie
print(r)
print("================5===================")

identite=np.eye(3,3)#on peut ecrire eye(3) donc 3 uns dans la matrice
print(identite)
print("================6===================")

a=np.arange(0,6,²1) #arange:cree un tableau ici de 0 à 5 de 1 pas 
print(a)
l=np.linspace(0,6,10)#linspace:cree un tableau ici de 0 à 6 avec 10 élement 
print(l)
print("================7===================")

d=np.linspace(0,6,10,dtype=np.float16)# dtype= permet de controler le type de variable elle est utilisable avec tous les constructeurs
print(d)

print("==========Manipulation des tableau ==========")
a=np.zeros((3,3))
b=np.ones((3,3))
h=np.hstack((a,b))#hstack permet de fusionner deux matrice horizontalment
#autre methode h=np.concatenation((a,b),axis=1)
print(h)
print("================8===================")
v=np.vstack((a,b))#vstack fusion vertical
#autre methode v=np.concatenation((a,b),axis=0)
print(v)
print(v.shape)
print("================9===================")
v=v.reshape((3,6))
print(v)

print("================10===================")
y=np.array([3,4,5])
print(y.shape)#retourne (3,)= (3 elemnt de la 1ere dimention,) on peut la rendre (3,1) avec reshape lol didn't work
#y=y.squeeze()      squeeze permet de supprimer le 1 dans shaper--> (3,1) est la rendre (3,)
print("================11===================")
g=np.full((3,3),4)
print(g)
g=g.ravel()#ravel permet d'applatir une matrice  
print(g)

