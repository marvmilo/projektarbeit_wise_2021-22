from  multiprocessing import Process, Pipe
import socket, time
import select



class TCP_Server:
    def __init__(self):
        self.info = "This is the TCP Module for Roboter-Communication of Group Nö1"
        self.commandfile_path = "server_commandfile.txt"

    def server_process_function(self, pipe):
        def create_commandfile():
            with open("server_commandfile.txt", "w") as dok:
                dok.write("")
                import os
                pipe.send(os.getcwd()+"/server_commandfile.txt")
                del os
        def clear_commandfile():
            with open("server_commandfile.txt", "w") as dok:
                dok.write("")
        def read_commandfile():
            with open("server_commandfile.txt", "r") as dok:
                data = dok.read()
                clear_commandfile()
                return data
        def delete_commandfile():
            import os
            os.remove("server_commandfile.txt")
            del os
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.setblocking(0)
        self.s.bind(("", 59152))
        self.s.listen(1)
        create_commandfile()
        while True:
            conn = 0
            while not conn:
                command = read_commandfile()
                if command.startswith("stop"):
                    self.s.close()
                    delete_commandfile()
                    exit()
                try:
                    conn, addr = self.s.accept()
                except BlockingIOError:
                    pass
            print("TCP Server connected to client ---> {}".format(addr))
            while True:
                conn.setblocking(0)
                while 1:
                    try:
                        pipe.send(conn.recv(1024).decode())
                    except BlockingIOError:
                        #keine Daten über tcp abrufbar
                        pass
                    except ConnectionAbortedError:
                        print("TCP Server disconnected from client!")
                        break
                    command = read_commandfile()
                    if command.startswith("send"):
                        conn.send("\n".join(command.split("\n")[1:]).encode())
                    elif command.startswith("stop"):
                        conn.close()
                        self.s.close()
                        delete_commandfile()
                        exit()
                    time.sleep(0.1)
                conn.close()
                break
    
    def send_command(self, command):
        while not open(self.commandfile_path, "r").read() == "":
            time.sleep(0.05)
        with open(self.commandfile_path, "w") as dok:
            dok.write(command)

    def start_server_process(self):
        print("TCP Server is starting up...")
        self.parent_conn, self.child_conn = Pipe()
        self.server_process = Process(target=self.server_process_function, args=(self.child_conn,))
        self.server_process.start()
        self.commandfile_path = self.parent_conn.recv()

    def stop_server_process(self):
        print("TCP Server is stopping...")
        self.send_command("stop")
    
    def send_data(self, data):
        print("TCP Server is sending data...")
        self.send_command("send\n{}".format(data))




""" def __init__(self):
        self.p_parent, self.p_child = Pipe()
        Process(target=tcp_process_function, args=(self.p_child,)).start()
        #send_data = "Hello"
        #parent.send(send_data)

    
    def tcp_process_function(self, pipe_conn):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(("", 59152))
        s.listen(1)
        while True:
            conn, addr = s.accept()
            while True:
                data = conn.recv(1024)
                if not data:
                    conn.close()
                    break
                print("[{}] {}".format(addr[0], data.decode()))
                nachricht = input("Antwort: ")
                conn.send(nachricht.encode())
        s.close()
        #message = output_p.recv()
        sys.exit(1)
    
    def send_data(self, data):
        pipe_send.send(data)
"""