import datetime
import pickle
import os
from stimulator import Stimulator
from Config import Config


config = Config()
texts = ['am i in control? or it is just a delusion?',
        'i am typing at by own will',
        'helllo mr.robot,are you talking to me?',
        'this feels like the matrix']
config.expINFO(texts=texts)

config.addSTI = 'picFolder/ssvep'
config.resolution = (1920,1080)

stimulator = Stimulator(config)
stimulator.loadPics()
stimulator.run()
