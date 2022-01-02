import marvmiloTools as mmt
import time

#import webserver script
from GUI import webserver
from GUI import debugger

#init necesarry vals
values = mmt.json.load("values.json")
sql_manager = mmt.SQL()
def sql(command):
    sql_manager.connect("database.db")
    resp = sql_manager.execute(command)
    sql_manager.disconnect()
    return resp

#run webserver
if __name__ == "__main__":
    debug_thread = debugger.Thread(values, sql)
    debug_thread.start()
    webserver.init_callbacks(values, sql)
    webserver.run(debug = True, port = 8050)