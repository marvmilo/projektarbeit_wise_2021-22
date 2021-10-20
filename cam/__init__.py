import threading

#main function of script
def Main(values, sql):
    print("this is cam Script")
    
#main thread of script
class Thread(threading.Thread):
    def __init__(self, values, sql):
        threading.Thread.__init__(self)
        self.values = values
        self.sql = sql
    def run(self):
        Main(self.values, self.sql)