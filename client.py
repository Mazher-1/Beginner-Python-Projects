import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ("localhost",8080)
client_socket.connect(server_address)

message="Hello Server !"
client_socket.send(message.encode('utf-8'))

response= client_socket.recv(1024)
print(f"Recieve from server: {response.decode('utf-8')}")

client_socket.close()
