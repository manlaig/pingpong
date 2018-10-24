import tensorflow as tf
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.models import Sequential
import numpy as np
from dataset import load_data

model = Sequential()

model.add(Dense(32, activation=tf.nn.relu, input_shape=(3, 1)))
model.add(Dense(32, activation=tf.nn.relu))
model.add(Dense(3, activation=tf.nn.softmax))

model.compile(loss=tf.keras.losses.categorical_crossentropy,
              optimizer=tf.keras.optimizers.Adam(),
              metrics=['accuracy'])

model.fit()

model.save("model_ANN.py")