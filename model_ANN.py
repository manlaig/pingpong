import tensorflow as tf
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.models import Sequential
import numpy as np
from dataset import load_data_text_file

(x_train, y_train) = load_data_text_file()

x_train = np.array(x_train).astype("float32")
x_train = x_train[..., np.newaxis]
y_train = tf.keras.utils.to_categorical(y_train, 3)

model = Sequential()

model.add(Flatten())
model.add(Dense(32, activation=tf.nn.relu))
model.add(Dense(32, activation=tf.nn.relu))
model.add(Dense(3, activation=tf.nn.softmax))

model.compile(loss=tf.keras.losses.categorical_crossentropy,
              optimizer=tf.keras.optimizers.Adam(),
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=10, batch_size=32)

model.save("bot_ANN.model")