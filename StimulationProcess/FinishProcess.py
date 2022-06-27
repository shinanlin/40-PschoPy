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
        self.controller.current_process = self.controller.prepare_process
        
        return

    def run(self):
        # 这里应该显示结果，如果是离线的话不用做什么
        return
