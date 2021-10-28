#=================================================
#list,tuple,string= Structure de données =Sequence
#=================================================

#list
List_numero=[1,2,3]
List_nom=["jonathan","giorno"]
List_ajouter=["joske"]
List_de_list=[List_numero,List_nom]
List_vide=[]
print(List_de_list[0]) #List_de_list � 2 case: 0=List_numer,1=List_nom
print(List_nom[1])

#utiliser les liste avec les methode:
List_nom.append("jolyne")     #ajoute à la liste
List_nom.insert(1,"joseph")   #ajoute à la liste avec l'emplacement voulu
List_nom.extend(List_ajouter) #ajoute àune liste � notre liste
len(List_nom)                 #done dimention
List_nom.sort()               #trier succecivement alphbetiquement
List_nom.sort(reverse=True)   #trier à l'envers
k=List_nom.count("giorno")    #calcule
print(k)
List_ajouter.clear()         #efface le contenu de la list 

#tuple=list constante qu'on ne peut pas changer
tuple_1=("Part 4","Part 2","Part 1","Part 6","Part 5")

#String##############################################
jojo="johnny Joestar"
print(jojo[0],jojo[1],jojo[7],jojo[8]) #index

print(jojo[0:2:1],jojo[0:9:8]) #slicing

mc="yensid"
print(mc[::-1])#affiche à lenver
###########################################
if "giorno" in List_nom:
    print("yes")
else:
    print("No")
    
print("=================")
#numerote la liste
for index,k in enumerate(List_nom):
    print(index,k)
    
print("=================")
#afficher les elemnt de deux liste en meme temps
for a,b in zip(List_nom,tuple_1):
    print(a,b)
