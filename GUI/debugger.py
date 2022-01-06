import threading
import time
import random
import os


#for setting / resetting balls
def set_balls():
    global balls
    balls = {
        "red": 6,
        "green": 7,
        "yellow": 4
    }
set_balls()

def Main(values, sql):
    time.sleep(5)
    values.server.status = "connected 192.168.1.69"
    
    #main loop
    while True:
        if values.robot.movementclear:
            values.ball.total = sum(balls.values())
            values.ball.to_collect = sum([balls[c] for c in balls.keys() if values.colors[c].container_num])
            values.colors.red.total = balls["red"]
            values.colors.green.total = balls["green"]
            values.colors.yellow.total = balls["yellow"]
            while any(balls.values()) and values.robot.movementclear:
                try:
                    color = random.choice([c for c in balls.keys() if values.colors[c].container_num and balls[c]])
                except IndexError:
                    break
                values.ball.color = color
                values.ball.x = random.randrange(0, 202)
                values.ball.y = random.randrange(0, 289)
                time.sleep(random.uniform(3,5))
                balls[color] -= 1
                values.ball.done += 1
                values.colors[color].sorted += 1
            values.robot.movementclear = False
            values.ball.color = None
            values.ball.x = 0
            values.ball.y = 0
            values.UI.sorting_done = True
        elif values.UI.sorting_done == False:
            values.ball.total = 0
            values.ball.done = 0
            values.colors.red.sorted = 0
            values.colors.red.total = 0
            values.colors.green.sorted = 0
            values.colors.green.total = 0
            values.colors.yellow.sorted = 0
            values.colors.yellow.total = 0
            set_balls()
        time.sleep(1)
            

class Thread(threading.Thread):
    def __init__(self, values, sql):
        threading.Thread.__init__(self)
        self.values = values
        self.sql = sql
    def run(self):
        Main(self.values, self.sql)