import threading

#import other Scripts
from . import webserver

#main function of script
def Main(values, sql):
    webserver.init_callbacks(values, sql)
    webserver.run()

#main thread of script
class Thread(threading.Thread):
    def __init__(self, values, sql):
        threading.Thread.__init__(self)
        self.values = values
        self.sql = sql
    def run(self):
        Main(self.values, self.sql)