import time
import os
import marvmiloTools as mmt

#import other scripts
import pixicam
import robot
import UI
scripts = [pixicam, robot, UI]

#global values variable
values = mmt.dictionary.toObj(
    {
        "storage": 200,
        "containters": [
            0,
            0,
            0,
            0
        ],
        "color": {
            "current": None,
            "next": None,
            "red": {
                "container": None,
                "total": 50
            },
            "green": {
                "container": None,
                "total": 50
            },
            "blue": {
                "container": None,
                "total": 50
            },
            "yellow": {
                "container": None,
                "total": 50
            }
        }
    }
)

#running scripts
for s in scripts:
    thread = s.Thread(values)
    thread.start()

#main loop
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    os._exit(0)