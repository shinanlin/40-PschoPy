import time
from StimulationProcess.BasicStimulationProcess import BasicStimulationProcess
from psychopy.visual.rect import Rect
from psychopy.visual.circle import Circle

class PrepareProcess(BasicStimulationProcess):
    def __init__(self) -> None:
        super().__init__()

        
    def update(self):
        self.controller.cue_id=self.cue.pop(0)
        # 这里应该拿到下一trial的cue是什么
        pass

    def change(self):
        

        # prepare --> stimulate
        self.controller.current_process = self.controller.stimulate_process

    def run(self):
        
        self.update()
        self.w=self._showCue(self.controller.cue_id)
        self.change()

    def _showCue(self,id):
        #绘制初始帧
        # self.w.flip(False)
        self.initFrame.draw()
        
        #绘制识别结果提示框
        stimTargetRectCell = self.targetPos
        pos=stimTargetRectCell[id % 40].position
        
        resultRect=Rect(win=self.w,pos=pos,width=140,height=140,units='pix', fillColor='Red')
        resultRect.draw()
        
        self.w.flip()

        time.sleep(0.5)
        # self.initFrame.draw()
        
        x,y = pos
        y = y-90
        circle = Circle(win=self.w,pos=[x,y],radius=4, fillColor='Red', units='pix')
        circle.draw()
        self.initFrame.draw()
        
        self.w.flip(False)
        time.sleep(0.2)
        
        circle.draw()
        self.initFrame.draw()
        self.w.flip(False)
        time.sleep(0.3)
        
        
        return self.w
