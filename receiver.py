import socket,struct,pickle,cv2

SENDER_IP = ''#target ip address 
PORT = 9999

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SENDER_IP, PORT))
print("[*] Successfully connected to screen share.")
data = b""
payload_size = struct.calcsize("Q")
try:
    while True:
        while len(data) < payload_size:
            packet = client_socket.recv(4096)
            if not packet: break
            data += packet
        if not data:
            break
        packed_msg_size = data[:payload_size]
        data = data[payload_size:]
        msg_size = struct.unpack("Q", packed_msg_size)[0]
        while len(data) < msg_size:
            data += client_socket.recv(4096)
        frame_data = data[:msg_size]
        data = data[msg_size:]
        encoded_frame = pickle.loads(frame_data)
        frame = cv2.imdecode(encoded_frame, cv2.IMREAD_COLOR)
        cv2.imshow("Live Python Screen Share", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
except Exception as e:
    print(f"[-] Disconnected from stream: {e}")
finally:
    cv2.destroyAllWindows()
    client_socket.close()
