import marvmiloTools as mmt

#import webserver script
from GUI import webserver

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
    webserver.init_callbacks(values, sql)
    webserver.run(debug = True, port = 8050)