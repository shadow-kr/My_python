#le dictionnaire n'est pas une sequence il'ny'a pas d'ordre de son contenus
dictionaire = { "swords":"epée" , "sheilds":"bouclier" , "arrows":"fléche"}

equipment={"swords":200 ,"sheilds":120 ,"arrows":300 }

traduction ={"dics":dictionaire,"equi":equipment  }
 
#afficher les motcles:
k= equipment.keys()
print(k)

#afficher le contenus des motcles:
v= equipment.values()
print(v)

#taille du dictionnaire
l=len(equipment)
print(l)

#ajouter un element à la liste:
equipment["potions"]=20

#pour voir si food existe dans le dictionnaire si non retourne none
print(equipment.get("food"))
print(equipment.get("food","lol_nop"))# retoune lol_nop à la place de none
print(equipment.get("sheilds"))

#ajouter une liste au dictionnaire
liste_1={"fire rod","ice rod","thunder rod" }
equipment.fromkeys(liste_1, 3)

print(equipment)
#vider le contenus d'une key

a=equipment.pop("arrows")#on supprime arrows mais son contenu sera garder mais invisible
print(equipment)
print(a)# a contien la valeur de la key supprimé

#boucle afficher tous le dictionnaire on utilise items
for e,f in equipment.items():
    print(e,f)#e c'est les keys et f c'est les valeurs
