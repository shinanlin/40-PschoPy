from numpy import random
import datetime
import time
from psychopy import visual, core, event
from StimulationProcess.StimulationController import StimulationController
import os
from tqdm import tqdm
import numpy as np
import pickle

class viewContainer():
    # container 应该包含所有刺激所需的要素
    def __init__(self,config) -> None:

        # w 代表window,所有的刺激都要在win上显示
        self.w = None
        # initFrame代表初始帧,非刺激状态下都是这一帧
        self.initFrame = None
        # frameSet是ImageStim的集合,是刺激帧
        self.frameSet = None
        # cue应该是一串数组
        self.cue = None
        # targetPos是每个目标在屏幕上的位置,显示cue的时候用得到
        self.targetPos = None
        # stringPos是在线实验时候,字符的位置,暂时用不到
        self.stringPos = None

        
        self.takeConfig(config)
        pass

    def takeConfig(self,config):

        self.cue = config.cue
        self.targetNUM = config.targetNUM
        self.blockNUM = config.blockNUM
        self.displayChar = config.displayChar
        self.resolution = config.resolution

        pass


class Stimulator():

    def __init__(self,config) -> None:

        self.addSTI = config.addSTI

        # viewContainer 用来装载刺激呈现的要素
        self.viewContainer = viewContainer(config)
        # controller 用来控制刺激呈现

        self.controller = StimulationController()
        
        pass 


    def loadPics(self):

        xScreen,yScreen = self.viewContainer.resolution

        win = visual.Window([xScreen, yScreen], monitor="testMonitor", units="pix", fullscr=True,waitBlanking=True, color=(0, 0, 0), colorSpace='rgb255', screen=0,allowGUI=True)
        # win.close()
        picAdd = os.listdir(self.addSTI)
        frameSet = []
        # initial frame
        add = self.addSTI + os.sep + 'initial_frame.png'
        initFrame = visual.ImageStim(win, image=add, pos=[0, 0], size=[xScreen, yScreen], units='pix', flipVert=False)

        # stimulation frames

        for picINX in tqdm(range(len(picAdd)-2)):
            add = self.addSTI + os.sep + '%i.png' % picINX
            frame = visual.ImageStim(win, image=add, pos=[0, 0], size=[xScreen, yScreen], units='pix', flipVert=False)
            frameSet.append(frame)

        self.viewContainer.w = win
        self.viewContainer.frameSet = frameSet
        self.viewContainer.initFrame = initFrame        

        with open(self.addSTI+os.sep+'STI.pickle', "rb") as fp:
            pos = pickle.load(fp)
        
        self.viewContainer.targetPos = pos.rectSet
        self.viewContainer.stringPos = pos.stringPositions

        return self

    def run(self):

        self.controller.initial(self.viewContainer)

        while True:
            self.controller.run()
            self.controller.change()

    


if __name__ == '__main__':
    
    addSTI = 'picFolder/ssvep'
    stimulator = Stimulator(addSTI)
    stimulator.loadPics()
    stimulator.run()
