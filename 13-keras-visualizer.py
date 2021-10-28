from keras import models  
from keras.layers import Dense, Conv2D, MaxPooling2D, Flatten, Activation  
from keras import layers 

 




model1 = models.Sequential()  
model1.add(Dense(16, input_shape=(784,)))
model1.add(Dense(8))
model1.add(Dense(4))
print(model1.summary()) 
from tensorflow.keras.utils import plot_model

#pour tracer soit utiliser plot_model 
#plot_model(model1, to_file='model_vertical.png', show_shapes=True)
#plot_model(model1, to_file='model_horizontal.png', rankdir='LR', show_shapes=True)


from keras_visualizer import visualizer

#ou utiliser visulize
#NB: il faut installer depuis anaconda conda install python-graphviz
visualizer(model1, filename='graph', format="png", view=False)


print("SVP aller au dossier de ce code! ")