import numpy as np
import math
import random
import string


class Config():

    def __init__(self) -> None:
        self.defaultConfig()
        pass
    
    def defaultConfig(self,):

        self.displayINFO()
        self.subINFO()
        self.expINFO()

        pass

    def subINFO(self,personName='joedoe',age='unknown',gender='m/f'):
        self.personName = personName
        self.age = age
        self.gender = gender
        pass

    def displayINFO(self, refreshRate=60, stiLEN=3, resolution=(1920, 1080), layout=(5, 8), cubicSize=140, interval=50, trim=(225, 90), phase=np.tile(np.arange(0, 2, 0.5)*math.pi, 10), frequency=np.linspace(8.0, 15.8, 40), char=list(string.ascii_lowercase) + list(np.arange(10))+['.', ' ', ',', '?'],):

        self.refreshRate = refreshRate
        self.stiLEN = stiLEN

        self.resolution = resolution
        self.layout = layout
        self.cubicSize = cubicSize
        self.interval = interval
        self.trim = trim


        self.frequency = frequency
        self.phase = phase
        self.char = char
        
        pass

    def expINFO(self, COM='abcd', targetNUM=40, blockNUM=6, srate=250, winLEN=1, paradigm='ssvep', saveAdd='picFolder',texts='random'):

        
        self.paradigm=paradigm
        self.saveAdd = saveAdd
        self.COM = COM
        self.targetNUM = targetNUM
        self.blockNUM = blockNUM
        self.srate = srate
        self.winLEN = winLEN

        self.projectCue(texts)

        
        pass
    
    def projectCue(self,texts):
        if texts == 'random':
            cueOrder = np.arange(0, self.targetNUM)
            random.seed(253)
            random.shuffle(cueOrder)
            self.cue = np.tile(cueOrder, (self.blockNUM,1))
            self.displayChar = [[' %s' % self.char[i] for i in cue] for cue in self.cue]
        else:
            self.cue = [[self.char.index(s) for s in text] for text in texts]
            self.displayChar = texts

        return

    def maskCue(self,masks):
        masked = []
        for (display,mask) in zip(self.displayChar,masks):
            for s in mask.split(','):
                display = display.replace(s.split('-')[0],s.split('-')[-1])
            masked.append(display)
        self.masked = masked



if __name__=='__main__':
    
    config = Config()
    texts = ['am i in control? or it is just a delusion?',
            'i am typing at by own will',
            'helllo mr.robot,are you talking to me?']


        
    masks = ['in-on,delusion-illusion',
            'own-you',
            'robot-tobor,talking-running',
            'this-that']
    
    config.expINFO(texts=texts)
    config.maskCue(masks=masks)
        
