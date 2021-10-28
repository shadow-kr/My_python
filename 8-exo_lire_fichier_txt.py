#programme qui lit tous les fichier txt est nous les donne sous forme de dictionnaire 
#le dictionnaire est comme ca key: elment
import glob

# * est egale à tous les variable
filename= glob.glob("*.txt")#le module glob retourne tous les fichier txt existant dans le dossier avec ce projet
d={}#d est un dictionnaire vide
for file in filename:#on entre dans tous les fichier donner par filefound
    with open(file,'r')as f:#on ouvre tous ces fichier et on met leurs contenus dans f
        d[file]=f.read().splitlines()# file = nomdu fichier ,f= le contenus
        #splitlines permet de retourner à la ligne apres chaque ligne

print(d)