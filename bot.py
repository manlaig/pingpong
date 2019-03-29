import tensorflow as tf
import numpy as np
from PIL import Image

class Bot:
    def __init__(self, modelName):
        self.modelName = modelName
        self.model = tf.keras.models.load_model(modelName)

    """
        get a filename as input and predict a move from it
        ex: pred = bot.getMove("Dataset_Formatted/d-23.jpg")
    """
    def getMove(self, filename):
        img = Image.open(filename)
        img = img.point(lambda x: 0.0 if x<128 else 1.0, 'L')
        
        img = np.array(img).astype("float32")
        img = img[..., np.newaxis]
        img = img[np.newaxis, :]
        
        ans = self.model.predict(np.array(img))
        return ans
        
    """
        get an array of the grayscale pixel values on the screen,
        predict and return a move
    """
    def getMoveArray(self, array):
        # the below line is for running a RNN model
        if self.modelName == "bot_RNN.model":
            array = np.squeeze(np.array(array), axis=3)
        ans = self.model.predict(array)
        return ans

    
    """
        given ball speed, ball position, and bot position,
        predict the right move
    """
    def getMoveText(self, ballSpeed, positionBall, positionP2Y):
        arr = np.array([ballSpeed[0], ballSpeed[1], positionBall[0], positionBall[1], positionP2Y])
        arr = arr[..., np.newaxis]        
        arr = arr[np.newaxis, :]
        ans = self.model.predict(arr)
        return ans
