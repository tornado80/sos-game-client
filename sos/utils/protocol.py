import struct
import json
from sos.utils.mapgen import *

class Packet(dict):
    """
    Packet is used to represent a request or response. 
    It has a "command" (equivalent to URL in APIs), "data" a dictionary of data fields, and may contain "session" data.
    """
    def __init__(self, d=None):
        super().__init__()
        if d:
            for key, value in json.loads(d).items():
                self.__setitem__(key, value)

    def toJson(self) -> str:
        return json.dumps(self)

    @staticmethod
    def fromJson(js : str): 
        return Packet(js)

    def send(self, sock):
        send_msg(sock, self.toJson())

    @staticmethod
    def recv(sock):
        return Packet.fromJson(recv_msg(sock))

def encrypt(bmsg : bytes) -> bytearray:
    result = bytearray()
    for b in bmsg:
        result.append(encrypt_secret[int(b)])
    return result

def decrypt(bmsg : bytes) -> bytearray:
    result = bytearray()
    for b in bmsg:
        result.append(decrypt_secret[int(b)])
    return result

def send_msg(sock, msg : str):
    msg = encrypt(msg.encode(encoding="utf-8"))
    msg = struct.pack('>I', len(msg)) + msg
    sock.sendall(msg)

def recv_msg(sock) -> str:
    raw_msglen = recvall(sock, 4)
    if not raw_msglen:
        return None
    msglen = struct.unpack('>I', raw_msglen)[0]
    return decrypt(recvall(sock, msglen)).decode(encoding="utf-8")

def recvall(sock, n : int) -> bytearray:
    data = bytearray()
    while len(data) < n:
        packet = sock.recv(n - len(data))
        if not packet:
            return None
        data.extend(packet)
    return data
