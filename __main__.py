import time
import os
import marvmiloTools as mmt

#import other scripts
import cam
import robot
import GUI
scripts = [cam, robot, GUI]

#global values variable
values = mmt.json.load("values.json")

#prepare global sql function
sql_manager = mmt.SQL()
sql_manager.connect("database.db")
def sql(command):
    return sql_manager.execute(command)

if __name__ == '__main__':    
    #running scripts
    for s in scripts:
        thread = s.Thread(values, sql)
        thread.start()

    #main loop
    try:
        while True:
            time.sleep(1)
                    
    except KeyboardInterrupt:
        sql_manager.disconnect()
        os._exit(0)