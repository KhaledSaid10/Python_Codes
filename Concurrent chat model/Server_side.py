import socket
import threading

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

clients = []

def handle_client(client_socket, address):
    """Handles communication with a single client."""
    while True:
        try:
            data = client_socket.recv(1024).decode('utf-8')
            if data:
                broadcast(data, client_socket)
            else:
                remove_client(client_socket)
                break
        except:
            remove_client(client_socket)
            break

def broadcast(message, client_socket):
    """Sends a message to all connected clients."""
    for client in clients:
        if client != client_socket:
            try:
                client.send(message.encode('utf-8'))
            except:
                remove_client(client)

def remove_client(client_socket):
    """Removes a client from the list and closes their socket."""
    clients.remove(client_socket)
    client_socket.close()

def start_server():
    """Starts the server and listens for connections."""
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    print(f'Server started on {HOST}:{PORT}')

    while True:
        client_socket, address = server_socket.accept()
        clients.append(client_socket)
        print(f'Client connected from {address}')
        threading.Thread(target=handle_client, args=(client_socket, address)).start()

if __name__ == '__main__':
    start_server()