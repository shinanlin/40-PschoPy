from abc import ABCMeta, abstractmethod
from psychopy.visual.rect import Rect
from psychopy import visual, core, event

import time

class BasicStimulationProcess:

    def __init__(self) -> None:
        pass

    @abstractmethod
    def initial(self, controller, view_struct):

        self.controller = controller
        self.w = view_struct.w

        self.initFrame = view_struct.initFrame
        self.frameSet = view_struct.frameSet

        self.historyString = None
        self.cue = view_struct.cue
        self.targetPos = view_struct.targetPos
        self.stringPos = view_struct.stringPos

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
    