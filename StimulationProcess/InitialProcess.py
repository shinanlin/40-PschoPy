from EventController import EventController
from StimulationProcess.BasicStimulationProcess import BasicStimulationProcess

class InitialProcess(BasicStimulationProcess):
    
    def __init__(self) -> None:
        super().__init__()


    def change(self):
        
        #initial --> prepare
        self.controller.current_process = self.controller.prepare_process
       
    def run(self):


        self.w.flip()
        self.initFrame.draw()
        self.w.flip()

