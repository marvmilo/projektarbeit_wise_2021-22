import threading
import time

def Main(values, sql):
    time.sleep(5)
    values.server.status = "connected 192.168.1.69"

class Thread(threading.Thread):
    def __init__(self, values, sql):
        threading.Thread.__init__(self)
        self.values = values
        self.sql = sql
    def run(self):
        Main(self.values, self.sql)