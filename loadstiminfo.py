import pickle
import os

subname='1'
stim_info='wn'
file = os.path.join(os.getcwd(), 'ExperimentInformation', subname, stim_info, 'expinfo.pickle')
res=open(file,'rb')
info=pickle.load(res)
print(info)