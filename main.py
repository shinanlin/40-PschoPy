import datetime
import pickle
import os
import copy
from stimulator import Stimulator
from ExperimentInformation.ExperimentInformation import ExperimentInformation

exp_info=ExperimentInformation()
exp_info.subname=input('请输入被试姓名：')

stim_info=input('请输入刺激类型，wn为1，ssvep为2：') 

while 1:
    if stim_info == '1':
        exp_info.addSTI = 'picFolder/wn'
        exp_info.stim_info='wn'
        break       
    elif stim_info == '2':
        exp_info.addSTI = 'picFolder/ssvep'
        exp_info.stim_info='ssvep'
        break
    else:
        stim_info=input('输入不符合要求，请重新输入：')
        

exp_info.blockNUM = int(input('请输入block数：'))
t = copy.copy(exp_info.getcue())


stimulator = Stimulator(exp_info)
stimulator.loadPics()
stimulator.run()

exp_info.cue_info = t

stimulator.getDroppedFrames()

exp_info.droppedframes = stimulator.viewContainer.droppedframes

exp_info.tofile()
