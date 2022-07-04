import time
from typing import Text
import numpy as np
from StimulationProcess.BasicStimulationProcess import BasicStimulationProcess
from psychopy import event, visual


class IdleProcess(BasicStimulationProcess):
    def __init__(self) -> None:
        super().__init__()

    def change(self):

        self.controller.currentProcess = self.controller.prepareProcess

    def run(self):
        # 本节实验结束界面
        self._idleInterface()
        # 等待键盘输入继续
        # event.waitKeys(keyList=['space'])

        # 更新当前block的信息
        self.update()
        # self.eventController.clearEvent()

        time.sleep(3)


    def _idleInterface(self):
        
        self.w.flip()
        if self.controller.currentBlockINX == 0:
            text = '实验即将开始，请保持平静，按空格键继续'
        else:
            text = '第%s节实验已经结束\n\n\n 休息结束结束后请按空格键继续实验' % self.controller.currentBlockINX
        text = visual.TextStim(self.w, pos=[0, 0], text=text, color=(255, 255, 255),
                                colorSpace='rgb255')
        text.draw()

        self.w.flip()

        self.controller.endBlock = False

        pass

    def update(self):

        self.controller.epochThisBlock = 0
        
        currentBlockINX = self.controller.currentBlockINX
        self.controller.blockCues = self.cues[currentBlockINX]
        self.controller.blockCueText = self.cueText[currentBlockINX]
        text = ' >>'+''.join(self.cueText[currentBlockINX])

        self.controller.dialogue = self.drawDialogue(text,color='gray',fillColor='white')
        self.controller.feedback = None

        self.initFrame.draw()
        self.controller.dialogue.draw()

        self.w.flip()
        self.controller.w = self.w
        self.controller.endBlock = False
        self.controller.feedback = self.drawDialogue("",color='White',fillColor=None)
        return 


    def _openEyes(self):
        self.w.flip()

        text = visual.TextStim(
            self.w, pos=[0, 0], text='请注释屏幕中央的标记，保持视线稳定',
            color=(255, 255, 255), colorSpace='rgb255'
        )
        text.draw()
        self.w.flip()

        time.sleep(1)
        
        
        cross = visual.ShapeStim(
            win=self.w, name='polygon', vertices='cross',
            size=(50, 50),
            ori=0.0, pos=(0, 0),
            lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
            opacity=None, depth=0.0, interpolate=True)

        cross.draw()
        self.w.flip()
        time.sleep(1)

        pass

    def _closeEyes(self):

        text = visual.TextStim(
            self.w, pos=[0, 0], text='请闭眼',
            color=(255, 255, 255), colorSpace='rgb255'
        )
        text.draw()

        self.w.flip()

        time.sleep(1)

        pass
        

    

           
