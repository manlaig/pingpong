"""
	train the CNN here and save the model as a .model file
"""

import tensorflow as tf
from tensorflow.keras.layers import Dense, Conv2D, MaxPooling2D, Dropout, Flatten
from tensorflow.keras.models import Sequential
import numpy as np
from dataset import load_data
from PIL import Image

(x_train, y_train) = load_data()

x_train = np.array(x_train).astype("float32")
x_train = x_train[..., np.newaxis]

y_train = tf.keras.utils.to_categorical(y_train, 3)

model = Sequential()
model.add(Conv2D(32, kernel_size=(3, 3),
                 activation='relu',
                 input_shape=(32,32,1)))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(Dropout(0.25))

model.add(Flatten())
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.25))

model.add(Dense(3, activation='softmax'))

model.compile(loss=tf.keras.losses.categorical_crossentropy,
              optimizer=tf.keras.optimizers.Adam(),
              metrics=['accuracy'])

model.fit(x_train, y_train,
          batch_size=20,
          epochs=5)

model.save("bot_CNN.model")
"""
model = tf.keras.models.load_model("bot_CNN.model")

model.fit(x_train, y_train,
          batch_size=20,
          epochs=4)
model.save("bot_updated.model")

score = model.evaluate(x_train, y_train, verbose=0)
print('Test loss:', score[0])
print('Test accuracy:', score[1])
"""