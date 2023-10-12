import socket

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server_socket.bind(("0.0.0.0",8080))

server_socket.listen(5)
print("Server is listening on Port 8080 ...")

client_socket , client_address = server_socket.accept()
print(f"Accept connection from {client_address}")

data= client_socket.recv(1024)
print(f"Received: {data.decode('utf-8')}")

response ="Hello world"
client_socket.send(response.encode('utf-8'))


client_socket.close()
server_socket.close()

