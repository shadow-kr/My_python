import random
import numpy as np

x = np.random.rand(3,2)
print(x)



#la transposé
x= x.T
print('la transposé:\n',x)

#X = X[:,0] c'est :=toutes les ligne et 0=la premiere colonne alors X[:,0]--> tout les ligne de la premiere colonne
x = x[:,0]
print('new x:\n',x)