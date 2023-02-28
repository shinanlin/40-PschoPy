import os
import copy
from stimulator import Stimulator
from ExperimentInformation.ExperimentInformation import ExperimentInformation

stim_info=input('请输入刺激类型，wn为1，ssvep为2：')

if stim_info=='1':
    paradigm='wn'
elif stim_info=='2':
    paradigm='ssvep'

exp_info=ExperimentInformation(paradigm=paradigm)

exp_info.subname=input('请输入被试姓名：')

exp_info.addSTI ='picFolder'+os.sep+paradigm
exp_info.stim_info = paradigm

exp_info.blockNUM = int(input('请输入block数：'))
exp_info.trialNUM_eachblock = 40
exp_info.stiLEN = 1
t = copy.copy(exp_info.getcue())


stimulator = Stimulator(exp_info)
stimulator.loadPics()
stimulator.run()

exp_info.cue_info = t

stimulator.getDroppedFrames()

exp_info.droppedframes = stimulator.viewContainer.droppedframes

exp_info.tofile()
