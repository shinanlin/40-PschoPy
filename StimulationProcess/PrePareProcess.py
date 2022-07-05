import time
from StimulationProcess.BasicStimulationProcess import BasicStimulationProcess
from psychopy.visual.circle import Circle




class PrepareProcess(BasicStimulationProcess):
    def __init__(self) -> None:
        
        super().__init__()



    def change(self):

        # prepare --> stimulate
        time.sleep(1)
        self.controller.currentProcess = self.controller.stimulateProcess

    def run(self):
        # pop a cue
        cueId = self.controller.blockCues.pop(0)
        if self.char[cueId] == ' ':
            self.spaceNUM += 1
            self.controller.cueId = self.controller.blockCues.pop(0)
            self.controller.epochThisBlock += 1
            self.controller.historyString.append(' ')
                        
        else:
            self.controller.cueId = cueId

        if self.controller.blockCueText[self.controller.epochThisBlock] != self.controller.blockMask[self.controller.epochThisBlock]:
            self.controller.maskFlag = True
        else:
            self.controller.maskFlag = False

            
        self.controller.w = self._showCue(self.controller.cueId)

