import socket
import cv2
import numpy as np

def start_server():
    # UDP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    
    server_socket.bind(('localhost', 12345))
    
    print("Server is listening for video frames...")
    
    while True:
        # Received img data
        frame_data, client_addr = server_socket.recvfrom(65507)
        
        #data->image
        nparr = np.frombuffer(frame_data, np.uint8)
        frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        
        if frame is not None:
            
            cv2.imshow("Server Video", frame)
        
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    server_socket.close()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    start_server()
