import socket
from pymongo import MongoClient
from dontcommit import MongoDB
import threading
import time

def Listen(bin="0.0.0.0"):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((bin, 12345))
    server.listen(1)
    conn, addr = server.accept()
    data = conn.recv(1024)
    conn.close()
    return [addr,data]

def  Send(ip,msg):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((ip, 12345))
    client.sendall(msg.encode('utf-8'))
    client.close()

def Add_Peer_List(ip):
    client = MongoClient(MongoDB)
    db = client["VOID-Docs"]
    Active_Peers = db["Active_Peers"]
    Peers = Active_Peers.find_one({"Peer": ip})

    if Peers == None:
        Active_Peers.insert_one({"Peer": ip})
        return "Peer Added."
    else:
        return "Peer already listed."
    
def Remove_Peer_List(ip):
    client = MongoClient(MongoDB)
    db = client["VOID-Docs"]
    Active_Peers = db["Active_Peers"]
    Peers = Active_Peers.find_one({"Peer": ip})

    if Peers != None:
        Active_Peers.delete_one({"Peer": ip})
        return "Peer Removed."
    else:
        return "Peer not listed."

def Discover_New_Peers():
    while True:
        dax = Listen()
        ip , data = dax[0] , dax[1] 
        time.sleep(1)
        print(ip)
        if data == "Add_Me" and ip not in current_connected_peers :
            current_connected_peers += [ip]
            Send(ip,"Added_You")

def Remove_Offline_Peers(current_connected_peers):
    while True:
        for i in current_connected_peers:
            dax = Send(i,"Online_Check")
            dab = Listen(i)
            time.sleep(1)
            if dab != "Add_Me":
                current_connected_peers.remove(i)

def Run():
    current_connected_peers = []

    Adder = threading.Thread(target = Discover_New_Peers)
    Remover = threading.Thread(target = Remove_Offline_Peers,args=(current_connected_peers,))
    Adder.start()
    Remover.start()

thread = threading.Thread(target=Run)
thread.start()