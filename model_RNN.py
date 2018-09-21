"""
    train the RNN here and save the model as a .model file
"""

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Flatten, LSTM
from dataset import load_data
import numpy as np

(x_train, y_train) = load_data()
x_train = np.array(x_train).astype("float32")


model = Sequential()
model.add(LSTM(128, input_shape=(32, 32), activation='relu', return_sequences=True))
model.add(Dropout(0.2))

model.add(LSTM(128, activation='relu'))
model.add(Dropout(0.2))

model.add(Dense(32, activation='relu'))
model.add(Dropout(0.2))

model.add(Flatten())
model.add(Dense(3, activation='softmax'))

model.compile(
    loss='sparse_categorical_crossentropy',
    optimizer="adam",
    metrics=['accuracy'])

model.fit(x_train,
          y_train,
          epochs=10)

model.save("bot_RNN.model")