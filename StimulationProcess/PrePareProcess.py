import time
from StimulationProcess.BasicStimulationProcess import BasicStimulationProcess



class PrepareProcess(BasicStimulationProcess):
    def __init__(self) -> None:
        super().__init__()


        
    def update(self):

        # 这里应该拿到下一trial的cue是什么
        pass

    def change(self):


        # prepare --> stimulate
        self.controller.current_process = self.controller.stimulate_process

    def run(self):
        
        self.update()


