import datetime
import pickle
import os
from stimulator import Stimulator
from Config import Config


config = Config()
texts = ['am i in control? or it is just a delusion?',
        'i am typing at by own will',
        'hello mr.robot,are you talking to me?',
        'this feels like the matrix']

mask = ['in-ok,control-lorlnoc,delusion-illusion',
        'own-you',
        'robot-tobor,talking-running',
        'this-that']

config.expINFO(texts=texts)
config.maskCue(mask)


config.addSTI = 'picFolder/ssvep'
config.resolution = (1920,1080)

stimulator = Stimulator(config)
stimulator.loadPics()
stimulator.run()
