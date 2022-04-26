class Sensor :
    def __init__(self, path, filename) :
        self.filename = filename
        self.path = path

    def getFileChange(self) :
        return "Watchdog"

    def initialize(self) :
        return "Start"
