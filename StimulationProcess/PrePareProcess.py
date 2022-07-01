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
        self.w.flip(False)
        self.initFrame.draw()
        
        #绘制识别结果提示框
        stimTargetRectCell = self.targetPos
        pos=stimTargetRectCell[id].position
        
        resultRect=Rect(win=self.w,pos=pos,width=145,height=145,units='pix',lineWidth=5)
        resultRect.lineColorSpace = 'rgb255'      
        resultRect.lineColor = (255, 0, 0)
        resultRect.fillColor = None
        resultRect.opacity = 0.9
        resultRect.draw()
        
        self.w.flip()

        time.sleep(1.5)

        self.initFrame.draw()
        
        x,y = pos
        y = y-90
        circle = Circle(win=self.w,pos=[x,y],radius=4)
        circle.colorSpace = 'rgb255'
        circle.color = (255,0,0)
        circle.draw()
        

        self.w.flip()
        time.sleep(1)
        
        
        return self.w
