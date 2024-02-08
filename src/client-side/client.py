import socket

HOST = "128.61.82.221" # Raspberry Pi ip address (wired)
PORT = 12345 # whatever port used by raspi script

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.connect((HOST, PORT))
	# Send instructions
	inp = input("What you tryna send")
	while input != "huh":
		s.sendall(bytes(inp, 'utf-8'))
		print(bytes(inp, 'utf-8'))
		inp = input("What you tryna send now")