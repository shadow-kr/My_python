#programme qui trie entre posetif et negatif
#dectionaire:
classeur={
        "positif":[]#tableau
        ,"negatif":[]#tableau
        }

#fonction trier:
def trier (classeur,nombre):
    if nombre>=0:
        classeur["positif"].append(nombre)#ajouter à la liste
    else:
        classeur["negatif"].append(nombre)
            
    return classeur
trier(classeur,3)
trier(classeur,-4)

d=trier(classeur,10)

print(d)

#remarque pour les dictionnaire
#les dictionnaire d'ont pas d'ordre donc pour appeler un élement il faut appeler key exemple
dic={"pos":(1,2,4),"nega":-3}
x=dic["pos"]
print(x)