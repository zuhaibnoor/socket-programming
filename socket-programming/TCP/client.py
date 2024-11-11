import socket
import threading


def send_message(client_socket):
    while True:
        message = input("\nEnter your message >>> ")
        client_socket.sendall(message.encode())  


def receive_message(client_socket):
    while True:
        response = client_socket.recv(1024)
        print("\nReceived message from the other client:", response.decode())


def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))  # Connecting to our server

    
    send_thread = threading.Thread(target=send_message, args=(client_socket,))
    receive_thread = threading.Thread(target=receive_message, args=(client_socket,))

    
    send_thread.start()
    receive_thread.start()

    
    send_thread.join()
    receive_thread.join()

    client_socket.close()

start_client()
