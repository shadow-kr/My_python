'''
train_test_split is a function in Sklearn model selection for splitting data arrays into two subsets: for training data and for testing data. 
With this function, you don't need to divide the dataset manually.

By default, Sklearn train_test_split will make random partitions for the two subsets. However, you can also specify a random state for the operation.
'''


import sklearn.model_selection as model_selection






X =  list(range(15))
print (X)

y = [x * x for x in X]
print (y)


X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, train_size=0.65,test_size=0.35, random_state=101)
print ("X_train: ", X_train)
print ("y_train: ", y_train)
print("X_test: ", X_test)
print ("y_test: ", y_test)