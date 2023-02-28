from UICreator.stiConfig import stiConfig
from UICreator.UIFactory import UIFactory

for p in ['wn','ssvep']:
    config = stiConfig(paradigm=p)
    factory = UIFactory(config)
    frames = factory.getFrames()
    factory.saveFrames(frames)

