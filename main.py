import datetime
import pickle
import os
from stimulator import Stimulator
from Config import Config


config = Config()
config.addSTI = 'picFolder/ssvep'
config.resolution = (1440,900)

stimulator = Stimulator(config)
stimulator.loadPics()
stimulator.run()
