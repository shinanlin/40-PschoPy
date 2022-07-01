import pickle
import os

subname='diode'
file = os.path.join(os.getcwd(), 'ExperimentInformation', subname, 'expinfo.pickle')
res=open(file,'rb')
info=pickle.load(res)
print(info)