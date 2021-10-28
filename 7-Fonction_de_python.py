#Fonction de phyton:
x=-3.14
print(x)
print(type(x))#retourne le type de la variable
print(abs(x))#valeur absolues
print(round(x))#retourn que le nb apres virgule

print("===============1===================")

list_1=[1,34,44,-55]
print(max(list_1))#retourne max
print(min(list_1))#retourne min
print(len(list_1))#retourne longeur
print(sum(list_1))#retourne somme des element de la liste

print("================2==================\n")
liste_2=[True,True,False]
print(all(liste_2)) #retourne true que si tous est true 
print(any(liste_2))#retourne true si aumois un element est tru

print("================3==================")
#fonction de conversion:
dicti={"hp":300,"mp":400}
k=10
print(bin(k))#k conversion binnaire
print(oct(k))#k conversion octadicima
print(hex(k))#k conversion hexadicimal

print("================4==================")

print(str(k))# k devient un string
print(int(k))#k devient int 
print(float(k))#k devient float
print(tuple(list_1))#transforme une liste à un tuple
print(list(dicti.keys()))#on a transformer les mot cles du dic en liste
print("================5==================")

r=input("veuiller ecrire ici: ")#permet d'ecrire
print(type(r)) #input retourne un string, pour utiliser r il faut la transformer en int 

print("================6==================")

j=int(input("veuiller entrer un entier ici: "))#permet d'ecrire un nombre int
print(type(j))#input retourne un nombre int

print("================7==================")

# pour utiliser des variables in faut utiliser la fonction .format( les variable utilisé)
message_1=" hello my name is {} my age is {} ".format(r, j) # les {} sont les variables utilisé
print(message_1)
print("-----version 2-------")
#pour on utilise f avec le stringe {variable }
message_2= f"salut mon nom est {r} et mon age est {j}"
print(message_2)

