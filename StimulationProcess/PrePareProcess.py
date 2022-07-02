import time
from StimulationProcess.BasicStimulationProcess import BasicStimulationProcess
from psychopy.visual.circle import Circle




class PrepareProcess(BasicStimulationProcess):
    def __init__(self) -> None:
        super().__init__()



    def change(self):

        # prepare --> stimulate
        time.sleep(2)
        self.controller.currentProcess = self.controller.stimulateProcess

    def run(self):
        # pop a cue
        self.controller.cueId = self.controller.blockCues.pop(0)
        self.controller.w = self._showCue(self.controller.cueId)


    def _showCue(self, id):
        """
        draw initial texture and show result
        :return: None
        """

        # 绘制初始帧
        self.initFrame.draw()

        # 绘制识别结果提示框 用tuple
        pos = self.targetPos[id].position
        x, y = pos
        y = y-90
        circle = Circle(win=self.w, pos=[x, y], radius=5)
        circle.colorSpace = 'rgb255'
        circle.color = (255, 0, 0)
        circle.draw()

        self.w.flip(False)
        time.sleep(0.5)

        return self.w
