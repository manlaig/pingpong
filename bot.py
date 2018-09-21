import tensorflow as tf
import numpy as np
from PIL import Image

class Bot:

    modelName = "bot_RNN.model"

    def __init__(self):
        self.model = tf.keras.models.load_model(self.modelName)

    def getMove(self, filename):
        img = Image.open(filename)
        img = img.point(lambda x: 0.0 if x<128 else 1.0, 'L')
        
        img = np.array(img).astype("float32")
        img = img[..., np.newaxis]
        img = img[np.newaxis, :]
        
        ans = self.model.predict(np.array(img))
        return ans
        

    def getMoveArray(self, array):
        # comment this line if running on a CNN model
        # the below line is for running a RNN model
        if self.modelName == "bot_RNN.model":
            array = np.squeeze(np.array(array), axis=3)
        ans = self.model.predict(array)
        return ans