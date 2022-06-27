from UICreator.stiConfig import stiConfig
from UICreator.UIFactory import UIFactory

config = stiConfig()
factory = UIFactory(config)
frames = factory.getFrames()
factory.saveFrames(frames)

