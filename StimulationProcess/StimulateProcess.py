from StimulationProcess.BasicStimulationProcess import BasicStimulationProcess
from psychopy import visual, core, event
from EventController import EventController
import datetime
import matplotlib.pyplot as plt
from psychopy import logging

class StimulateProcess(BasicStimulationProcess):
    def __init__(self) -> None:
        super().__init__()
        

    def change(self):
        # stimulate --> finish
        self.controller.current_process = self.controller.finish_process


    def run(self):
        
        self.w.flip()
        # 发送trigger

        # self.eventController.sendEvent(self.controller.cue_id+1)

        # 这一步是为了记录每一帧的时间，用来检查是否掉帧
        self.w.recordFrameIntervals = True
        self.w.refreshThreshold = 0.001+1/60
        logging.console.setLevel(logging.WARNING)

        inx = 0
        while inx<30:
            self.frameSet[inx].draw()
            self.w.flip(False)
            inx += 1
    

        print('Overall trial dropped %i frames'%self.w.nDroppedFrames)
        self.w.frameIntervals = []
        self.w.recordFrameIntervals = False
        # self.eventController.clearEvent()





    def check_key_board(self):
        for i in event.getKeys():
            if i == 'escape':
                self.w.close()
                core.quit()
                raise Exception("SSVEPExperiment: UserInterrupt", '用户中断实验')
                
            elif i == 'delete':
                #message = ToOperationSendingExchangeMessage.ClearResultOperation
                print('\nStimulateProcess发送清空结果显示指令，执行时间{}\n'.format(datetime.datetime.now()))
