# 参考: https://qiita.com/akakou/items/e9fbcfc0c69cc957152e
from socket import socket, AF_INET, SOCK_DGRAM
from connection_mode import Connection_Mode

HOST = ''
PORT = 5005
MODE = Connection_Mode.TCP

if MODE == Connection_Mode.UDP:
    s = socket(AF_INET, SOCK_DGRAM)
    s.bind((HOST, PORT))
    while True:
        msg, address = s.recvfrom(4096)
        print(f"message: {msg}\nfrom: {address}")
elif MODE == Connection_Mode.TCP:
    sock_sv = socket(AF_INET)
    sock_sv.bind((HOST, PORT))
    sock_sv.listen()

    # クライアントの接続受付
    sock_cl, addr = sock_sv.accept()

    while True:
        data = sock_cl.recv(1024)
        print(data)
else:
    raise Exception("Invalid Connection Mode")
