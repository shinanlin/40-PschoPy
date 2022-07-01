from abc import ABCMeta, abstractmethod
from psychopy.visual.rect import Rect
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

        self.historyString = None
        self.cue = viewContainer.cue
        self.targetPos = viewContainer.targetPos
        self.stringPos = viewContainer.stringPos

        self.cues = viewContainer.cue
        self.targetNUM = viewContainer.targetNUM
        self.blockSize = self.targetNUM//2
        self.cueText = viewContainer.displayChar
        self.stringPosition = viewContainer.stringPos
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
        self.w, text=text, font='Hack',
            pos=(-0.8, 0.5), letterHeight=0.03,
            size=(1.5, 0.05), borderWidth=2.0,
            color='white', colorSpace='rgb',
            opacity=None,
            bold=False, italic=False,
            lineSpacing=1.0,
            padding=0.0, alignment='top-left',
            anchor='top-left',
            fillColor='white', borderColor=None,
            editable=False,
            name='textbox_2',
            autoLog=True,)

        # dialogue.pos = (0.5, 0.9)
        
        dialogue.draw()
        self.initFrame.draw()
        self.w.flip()
        

        return dialogue



