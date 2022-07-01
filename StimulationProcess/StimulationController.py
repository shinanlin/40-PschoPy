import sys
sys.path.append('.././EventControl')
from StimulationProcess.IdleProcess import IdleProcess
from StimulationProcess.PrePareProcess import PrepareProcess
from StimulationProcess.StimulateProcess import StimulateProcess
from StimulationProcess.FinishProcess import FinishProcess
from EventController import EventController

import datetime

class StimulationController:
    def __init__(self):

        self.initialProcess = None
        self.prepareProcess = None
        self.stimulateProcess = None
        self.idleProcess = None
        self.finishProcess = None
        self.currentProcess = None

        # 显示界面
        self.win = None

        self.endBlock = False
        self.endSession = None

        # 当前epoch的cue
        self.cueId = None
        # 当前block的提示编号
        self.blockCues = None
        # 当前block提示字符
        self.blockCueText = None
        # 当前epoch的编号
        self.currentEpochINX = 0
        # 当前block内epoch的编号
        self.epochThisBlock = 0
        # 当前block的编号
        self.currentBlockINX = 0
        # 当前epoch的结果（由operation返回）
        self.currentResult = None
        # 用户打字的字符框反馈
        self.feedback = None
        # 字符映射


    def initial(self, viewContainer):

        # trigger 控制器
        # self.eventController = EventController()

        # 开始
        self.idleProcess = IdleProcess()
        self.idleProcess.initial(self, viewContainer)
        
        # 准备阶段：展示cue，展示上次结果
        self.prepareProcess = PrepareProcess()
        self.prepareProcess.initial(self, viewContainer)

        # 开始刺激：刺激时展示cue
        self.stimulateProcess = StimulateProcess()
        self.stimulateProcess.initial(self, viewContainer)

        # 结束刺激：展示结果？
        
        self.finishProcess = FinishProcess()
        self.finishProcess.initial(self, viewContainer)

        self.currentProcess = self.idleProcess

    def change(self):
        self.currentProcess.change()

    def run(self):
        self.currentProcess.run()


