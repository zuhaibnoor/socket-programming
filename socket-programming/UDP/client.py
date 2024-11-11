import socket
import cv2
import numpy as np

def send_in_chunks(client_socket, data, server_address, chunk_size=65507):
    
    for i in range(0, len(data), chunk_size):
        chunk = data[i:i + chunk_size]
        client_socket.sendto(chunk, server_address)

def start_client():
    #UDP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    
    server_address = ('localhost', 12345)

    
    cap = cv2.VideoCapture(0)  

    while True:
        ret, frame = cap.read()
        
        
        
        frame_resized = cv2.resize(frame, (640, 480)) 

        
        _, encoded_frame = cv2.imencode('.jpg', frame_resized)
        
        
        send_in_chunks(client_socket, encoded_frame.tobytes(), server_address)

        #showing vid on client side
        cv2.imshow("Client Video", frame_resized)

        # Exit the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    client_socket.close()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    start_client()
