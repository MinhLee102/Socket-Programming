from socket import *
 
def requestServer(message: str):
    serverName = "192.168.0.101"
    serverPort = 12000
    clientSocket = socket(AF_INET, SOCK_DGRAM)

    clientSocket.sendto(message.encode(),(serverName, serverPort))
    modifiedMessage, serverAddress = clientSocket.recvfrom(8192)
    
    clientSocket.close()
    return modifiedMessage.decode()