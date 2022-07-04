from StimulationProcess.BasicStimulationProcess import BasicStimulationProcess
from psychopy import visual, core, event
from EventController import EventController
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')
import datetime
from psychopy import logging

class StimulateProcess(BasicStimulationProcess):
    def __init__(self) -> None:
        super().__init__()
        
    def update(self):
        self.controller.endBlock = self._checkBlock()

        self.w.flip()
        self.initFrame.draw()
        self.controller.feedback.draw()
        self.controller.dialogue.draw()

        feedback = self.controller.feedback
        if feedback is not None:
            feedback.draw()

        # 增加另一个epoch
        self.controller.currentEpochINX += 1
        # 增加另一个epoch
        self.controller.epochThisBlock += 1
        pass

    def change(self):
        # stimulate --> finish
        self.controller.currentProcess = self.controller.finishProcess


    def run(self):
        
        controller = self.controller
        self.w = controller.w

        # 发送trigger

        # self.eventController.sendEvent(self.controller.cue_id+1)

        # 这一步是为了记录每一帧的时间，用来检查是否掉帧
        frameINX = 0
        self.w.flip(False)

        startTime = core.getTime()
        self.w.recordFrameIntervals = True
        while frameINX < len(self.frameSet):
        
            # if frameINX == 0:
                # self.eventController.sendEvent(self.controller.cueId+1)
                
            self.frameSet[frameINX].draw()
            self.w.flip(clearBuffer=False)
            frameINX += 1
            # if frameINX == len(self.frameSet):
            #     frameINX = 0
        f = plt.figure()
        plt.plot(self.w.frameIntervals)
        plt.ylim(0.0157,0.0177)
        plt.savefig('FRAME.png')

        self.w.frameIntervals = []
        self.w.recordFrameIntervals = False
        endTime = core.getTime()
        self.update()

        # self.eventController.clearEvent()


    def _checkBlock(self):
    
        if self.controller.blockCues == []:
            self.controller.currentBlockINX += 1
            return True
        else:
            return False

