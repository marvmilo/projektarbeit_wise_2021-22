import threading
import time

#main function of script
def Main(values):
    print("this is pixicam Script")
    time.sleep(1)
    print(values.pretty())

#main thread of script
class Thread(threading.Thread):
    def __init__(self, values):
        threading.Thread.__init__(self)
        self.values = values
    def run(self):
        Main(self.values)