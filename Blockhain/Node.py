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

def Send(ip,msg):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((ip, 12345))
    client.sendall(msg.encode('utf-8'))
    client.close()

def Get_Peer():
    client = MongoClient(MongoDB)
    db = client["VOID-Docs"]
    Active_Peers = db["Active_Peers"]
    Available_Peers = Active_Peers.find_one()

    for i in Available_Peers:
        print(i)

def First_Connect(ip):
    while True:
        b = Listen(ip)
        a = Send(ip,"Addme")
        time.sleep(1)
        if b[1] == "Added you":
            break
        else:
            continue

def Stay_Connected(ip):
    while True:
        b = Listen(ip)
        time.sleep(1)
        if b[1] == "Online_Check":
            Send("Addme")
        else:
            continue

def Run(ip):
    First_Connect(ip)
    thread = threading.Thread(target=Stay_Connected, args=(ip))
    thread.start()


ip_input = input("Enter IP :")
thread = threading.Thread(target=Run, args=(ip_input))
thread.start()