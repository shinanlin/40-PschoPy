from os.path import join
from StimulationProcess.BasicStimulationProcess import BasicStimulationProcess
from psychopy.visual.rect import Rect
import time
from psychopy import visual, core, event
from psychopy.tools.monitorunittools import posToPix,cm2pix

class FinishProcess(BasicStimulationProcess):

    def __init__(self) -> None:
        super().__init__()


    def update(self):

        self.currentReport = self.controller.currentResult
        self.historyString.append(self.targetTable['DISPLAYCHAR'][self.currentReport])
        


    def change(self):

        # while self.messanger.exchange_message_operator.state_monitor.cue_state != 'CUE':
        #     time.sleep(0.1)
        
        if self.controller.endBlock:
            self.controller.currentProcess = self.controller.idleProcess
            self.historyString = []
        else:
            self.controller.currentProcess = self.controller.prepareProcess

        
        
    def run(self):

        self._showFeedback()
        time.sleep(1)
        self.change()

        pass


    def _showFeedback(self):
    
        self.controller.dialogue.draw()
        
        epochINX = self.controller.epochThisBlock
        
        histroString = self.historyString  
        feedbackText = ''.join(histroString)
        feedbackText = ' >>'+feedbackText

        feedback = self.drawDialogue(feedbackText,color='black',fillColor=None)
        feedback.draw()

        # result in this epoch
        commandId = self.commandID[self.controller.currentResult]
        resultChar = self.targetTable[commandId]
        resultChar = '%s'%(resultChar)
        placeholder = [' ' for _ in range(epochINX-1)]
        placeholder = ''.join(placeholder)
        resultText = '   '+placeholder+resultChar

        # correctness = 'red' if self.controller.blockCueText[epochINX] != self.targetTable[commandId] else 'green'
        correctness = 'black'
        result = self.drawDialogue(resultText, color=correctness,fillColor=None)
        result.draw()
        
        self.historyString.append(resultChar)
        self.controller.feedback = feedback
        self.w.flip(False)

        return
        

    

           

