import threading

#main function of script
def Main(values):
    print("this is UI Script")
    values.storage = 150

#main thread of script
class Thread(threading.Thread):
    def __init__(self, values):
        threading.Thread.__init__(self)
        self.values = values
    def run(self):
        Main(self.values)