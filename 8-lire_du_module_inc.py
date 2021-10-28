#le module est la fonction qu'on appele depuis un autre fichier


k=4

import inc #on appele le fichier inc
r= inc.increment(k) #depuis le fichier inc on appel la fonction incrementer
print("fonction incrementer:",r)

#=========================
#autre methode
import inc as fichier #as permet de donner un nouveau nom au fichier source
p=fichier.diminuer(k)
print("fonction diminuer:",p)

#==========================
#declarer la fonction directement
from inc import puissance
j=puissance(k) # on peut utiliser la fonction directement car on la declarer
print("fonction puissance:",j)

#========================
#on peut appler tous les fonctions du fichier avec:
from inc import * #* veut dire all
m=2
z=diminuer(m)
print(z)
