import socket,struct,pickle,time,cv2,pyautogui
import numpy as np 

HOST = '0.0.0.0'
PORT = 9999

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)
client_socket, addr = server_socket.accept()

try:
    while True:
        screen = pyautogui.screenshot()
        frame = np.array(screen)
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        frame = cv2.resize(frame, (1280, 720))
        result, encoded_frame = cv2.imencode('.jpg', frame, [int(cv2.IMWRITE_JPEG_QUALITY), 70])
        data = pickle.dumps(encoded_frame)
        message_size = struct.pack("Q", len(data))
        client_socket.sendall(message_size + data)
        time.sleep(0.03)
except Exception as e:
    print(f"[-] Connection closed or interrupted: {e}")
finally:
    client_socket.close()
    server_socket.close()