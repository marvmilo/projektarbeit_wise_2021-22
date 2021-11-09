import time
import os
import sys
import marvmiloTools as mmt

#import other scripts
import cam
import robot
import GUI
scripts = [cam, robot, GUI]

#global values variable
values = mmt.dictionary.toObj(
    {
        "status": False,
        "marbel": {
            "color": None,
            "x": 0,
            "y": 0
        },
        "colors": {
            "red": {
                "container": None,
                "sorted": 0
            },
            "green": {
                "container": None,
                "sorted": 0
            },
            "yellow": {
                "container": None,
                "sorted": 0
            }
        },
        "total": {
            "marbels": 30,
            "sorted": 0,
            "seconds": 0.0,
            "precentage": 0.0
        }
    }
)

#prepare global sql function
sql_manager = mmt.SQL()
sql_manager.connect("database.db")
def sql(command):
    return sql_manager.execute(command)

if __name__ == '__main__':    
    #running scripts
    for s in scripts:
        thread = s.Thread(values, sql)
        #thread.start()
        
        #GUI debugger
        try:
            if sys.argv[1] == "--debugUI" and s == GUI:
                print("GUI DEBUG MODE ACTIVE!")
                GUI.webserver.init_callbacks(values, sql)
                GUI.webserver.run(debug = True)
            else: 
                thread.start()
        except IndexError:
            thread.start()

    #main loop
    try:
        while True:
            time.sleep(1)
                    
    except KeyboardInterrupt:
        sql_manager.disconnect()
        os._exit(0)