from  multiprocessing import Process, Pipe
import os, socket, time



class TCP_Server:
    def __init__(self):
        self.info = "This is the TCP Module for Roboter-Communication of Group Nö1"
        self.serverstatusfile_path = "robot/server_statusfile.txt"
        self.commandfile_path = "robot/server_commandfile.txt"
        self.xmlfile_path = "robot/server_xmlfile.xml"

    def server_process_function(self, pipe):
        def write_serverstatusfile(data=""):
            with open("robot/server_statusfile.txt", "w") as dok:
                dok.write(data)
            path = os.getcwd()+"/robot/server_statusfile.txt"
            return path
        def create_commandfile(data=""):
            with open("robot/server_commandfile.txt", "w") as dok:
                dok.write(data)
            path = os.getcwd()+"/robot/server_commandfile.txt"
            return path
        def clear_commandfile():
            with open("robot/server_commandfile.txt", "w") as dok:
                dok.write("")
        def read_commandfile():
            with open("robot/server_commandfile.txt", "r") as dok:
                data = dok.read()
                clear_commandfile()
                return data
        def delete_files():
            os.remove("robot/server_statusfile.txt")
            os.remove("robot/server_commandfile.txt")
            os.remove("robot/server_xmlfile.xml")
        def write_xmlfile(data):
            with open("robot/server_xmlfile.xml", "w") as dok:
                dok.write(data)
            path = os.getcwd()+"/robot/server_xmlfile.xml"
            return path
        
        buffer_send_data = None

        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.setblocking(0)
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.s.bind(("", 59152))
        self.s.listen(1)
        pipe.send("{}\n{}\n{}".format(write_serverstatusfile("idle"), create_commandfile(), write_xmlfile("")))
        while True:
            conn = 0
            while not conn:
                command = read_commandfile()
                if command.startswith("stop"):
                    self.s.close()
                    delete_files()
                    exit()
                try:
                    conn, addr = self.s.accept()
                except BlockingIOError:
                    pass
            print("TCP Server connected to client ---> {}".format(addr))
            write_serverstatusfile("connected {}".format(addr))
            conn.setblocking(0)
            while True:
                try:
                    recv_data = conn.recv(1024).decode()
                    print("TCP Server received data... " + recv_data)
                    write_xmlfile(recv_data)#blocking???
                    del recv_data
                except BlockingIOError:
                    #keine Daten über tcp abrufbar
                    pass
                except BrokenPipeError:
                    print("TCP Server disconnected from client!\nTrying to resend data when reconnected.")
                    write_serverstatusfile("idle")
                    break
                if not buffer_send_data == None:
                    try:
                        conn.send(buffer_send_data)
                        buffer_send_data = None
                    except:
                        print("TCP Server disconnected from client!\nTrying to resend data when reconnected.")
                        write_serverstatusfile("idle")
                        break
                command = read_commandfile()
                if command.startswith("send"):
                    buffer_send_data = command.split("\n")[1].encode()
                    try:
                        conn.send(buffer_send_data)
                        buffer_send_data = None
                    except BrokenPipeError:
                        print("TCP Server disconnected from client!\nTrying to resend data when reconnected.")
                        write_serverstatusfile("idle")
                        break
                elif command.startswith("stop"):
                    conn.close()
                    self.s.close()
                    delete_files()
                    exit()
                time.sleep(0.1)
            conn.close()
    
    def check_serverstatus(self):
        with open(self.serverstatusfile_path, "r") as dok:
            data = dok.read()
        return data

    def send_command(self, command):
        while not open(self.commandfile_path, "r").read() == "":
            time.sleep(0.05)
        with open(self.commandfile_path, "w") as dok:
            dok.write(command)

    def read_robot_xml(self):
        data = open(self.xmlfile_path, "r").read()
        open(self.xmlfile_path, "w").write("")
        return data

    def start_server_process(self):
        print("TCP Server is starting up...")
        self.parent_conn, self.child_conn = Pipe()
        self.server_process = Process(target=self.server_process_function, args=(self.child_conn,))
        self.server_process.start()
        self.serverstatusfile_path, self.commandfile_path, self.xmlfile_path = self.parent_conn.recv().split("\n")

    def stop_server_process(self):
        print("TCP Server is stopping...")
        self.send_command("stop")
    
    def send_data(self, data):
        print("TCP Server is sending data... " + data)
        self.send_command("send\n{}".format(data))
