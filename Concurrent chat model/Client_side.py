import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

while True:
    message = input("Enter message (or 'quit' to exit): ")
    if message == 'quit':
        break
    client_socket.send(message.encode('utf-8'))

    data = client_socket.recv(1024).decode('utf-8')
    if data:
        print(f'Received message: {data}')

client_socket.close()