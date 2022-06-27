import sys
sys.path.append('.././EventControl')
from StimulationProcess.InitialProcess import InitialProcess
from StimulationProcess.PrePareProcess import PrepareProcess
from StimulationProcess.StimulateProcess import StimulateProcess
from StimulationProcess.FinishProcess import FinishProcess
from EventController import EventController

import datetime

class StimulationController:
    def __init__(self):

        self.initial_process = None
        self.prepare_process = None
        self.stimulate_process = None
        self.finish_process = None
        self.current_process = None
        self.cue_id = None
        self.end = False

    def initial(self, view_struct):

        # trigger 控制器
        # self.eventController = EventController()

        # 开始
        self.initial_process = InitialProcess()
        self.initial_process.initial(self, view_struct)
        
        # 准备阶段：展示cue，展示上次结果
        self.prepare_process = PrepareProcess()
        self.prepare_process.initial(self, view_struct)

        # 开始刺激：刺激时展示cue
        self.stimulate_process = StimulateProcess()
        self.stimulate_process.initial(self, view_struct)

        # 结束刺激：展示结果？
        
        self.finish_process = FinishProcess()
        self.finish_process.initial(self, view_struct)

        self.current_process = self.initial_process

    def change(self):
        
        self.current_process.change()
        

    def run(self):
        print('\n开始进入{0}呈现阶段，执行时间{1}\n'.format(self.__class__.__name__, datetime.datetime.now()))
        self.current_process.run()

        