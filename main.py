import datetime
import pickle
import os
from stimulator import Stimulator


addSTI = 'picFolder/ssvep'
stimulator = Stimulator(addSTI)
stimulator.loadPics()

stimulator.run()
