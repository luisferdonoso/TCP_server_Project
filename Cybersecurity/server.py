import socket

# Create a socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Host address and port number
host = socket.gethostname()
port = 8000

# Bind the socket to the address and port
serversocket.bind((host, port))


#listen TCP connection 
serversocket.listen(3)

#Starting the connection

while True :
    clientsocket, address = serversocket.accept()    

    print("received connection from %s" % str(address))

    message = "Thank you for connecting to the server, this a portfolio project" + "\r\n"
    clientsocket.send(message.encode('ascii'))

    clientsocket.close()








