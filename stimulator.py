from cmath import exp
from numpy import random
import datetime
import time
from psychopy import visual, core, event
from StimulationProcess.StimulateProcess import StimulateProcess
from StimulationProcess.StimulationController import StimulationController
import os
from tqdm import tqdm
import numpy as np
import pickle
import random

class viewContainer():
    # container 应该包含所有刺激所需的要素
    def __init__(self) -> None:
        super().__init__()
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
        self.stim_info = None
        self.targetNUM = None
        self.droppedframes = None
        self.trialNUM_eachblock = None
        pass


class Stimulator():

    def __init__(self,exp_info) -> None:

        self.addSTI = exp_info.addSTI
        
        # viewContainer 用来装载刺激呈现的要素
        self.viewContainer = viewContainer()
        self.viewContainer.stim_info = exp_info.stim_info
        self.viewContainer.targetNUM = exp_info.targetNUM
        self.viewContainer.cue = exp_info.cue_info
        self.viewContainer.trialNUM_eachblock = exp_info.trialNUM_eachblock
        
        # controller 用来控制刺激呈现

        self.controller = StimulationController()
        
        pass 


    def loadPics(self):

        win = visual.Window([1920, 1080], monitor="testMonitor", units="pix", fullscr=True,waitBlanking=True, color=(0, 0, 0), colorSpace='rgb255', screen=0,allowGUI=True)
        # win.close()
        picAdd = os.listdir(self.addSTI)
        frameSet = []
        # initial frame
        add = self.addSTI + os.sep + 'initial_frame.png'
        initFrame = visual.ImageStim(win, image=add, pos=[0, 0], size=[
                                    1920, 1080], units='pix', flipVert=False)

        # stimulation frames

        for picINX in tqdm(range(len(picAdd)-2)):
            add = self.addSTI + os.sep + '%i.png' % picINX
            frame = visual.ImageStim(win, image=add, pos=[0, 0], size=[
                                        1920, 1080], units='pix', flipVert=False)
            frameSet.append(frame)

        self.viewContainer.w = win
        self.viewContainer.frameSet = frameSet
        self.viewContainer.initFrame = initFrame
        
        # writing
        # blockNUM=1
        # targetNUM=40
        # cueOrder=np.arange(0,targetNUM)
        # random.shuffle(cueOrder)
        # self.viewContainer.cue=np.tile(cueOrder,blockNUM).tolist()
                
        # writing
        
        with open(self.addSTI+os.sep+'STI.pickle', "rb") as fp:
            self.viewContainer.targetPos = pickle.load(fp)

        return self

    def run(self):

        self.controller.initial(self.viewContainer)

        while self.controller.end == False:
            self.controller.run()
            # self.controller.change()

    def getDroppedFrames(self):
        self.viewContainer.droppedframes = self.controller.stimulate_process.droppedframes
    


if __name__ == '__main__':
    
    addSTI = 'picFolder/ssvep'
    stimulator = Stimulator(addSTI)
    stimulator.loadPics()
    stimulator.run()
