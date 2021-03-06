# -*- coding: utf-8 -*-
"""Copy of Copy of CS2 III year RNN.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/github/muskan-patidar/ML-Lab/blob/main/RNN.ipynb
"""



#import required packages/library
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, LSTM#, CuDNNLSTM

"""Similar to before, we load in our data, and we can see the shape again of the dataset and individual samples:"""

mnist = tf.keras.datasets.mnist  # mnist is a dataset of 28x28 images of handwritten digits and their labels
(x_train, y_train),(x_test, y_test) = mnist.load_data()  # unpacks images to x_train/x_test and labels to y_train/y_test

x_train = x_train/255
x_test = x_test/255

print("x_train =",x_train.shape)
print("y_train =",y_train.shape)
print("x_test =",x_test.shape)
print("y_test =",y_test.shape)

print(x_train[0].shape)

"""Recall we had to flatten this data for the regular deep neural network. In this model, we're passing the rows of the image as the sequences. So basically, we're showing the the model each pixel row of the image, in order, and having it make the prediction. (28 sequences of 28 elements)"""

model = Sequential()

# IF you are running with a GPU, try out the CuDNNLSTM layer type instead (don't pass an activation, tanh is required)
model.add(LSTM(128, input_shape=(x_train.shape[1:]), activation='relu', return_sequences=True))
model.add(Dropout(0.2))

#return_sequences= True   # This flag is used for when you're continuing on to another recurrent layer.

model.add(LSTM(128, activation='relu'))
model.add(Dropout(0.1))

model.add(Dense(32, activation='relu'))
model.add(Dropout(0.2))

model.add(Dense(10, activation='softmax')) #output layer

model.summary()

"""Compile the model"""

opt = tf.keras.optimizers.Adam(lr=0.001, decay=1e-6)

# Compile model
model.compile(
    loss='sparse_categorical_crossentropy',
    optimizer=opt,
    metrics=['accuracy'],
)

"""Training to the model"""

model.fit(x_train,y_train,
          epochs=3,verbose=1)

score = model.evaluate(x_test, y_test)
print('Test score:', score[0])
print('Test accuracy:', score[1])