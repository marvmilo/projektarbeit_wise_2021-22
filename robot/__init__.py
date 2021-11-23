import threading, time
from robot_tcp import TCP_Server
from robot_xml import RobotData

#main function of script
def Main(values, sql):
    if __name__ == '__main__':
        xml = RobotData()
        server = TCP_Server()
        def del_ball_values():
            values["ball"]["color"] = None
            values["ball"]["x"] = 0
            values["ball"]["y"] = 0

        def get_container_num(color):
            for x in values["colors"]:
                

        server.start_server_process()

        while 1:
            command = input("Command: ")
            if command.startswith("stop"):
                server.stop_server_process()
                break
            else:
                print("lol")
            print(server.read_robot_xml())


            if not values["ball"]["color"] == None:
                xml.set_btp_container(values["ball"]["container"])
                xml.set_btp_position(values["ball"]["x"], values["ball"]["y"], values["ball"]["z_standard"])
                server.send_data(xml.create_xml())
            
            robot_xml_data = server.read_robot_xml()
            if not robot_xml_data == "":
                xml.read_xml(robot_xml_data)



#main thread of script
class Thread(threading.Thread):
    def __init__(self, values, sql):
        threading.Thread.__init__(self)
        self.values = values
        self.sql = sql
    def run(self):
        Main(self.values, self.sql)