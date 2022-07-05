from os.path import join
from StimulationProcess.BasicStimulationProcess import BasicStimulationProcess
from psychopy.visual.rect import Rect
import time
import numpy as np
from psychopy import visual, core, event
from psychopy.tools.monitorunittools import posToPix,cm2pix

class FinishProcess(BasicStimulationProcess):

    def __init__(self) -> None:
        super().__init__()


    def update(self):

        # self.currentReport = self.controller.currentResult
        self.currentReport = np.random.randint(20,size=1)[0]
        self.controller.historyString.append(self.char[self.currentReport])
        


    def change(self):

        # while self.messanger.exchange_message_operator.state_monitor.cue_state != 'CUE':
        #     time.sleep(0.1)
        
        if self.controller.endBlock:
            self.controller.currentProcess = self.controller.idleProcess
            self.controller.historyString = []
        else:
            self.controller.currentProcess = self.controller.prepareProcess

        
        
    def run(self):

        # self.update()
        self.currentReport = 0
        self._showFeedback()
        # self.controller.historyString.append(self.char[self.currentReport])
        time.sleep(1)

        pass


    def _showFeedback(self):
    
        self.controller.dialogue.draw()
        
        epochINX = self.controller.epochThisBlock-1
        
        histroString = self.controller.historyString  
        feedbackText = ''.join(histroString)

        feedbackText = ' >>'+feedbackText

        feedback = self.drawDialogue(feedbackText,color='green',fillColor=None)
        feedback.draw()

        # result in this epoch
        if self.controller.maskFlag:
            resultChar = self.controller.blockMask[epochINX]
            self.controller.maskFlag = False
        else:
            resultChar = self.char[self.currentReport]
        resultChar = '%s'%(resultChar)
        placeholder = [' ' for _ in range(epochINX)]
        placeholder = ''.join(placeholder)
        resultText = '   '+placeholder+resultChar

        # correctness = 'red' if self.controller.blockCueText[epochINX] != self.targetTable[commandId] else 'green'
        correctness = 'red'
        result = self.drawDialogue(resultText, color=correctness,fillColor=None)
        result.draw()
        
        feedback = self.drawDialogue(feedbackText+resultChar,color='green',fillColor=None)
        self.controller.historyString.append(resultChar)
        self.controller.feedback = feedback

        self.w.flip(False)

        return
        

    

           

