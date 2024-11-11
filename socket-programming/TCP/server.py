import socket
import threading

# Function to handle client communication
def handle_client(client_socket, client_address, other_client_socket):
    try:
        while True:
            #msg from client
            message = client_socket.recv(1024)

            
            print(f"Received from {client_address}: {message.decode()}")
            other_client_socket.sendall(message)  #sending msg to target client
    except ConnectionError:
        print(f"Connection with {client_address} closed.")
    finally:
        client_socket.close()


def start_server():
    
    #TCP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))  
    server_socket.listen(2)  

    print("<<<-----------------Server is listening for clients--------------->>>")

    # Accepting conn
    client1_socket, client1_address = server_socket.accept()
    print(f">>>----Client 1 connected from {client1_address}----<<<")
    client2_socket, client2_address = server_socket.accept()
    print(f">>>----Client 2 connected from {client2_address}----<<<")

    client1_thread = threading.Thread(target=handle_client, args=(client1_socket, client1_address, client2_socket))
    client2_thread = threading.Thread(target=handle_client, args=(client2_socket, client2_address, client1_socket))

    client1_thread.start()
    client2_thread.start()

    client1_thread.join()
    client2_thread.join()

    server_socket.close()

start_server()
