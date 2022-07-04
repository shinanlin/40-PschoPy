from UICreator.UIFactory import UIFactory
from Config import Config

config = Config()
config.stiLEN = 0.5


factory = UIFactory(config)
frames = factory.getFrames()
factory.saveFrames(frames)

