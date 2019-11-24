from mfccConverter import newArray
from mfccConverter import yData
from sklearn.model_selection import train_test_split
from keras.utils import to_categorical
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense, Conv2D, Flatten, MaxPooling2D, Dropout
from keras import layers
from imblearn.over_sampling import SMOTE

X = newArray
X = np.resize(X, (len(yData), 124, 13, 1))
y = yData
y_categorical = to_categorical(y)

print(sum(y_categorical))

X_train, X_test, y_train, y_test = train_test_split(X, y_categorical, test_size=0.01, shuffle=True)

# print(np.shape(X_train))
# print(np.shape(X_test))
# print(np.shape(y_train))
# print(np.shape(y_test))

#create model
model = Sequential()
#add model layers
model.add(Conv2D(32, (4,4), activation='relu', input_shape=(124, 13, 1)))
model.add(MaxPooling2D((2,2)))

model.add(Conv2D(64, (4,4), activation='relu'))
model.add(MaxPooling2D((2,2)))

model.add(Flatten())
model.add(Dense(64, activation='relu'))
# model.add(Dropout(0.5))
# model.add(Dense(32, activation='relu'))
model.add(Dense(5, activation='softmax'))

#compile model using accuracy to measure model performance
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

#train the model
model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=20)

test_loss, test_acc = model.evaluate(X_test, y_test)

print(test_acc)

model_json = model.to_json()
with open("model.json", "w") as json_file:
    json_file.write(model_json)
# serialize weights to HDF5
model.save_weights("model.h5")
print("Saved model to disk")


