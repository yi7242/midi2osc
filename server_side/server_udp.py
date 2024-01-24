# 参考: https://qiita.com/akakou/items/e9fbcfc0c69cc957152e
from socket import socket, AF_INET, SOCK_DGRAM

HOST = ''
PORT = 5005

# ソケットを用意
s = socket(AF_INET, SOCK_DGRAM)
# バインドしておく
s.bind((HOST, PORT))
try:
    while True:
        msg, address = s.recvfrom(8192)
        print(f"message: {msg}\nfrom: {address}")
except KeyboardInterrupt:
    s.close()
    print('close')
