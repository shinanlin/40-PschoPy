from psychopy import parallel
9/8
class EventController():
    def __init__(self,COM=12544) -> None:
        self.address = COM
        self.port = parallel.ParallelPort(self.address)
        self.clearEvent()
        
    def sendEvent(self,eventType):
        self.port.setData(eventType)

    def clearEvent(self):
        self.port.setData(0)
    