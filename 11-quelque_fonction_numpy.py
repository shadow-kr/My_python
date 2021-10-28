import numpy as np 
 
#np.empty permet de creer un array de dimention
x = np.empty((3, 2)) 
print(x)

print('===============================================================')
#np.hstack permet de rassembler deux array exp 
a = np.array((1,2,3))
b = np.array((2,3,4))
k=np.hstack([a,b])

print(a)
print(b)
print('np.hstack:',k)
print('===============================================================')
#np.hstack permet de rassembler deux array exp 

a = np.array([[1],[2],[3]])
b = np.array([[2],[3],[4]])
k=np.hstack((a,b))

print(a)
print(b)
print('np.hstack:\n',k)


print('===============================================================')
#np.vstack stoque les données de facons verticale
a = np.array([1, 2, 3])
b = np.array([2, 3, 4])
k=np.vstack((a,b))
print('np.vstack:\n',k)

print('===============================================================')
#np.expand_dims permet etendre la taille(the shape) of an array.
x = np.array([1, 2])
print(x)
print('shape:',x.shape)#une ligne deux colonne
y = np.expand_dims(x, axis=1)#axe precise d'ou extendre asis =0 -->hori et esis = 1 -->ver
print('np.expand_dims:\n',y)
print('shape:',y.shape)##deux ligne une colonne