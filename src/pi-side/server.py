
# making a TCP server to communicate with a PC
import socket



class Server:
	def __init__(self, port):
		self.HOST = '' #RP IP address
		self.PORT = port



		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.bind((self.HOST, self.PORT))
		s.listen()
		print("Server has started")
		# once a connection is received, accepted to vars
		self.conn, self.addr = s.accept()
		s.close()
		print("Connected by", self.addr)

		# set the socket to non-blocking mode
		self.conn.setblocking(False)


	def getData(self, peek=False):
		if peek:
			try:
				data = self.conn.recv(1024,socket.MSG_PEEK)
			except BlockingIOError:
				data = False
		else:
			data = self.conn.recv(1024)
		return data
	def sendData(self, data):
		self.conn.sendmsg(data)

	def closeServer(self):
		self.conn.close()
