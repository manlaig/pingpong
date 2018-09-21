import tensorflow as tf
import numpy as np
from PIL import Image

class Bot:

    def __init__(self):
        self.model = tf.keras.models.load_model("bot_CNN.model")

    def getMove(self, filename):
        img = Image.open(filename)
        img = img.point(lambda x: 0.0 if x<128 else 1.0, 'L')
        
        img = np.array(img).astype("float32")
        img = img[..., np.newaxis]
        img = img[np.newaxis, :]
        ans = self.model.predict(np.array(img))
        return ans
        

    def getMoveArray(self, array):
        ans = self.model.predict(np.array(array))
        return ans