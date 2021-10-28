#Liste comprehension plus rapide que normal
# cas normal:

import time #module pour mesurer le temps

start1 =time.time()#mesurer le temps de debut
liste_1=[]
for i in range(10):
    liste_1.append(i+1)
    end1=time.time()#mesurer le temps de fin
print (liste_1)
print(end1-start1)
print("==================================")

start2 =time.time()#mesurer le temps de debut
#cas liste comprehension: 
#on met la boucle dans la liste
liste_2=[i+2 for i in range(10)]#i+2 c'est la valeur initial 0+2=2
end2=time.time()#mesurer le temps de fin
print(liste_2)
print(end2-start2)
print("==================================")

#liste dans list:
liste_3=[[i for i in range(3)]for j in range (3)]#repeter la liste(i) 3 fois avec j
print(liste_3)
print("==================================")

#Disconaire comprehension
smash={"0":"Sora","1":"Leon","2":"2b"}
print(smash)

character=["Sora","Leon","2b"]
dico={k:v for k,v in enumerate(character)}
print(dico)
print(dico.keys())
print(dico.values())

#dictionnaire utulisant une liste
classe=["sword","gunner","mix"]
#zip afficher les elemnt de deux liste en meme temps
smash_classe={classe:character for character,classe in zip(character,classe) }
print(smash_classe)

choice_sword={classe:character for character,classe in zip(character,classe) if classe=="sword" }
print(choice_sword)#affiche que les sword classe

print("==================================")
#tuple comprehension
tuple_1=tuple((i**2 for i in range(4)) )#il faut ajouter tuple sinon erreur
print(tuple_1)


