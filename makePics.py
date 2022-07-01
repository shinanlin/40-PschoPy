from UICreator.UIFactory import UIFactory
from Config import Config

config = Config()
# config.resolution = (1920,1080)
config.stiLEN = 0.5


factory = UIFactory(config)
frames = factory.getFrames()
factory.saveFrames(frames)

