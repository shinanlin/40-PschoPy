from StimulationProcess.BasicStimulationProcess import BasicStimulationProcess
from psychopy import visual, core, event
from EventController import EventController
import datetime
import matplotlib.pyplot as plt
from psychopy import logging
from psychopy import parallel


class StimulateProcess(BasicStimulationProcess):
    def __init__(self) -> None:
        super().__init__()
        self.droppedframes = []
        
    def change(self):
        # stimulate --> finish
        self.initFrame.draw()
        self.w.flip()
        self.initFrame.draw()
        self.w.flip()
        
        self.controller.current_process = self.controller.finish_process
        self.controller.currenttrialINX += 1


    def run(self):
        
        # 发送trigger
        self.eventController = EventController()
        self.eventController.clearEvent()
        # 这一步是为了记录每一帧的时间，用来检查是否掉帧
        self.w.recordFrameIntervals = True
        self.w.refreshThreshold = 0.001+1/60
        logging.console.setLevel(logging.WARNING)

        inx = 0
        lastdroppedframes=self.w.nDroppedFrames
        while inx < self.stiLEN*self.refreshRate:
            if inx == 1:
                self.eventController.sendEvent(self.controller.cue_id+1)

            self.frameSet[inx].draw()
            self.w.flip(False)
            inx += 1
        
        self.getdroppedframes(self.w.nDroppedFrames-lastdroppedframes)

        print('Overall trial dropped %i frames'%self.w.nDroppedFrames)
        self.w.frameIntervals = []
        self.w.recordFrameIntervals = False
        self.eventController.clearEvent()
        
        self.change()

    def getdroppedframes(self,dframes):
        self.droppedframes.append(dframes)