# 参考: https://qiita.com/akakou/items/e9fbcfc0c69cc957152e

from socket import socket, AF_INET, SOCK_DGRAM
def send_udp(addr, port, msg):
    s = socket(AF_INET, SOCK_DGRAM)
    # Broadcastする場合は以下をコメントアウト
    # s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

    s.sendto(msg, (addr, port))
    s.close()