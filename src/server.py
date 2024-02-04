
# making a TCP server to communicate with a PC
import socket



class Server:
	def __init__(self, port):
		self.HOST = '' #RP IP address
		self.PORT = port



		with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
			s.bind((HOST, PORT))
			s.listen()
			print("Server has started")
			# once a connection is received, accepted to vars
			self.conn, self.addr = s.accept()
		with conn:
			print("Connected by", addr)
	def getData(self):
		data = self.conn.recv(1024)
		if not data:
			return False
	def sendData(self, data):
		self.conn.sendmsg(data)
