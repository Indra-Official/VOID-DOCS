import socket
import threading

def listen(port):
    s = socket.socket()
    s.bind(("0.0.0.0", port))
    s.listen(5)
    while True:
        conn, addr = s.accept()
        print(f"Connected by {addr}")
        # Handle incoming datal
        conn.close()

def connect(ip, port):
    s = socket.socket()
    s.connect((ip, port))
    s.sendall(b"Hello, peer!")
    s.close()

threading.Thread(target=listen, args=(5000,)).start()
# Later, connect to another peer:
# connect("peer_ip_address", 5000)
