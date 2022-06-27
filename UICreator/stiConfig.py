import numpy as np
import math
import string

class stiConfig():
    def __init__(self):
        
        self.paradigm = 'ssvep'
        self.saveAdd = 'picFolder'
        
        self.refreshRate = 60
        self.stiLEN = 0.5
        self.resolution=(1920,1080)
        self.layout = (5,8)
        self.cubicSize = 140
        self.interval = 50
        self.initWidth, self.initHeight = (225, 90)

        self.frequency = np.linspace(8.0, 15.8, 40)
        self.phase = np.tile(np.arange(0, 2, 0.5)*math.pi, 10)
        self.displayChar = list(string.ascii_uppercase) + \
            list(np.arange(10))+['.', ' ', ',', 'Del']

        pass

