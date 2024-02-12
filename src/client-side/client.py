import socket


class Client:
    def __init__(self, host, port):
        self.HOST = host # should be Raspberry pi ip address, "128.61.82.221"
        self.PORT = port # whatever port the raspi script uses

        # connects to specified host and port
        try:
            self.sckt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sckt.connect((self.HOST, self.PORT))
            print("connected")
        except:
            self.sckt = False
            print("Connection failed")
        



    def send_data(self, data):
        if self.sckt:
            return self.sckt.sendall(bytes(data))
        else:
            return False

    def receive_data(self):
        # check if there is data to be received first, then return it
        try:
            self.sckt.recv(1024, socket.MSG_PEEK)
            # make sure the data is used up (peek doesn't)
            return self.sckt.recv(1024)
        except:
            return False
