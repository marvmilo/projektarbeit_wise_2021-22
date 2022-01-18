import marvmiloTools as mmt
import time
import os

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

debug_thread = debugger.Thread(values, sql)
debug_thread.daemon = True
debug_thread.start()
webserver.init_callbacks(values, sql)
webserver.run(debug = True, port = 8050)
os._exit(0)