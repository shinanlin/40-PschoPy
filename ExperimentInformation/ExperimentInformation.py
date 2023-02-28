from UICreator.stiConfig import stiConfig
import random
import numpy as np
import scipy.io as scio
import os
import sys
import pickle

class ExperimentInformation(stiConfig):
    def __init__(self,paradigm):
        super().__init__(paradigm=paradigm)
        #被试姓名
        self.subname = None
        #刺激信息wn/ssvep
        self.stim_info = None
        #block数
        self.blockNUM = None
        #cue次序信息list
        self.cue_info = None
        #掉帧信息list
        self.droppedframes = None
        self.rowNUM,self.columnNUM = self.layout
        self.targetNUM = self.rowNUM * self.columnNUM
        self.saveFolder = None
        self.addSTI = None
        self.trialNUM_eachblock = None
        self.stiLEN = None
        self.paradigm = paradigm

    def getcue(self):
        random.seed(1)
        if self.paradigm == 'wn':
            cueOrder=np.arange(0,self.targetNUM)
        else:
            cueOrder=np.arange(self.targetNUM,2*self.targetNUM)
        random.shuffle(cueOrder)
        # cueOrder=0
        self.cue_info=np.tile(cueOrder,self.blockNUM).tolist()
        return self.cue_info
        
    def tofile(self):
        d={'subname' : self.subname, 'stim_info': self.stim_info, 'blockNUM': self.blockNUM, 'cue_info': self.cue_info, 'droppedframes': self.droppedframes}
        self.saveFolder = os.path.join(os.getcwd(), 'ExperimentInformation', self.subname, self.stim_info)
        if os.path.exists(self.saveFolder) is False:
            os.makedirs(self.saveFolder)
        with open(self.saveFolder+os.sep+'expinfo.pickle', "wb+") as fp:
            pickle.dump(d, fp, protocol=pickle.HIGHEST_PROTOCOL)