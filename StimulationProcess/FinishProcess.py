from os.path import join
from StimulationProcess.BasicStimulationProcess import BasicStimulationProcess
from psychopy.visual.rect import Rect
import time
from psychopy import visual, core, event
from psychopy.tools.monitorunittools import posToPix,cm2pix

class FinishProcess(BasicStimulationProcess):

    def __init__(self) -> None:
        super().__init__()
    
    def change(self):
         
        # finish --> process
        if len(self.cue)==0:
            self.controller.end = True
        elif len(self.cue) % self.trialNUM_eachblock == 0:
            self.controller.current_process = self.controller.rest_process
        else:
            self.controller.current_process = self.controller.prepare_process
        
        return

    def run(self):
        self.change()
        # 这里应该显示结果，如果是离线的话不用做什么
        return
