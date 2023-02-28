from EventController import EventController
from StimulationProcess.BasicStimulationProcess import BasicStimulationProcess
from psychopy import event, visual
import time

class InitialProcess(BasicStimulationProcess):
    
    def __init__(self) -> None:
        super().__init__()


    def change(self):
        
        #initial --> prepare
        self.controller.current_process = self.controller.prepare_process
       
    def run(self):


        self.w.flip()
        text = '实验即将开始，请保持平静，按空格键继续'
        prepare_finish_text=visual.TextStim(self.w, pos=[0, 0], text=text, color=(255, 255, 255),colorSpace='rgb255')
        prepare_finish_text.draw()
        self.w.flip()
        event.waitKeys(keyList=['space'])
        self._openEyes()
        # self._closeEyes()
        self.change()


    def _openEyes(self):
        self.w.flip()

        text = visual.TextStim(
            self.w, pos=[0, 0], text='请注释屏幕中央的标记，保持视线稳定',
            color=(255, 255, 255), colorSpace='rgb255'
        )
        text.draw()
        self.w.flip()

        time.sleep(3)
        
        cross = visual.ShapeStim(
            win=self.w, name='polygon', vertices='cross',
            size=(50, 50),
            ori=0.0, pos=(0, 0),
            lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
            opacity=None, depth=0.0, interpolate=True)

        cross.draw()
        self.w.flip()
        time.sleep(3)
        self.w.flip()