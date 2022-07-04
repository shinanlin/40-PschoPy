from abc import ABCMeta, abstractmethod
from psychopy.visual.rect import Rect
from psychopy.visual.circle import Circle
from psychopy import visual, core, event

import time

class BasicStimulationProcess:

    def __init__(self) -> None:
        pass

    @abstractmethod
    def initial(self, controller, viewContainer):

        self.controller = controller
        self.w = viewContainer.w

        self.initFrame = viewContainer.initFrame
        self.frameSet = viewContainer.frameSet

        self.controller.historyString = []
        self.char = viewContainer.char        
        self.targetPos = viewContainer.targetPos
        self.stringPos = viewContainer.stringPos

        self.cues = viewContainer.cue
        self.targetNUM = viewContainer.targetNUM
        self.blockSize = self.targetNUM//2
        self.cueText = viewContainer.displayChar
        self.eventController = None

        pass

    @abstractmethod
    def update(self):

        pass



    @abstractmethod
    def change(self):

        pass


    @abstractmethod
    def run(self):

        pass

    def drawDialogue(self,text,color,fillColor):
        
        dialogue = visual.TextBox2(
        self.w, text=text, font='Hack',units='pix',
        pos=(-735, 525), letterHeight= 50.0,
        size=(1470, 50), borderWidth=2.0,
        color=color, colorSpace='rgb',
        opacity=None,
        bold=False, italic=False,
        lineSpacing=1.0,
        padding=0.0, alignment='top-left',
        anchor='top-left',
        fillColor='None', borderColor=None,
        editable=False,
        autoLog=True,)
        
        return dialogue

    
    def _showCue(self, id):
        """
        draw initial texture and show result
        :return: None
        """

        self.initFrame.draw()
        self.controller.feedback.draw()
        self.controller.dialogue.draw()
        
        
        # rect
        pos = self.targetPos[id].position
        rect = Rect(win=self.w,pos=pos,width=140,height=140,units='pix',fillColor='Red')
        rect.draw()
        self.w.flip()

        time.sleep(1)

        # circle
        self.initFrame.draw()
        self.controller.feedback.draw()
        self.controller.dialogue.draw()
        

        # x, y = pos
        # y = y-90
        # circle = Circle(win=self.w, pos=[x,y], radius=5)
        # circle.colorSpace = 'rgb255'
        # circle.color = (255, 0, 0)
        # circle.draw()

        # self.w.flip(False)

        time.sleep(1)

        return self.w



