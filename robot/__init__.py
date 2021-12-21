import threading, time
from robot.robot_tcp import TCP_Server
from robot.robot_xml import RobotData

#main function of script
def Main(values, sql):
    #if __name__ == '__main__':
    xml = RobotData()
    server = TCP_Server()
    def del_ball_values():
        values["ball"]["color"] = None
        values["ball"]["x"] = 0
        values["ball"]["y"] = 0

    def get_container_num(color):
        for x in values["colors"].keys():
            if x == color:
                #print(values["colors"][x]["container_num"])
                return int(values["colors"][x]["container_num"])
    
    def add_container(c_num):
        for x in values["colors"].keys():
            if values["colors"][x]["container_num"] == c_num:
                values["colors"][x]["sorted"] += 1
        print("Counter in Container {:5} increased by 1".format(c_num))
    
    def sum_balls_sorted():
        sum = 0
        for x in values["colors"].keys():
            sum += values["colors"][x]["sorted"]
                
    server.start_server_process(values)
    prev_movementclear = False

    while 1:
        if values["server"]["stop"]:
            server.stop_server_process()
        
        #receiving data
        robot_xml_data = server.read_robot_xml(values)
        if not robot_xml_data == "":
            #print(robot_xml_data)
            robot_dict = xml.read_xml(robot_xml_data)
            for x in robot_dict.keys():
                if x == "robot_cameraarea":
                    values["robot"]["cameraarea"] = robot_dict[x]
                if x == "robot_movementstatus":
                    values["robot"]["movementstatus"] = robot_dict[x]
                if x == "btp_isplaced":
                    add_container(robot_dict[x])
                    values.ball.prev_ball_placed = True
        
        #sending data
        if server.check_serverstatus().startswith("connected"):
            if not values["server"]["send_command"] == None:
                server.send_data(values["server"]["send_command"])

            if not values["ball"]["color"] == None and values.ball.prev_ball_placed:
                #sorting a ball
                #print(values.pretty())
                #print(values.ball)
                xml.set_btp_container(get_container_num(values["ball"]["color"]))
                xml.set_btp_position(values["ball"]["x"], values["ball"]["y"], values["ball"]["z_standard"])
                xml.set_movementclear(True)#experimental!!!
                del_ball_values()
                server.send_data(xml.create_xml())
                values.ball.prev_ball_placed = False
        
            if values["robot"]["movementclear"] != prev_movementclear:
                xml.set_movementclear(values["robot"]["movementclear"])
                prev_movementclear = values["robot"]["movementclear"]
                server.send_data(xml.create_xml())


#main thread of script
class Thread(threading.Thread):
    def __init__(self, values, sql):
        threading.Thread.__init__(self)
        self.values = values
        self.sql = sql
    def run(self):
        Main(self.values, self.sql)
