from mfccConverter import newArray
from mfccConverter import yData
from sklearn.model_selection import train_test_split
from keras.utils import to_categorical
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense, Conv2D, Flatten, MaxPooling2D
from keras import layers

#download mnist data and split into train and test sets

# (X_train, y_train), (X_test, y_test) = mnist.load_data()

X = newArray
X = np.resize(X, (455, 124, 13, 1))
y = yData
y_categorical = to_categorical(y)

print(np.shape(X))
print(X[454])
print(np.shape(y_categorical))

X_train, X_test, y_train, y_test = train_test_split(X, y_categorical, test_size=0.2, shuffle=True)

print(np.shape(X_train))
print(np.shape(X_test))
print(np.shape(y_train))
print(np.shape(y_test))

#create model
model = Sequential()
#add model layers
model.add(Conv2D(32, (2,2), activation='relu', input_shape=(124, 13, 1)))
model.add(MaxPooling2D((2,2)))

model.add(Conv2D(64, (2,2), activation='relu'))
model.add(MaxPooling2D((2,2)))

# model.add(Conv2D(64, (3,3), activation='relu'))

model.add(Flatten())
model.add(Dense(64, activation='relu'))
model.add(Dense(5, activation='softmax'))

#compile model using accuracy to measure model performance
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

#train the model
model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=10)

test_loss, test_acc = model.evaluate(X_test, y_test)

print(test_acc)
