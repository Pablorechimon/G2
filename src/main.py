import time
import random
from pathlib import Path
from SMWinservice import SMWinservice
import Sensor


class SensorService(SMWinservice) :
    _svc_name_ = "G2 Sensor Service"
    _svc_display_name_ = "G2 Sensor Service"
    _svc_description_ = "Sensor Service that will trigger G2 operations after file creation under specific path"

    def start(self) :
        self.isrunning = True

    def stop(self) :
        self.isrunning = False

    def main(self) :
        observer = Sensor.create_observer()
        Sensor.sensor(observer)
        while True :
            if not self.isrunning:
                Sensor.stop_sensor(observer)
                break


if __name__ == '__main__' :
    SensorService.parse_command_line()
