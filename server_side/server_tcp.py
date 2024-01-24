import socket

HOST = ""
PORT = 5005

sock_sv = socket.socket(socket.AF_INET)
sock_sv.bind((HOST, PORT))
sock_sv.listen()

# クライアントの接続受付
sock_cl, addr = sock_sv.accept()

while True:
    # データ受信
    data = sock_cl.recv(1024)
    print(data.decode("utf-8"))
