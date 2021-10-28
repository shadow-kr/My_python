#utiliser que matplolib seul donne des erreur pour tracer utiliser matplotlib.pyplot 

import matplotlib.pyplot as plt
#ou  from matplotlib import pyplot as plt


x = list(range(0,10))
y = list(range(-10,0))

plt.plot(x,y)

a = [0,-100,25,67,-323]
b = [0,3,7,3,9]

plt.plot(a,b)
#mettre les deux plotlib donne les deux plot dans le meme graph

#axis permet de choisir le plan a utiliser axis([xstart,xfin , ystart,yfin])
plt.axis([-50,80,2,8])
plt.plot(a,b)

#pour donner des titre :
plt.title('triangle')
plt.xlabel('voici x')
plt.ylabel('voici y')
plt.plot(a,b)

#pour remplacer appelation 
plt.xticks((-40,-20,0,20,40,60,80),('a','c','d','e','f','g','h'))
plt.plot(a,b,color='blue')

#pour tracer dans un histograme 
plt.hist(x)
plt.hist(y)

#pour tracer sous forme de pointier
plt.scatter(x, y)


#============================================hey=============
'''
                      #il y'a 5 methode pour tracer:

#0-If you just want to get one graphic, you can use this way.
plt.plot(x, y)

#======================================
#1 favorite plt.subplot(nb_ligne, nb_colonne, numero_élement)
#ici on a 3 ligne et 2 colonne donc 6 élement
plt.figure(figsize=(20,10))
plt.subplot(3, 2, 1)
plt.plot(x) #1 premier élèment à tracer
plt.tight_layout() 

plt.subplot(3, 2, 2)
plt.plot(x) #2 éme élèment à tracer

plt.tight_layout()#permet de laisser de l'espace entre les graphs



#======================================
#2-This lets you plot one or several figure(s) in the same window. 
#pour un seul graph ax.plot=plt.plot
ax = plt.subplot()
ax.plot(x, y)

#You will plot 4 figures which are named ax1, ax2, ax3 and ax4 each one but on the same window. 

fig1, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
ax1.plot(x1,y1)
ax2.plot(x2,y2)
ax3.plot(x3,y3)
ax4.plot(x4,y4)


#======================================
#3-
one plot:
    
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_title('A single plot')

two plot vertical:
    
fig, axs = plt.subplots(2)
fig.suptitle('Vertically stacked subplots')
axs[0].plot(x, y)
axs[1].plot(x, -y)

two horizontal:
    
fig, (ax1, ax2) = plt.subplots(1, 2)
fig.suptitle('Horizontally stacked subplots')
ax1.plot(x, y)
ax2.plot(x, -y)

4 plots:
    
fig, axs = plt.subplots(2, 2)
axs[0, 0].plot(x, y)
axs[0, 0].set_title('Axis [0, 0]')
axs[0, 1].plot(x, y, 'tab:orange')
axs[0, 1].set_title('Axis [0, 1]')
axs[1, 0].plot(x, -y, 'tab:green')
axs[1, 0].set_title('Axis [1, 0]')
axs[1, 1].plot(x, -y, 'tab:red')
axs[1, 1].set_title('Axis [1, 1]')

for ax in axs.flat:
    ax.set(xlabel='x-label', ylabel='y-label')

# Hide x labels and tick labels for top plots and y ticks for right plots.
for ax in axs.flat:
    ax.label_outer()


#======================================
#4-pour afficher le barre d'echelle:
    
    data = np.arange(100, 0, -1).reshape(10, 10)

fig, ax = plt.subplots()
im=librosa.display.specshow(mel, x_axis='time', sr=sr)

fig.colorbar(im, ax=ca, orientation='horizontal')
fig.colorbar(im, ax=ca)#vertical

5-autre type

y, sr = librosa.load('./example_data/blues.00000.wav')
plt.plot(y);
plt.title('Signal');
plt.xlabel('Time (samples)');
plt.ylabel('Amplitude');



'''



