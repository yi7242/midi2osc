# 参考: https://qiita.com/akakou/items/e9fbcfcc0c69cc957152e

from socket import socket, AF_INET, SOCK_DGRAM,SOCK_STREAM, SOL_SOCKET, SO_BROADCAST
from connection_mode import Connection_Mode

class Sender:
    def __init__(self, addr, port, mode):
        self.addr = addr
        self.port = port
        self.mode = mode
        if mode == Connection_Mode.UDP:
            self.s = socket(AF_INET, SOCK_DGRAM)
        elif mode == Connection_Mode.TCP:
            self.s = socket(AF_INET, SOCK_STREAM)
            self.s.connect((self.addr, self.port))
        else:
            raise Exception("Invalid Connection_Mode")

    def __del__(self):
        self.s.close()

    def send(self, msg):
        if self.mode == Connection_Mode.UDP:
            self.s.sendto(msg, (self.addr, self.port))
        elif self.mode == Connection_Mode.TCP:
            self.s.send(msg)