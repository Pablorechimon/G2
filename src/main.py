import time
import random
from pathlib import Path
from SMWinservice import SMWinservice


class SensorService(SMWinservice) :
    _svc_name_ = "G2 Sensor Service"
    _svc_display_name_ = "G2 Sensor Service"
    _svc_description_ = "Sensor Service that will trigger G2 operations after file creation under specific path"

    def start(self) :
        self.isrunning = True

    def stop(self) :
        self.isrunning = False

    def main(self) :
        while self.isrunning :
            random.seed()
            x = random.randint(1, 1000000)
            Path(f'c:{x}.txt').touch()
            time.sleep(5)


if __name__ == '__main__' :
    PythonCornerExample.parse_command_line()
