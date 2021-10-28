import os

directory = "C:/Users/Toshiba/Pictures/python_tester"

#-->listdir retourne une liste contenant élements existant 
lst = os.listdir(directory)
print(lst)

#__je veux retourner que les fichier png__
#1crrer une liste vide
png_files = [] 

#faire une boucle avec une variable path qui va traverser le chemin donnée
for path in lst:
    #endwith test si le fichier se termine avec .png
    if path.endswith('.png'):
        #si le fichier se termine par .png on l'ajoute çà la liste avec append
        png_files.append(path)
        
print(png_files)
#------------------------------------------------------------------
#la methode plus simple est d'utiliser glob
#glob for specifique search
#glob permet de trouver facilement les fichier
import glob
#============glob========
print('\n============glob========')
#glob retourne tous les fichier avec leurs chemin
g = glob.glob('{}/*'.format(directory))
print(g)

#en ajoutant .png tous les fichier png seront retourné
print('\n============png========')
p = glob.glob('{}/*.png'.format(directory))
print(p)