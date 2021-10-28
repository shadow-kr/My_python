#module os

import os


directory = "C:/Users/Toshiba/Pictures/python_tester"

#-->system permet d'executer n'importe quel fichier
os.system("C:/Users/Toshiba/Pictures/python_tester/travler.mp4")

#-->getcwd retourne le dossier ou se trouve ce code
print(os.getcwd())

#-->listdir retourne une liste contenant élements existant 
lst = os.listdir(directory)
print(lst)

#-->mkdir permet de créer un dossier
#os.mkdir("nom du nouveau dossier")

#-->pour trier
#lst.sort() #ou sorted(os.listdir(whatever_directory))

#-->renomer
#os.rename("ancien_fichier.txt","nouveau_nom.txt")

#-->remove permet de suppr le fichier demandé
#os.remove("nom_du_fichier_à_suppr")

#-->rmdirsupprimer un dossier
#os.rmdir('chemin vers le fichier à suppr')

#-->voir si le chemin existe reoutne false ou true
isdir = os.path.isdir("C:/Users/Toshiba/Pictures/python_tester/travler.mp4")
print(isdir)

#-->joindre deux chemin dans le meme chemin
#join = os.path.join('C:/Users/Toshiba/Pictures',"/python_tester/travler.mp4")
#print(join)

#-->changer le chemin du code vers un nouveau chemin 'path'
#os.chdir(path)


#-->__je veux retourner que les fichier png__
#1crrer une liste vide
png_files = [] 

#faire une boucle avec une variable path qui va traverser le chemin donnée
for path in lst:
    #endwith test si le fichier se termine avec .png
    if path.endswith('.png'):
        #si le fichier se termine par .png on l'ajoute çà la liste avec append
        png_files.append(path)
        
print(png_files)
#__end__here__







