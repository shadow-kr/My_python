#utiliser l'algo svm

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
style.use("ggplot")#le style du graph
from sklearn import svm#c'est notre algo

'''
x = [1, 5, 1.5, 8, 1, 9]
y = [2, 8, 1.8, 8, 0.6, 11]

plt.scatter(x,y)#on dessine x et y
plt.show()
'''

X = np.array([[1,2],[5,8],[1.5,1.8],[8,8],[1,0.6],[9,11]])
y =  [0,1,0,1,0,1]

#==============================================svm===============================
clf = svm.SVC(kernel='linear', C = 1.0)# C is a valuation of "how badly" you want to properly classify
clf.fit(X,y)
print(clf.predict([[10.58,10.76]]))
#==============================================svm===============================


#pour dessiner la ligne du svm dans le graphe
w = clf.coef_[0]
print(w)

#pour la mettre dans le graph
a = -w[0] / w[1]

xx = np.linspace(0,12)
yy = a * xx - clf.intercept_[0] / w[1]

h0 = plt.plot(xx, yy, 'k-', label="non weighted div")#k est la couleur noir 

#pour mettre les autres élement 
plt.scatter(X[:, 0], X[:, 1], c = y) #c=y est la couleur
plt.legend()
plt.show()