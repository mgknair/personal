import socket

# #create an INET, STREAMing socket
# s = socket.socket(
#     socket.AF_INET, socket.SOCK_STREAM)
# #now connect to the web server on port 80
# # - the normal http port
# s.connect(("www.google.com", 80))

#create an INET, STREAMing socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#bind the socket to a public host,
# and a well-known port
#serversocket.bind((socket.gethostname(), 80))
#become a server socket
#serversocket.listen(5)

serversocket.connect(('209.172.51.58', 3306))
serversocket

print socket.getaddrinfo("www.uwaterloo.ca", 80, 0, 0, socket.IPPROTO_TCP)
print socket.getaddrinfo("www.google.com", 3306, 0, 0, socket.IPPROTO_TCP)
print socket.getaddrinfo("www.google.com", 80, 0, 0, socket.IPPROTO_TCP)

def Main():
	host = '74.15.21.201'
	port = 5000

	s = socket.socket()
	s.bind((host,port))
	s.listen(1)
	c, addr = s.accept()
	print 'Connection from: ', str(addr)

	while True:
		data = c.recv(1024)
		if not data:
			break
		print 'from connected user: ', str(data)
		data = str(data).upper()
		print 'sending: ', str(data)
		c.send(data)
	c.close()

if __name__ == '__main__':
	Main()