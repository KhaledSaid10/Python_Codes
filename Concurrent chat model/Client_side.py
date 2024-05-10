import socket

# Function to handle sending and receiving messages from the server
def client_function():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 9999))
    
    while True:
        # Send a message to the server
        message = input("Enter your message: ")
        client.send(message.encode('utf-8'))
        
        # Receive a response from the server
        response = client.recv(4096)
        print(f"Server response: {response.decode('utf-8')}")

if __name__ == "__main__":
    client_function()
