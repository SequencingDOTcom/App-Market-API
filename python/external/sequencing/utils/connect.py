import base64
import urllib
import hashlib
import json

from Crypto.Cipher import AES
from external.sequencing.config import SequencingEndpoints


class AESCipher:
    def __init__(self, key, iv):
        self.key = key[:32]
        self.iv = iv[:16]

    __pad = lambda self,s: s + (AES.block_size - len(s) % AES.block_size) * chr(AES.block_size - len(s) % AES.block_size)
    __unpad = lambda self,s: s[0:-ord(s[-1])]

    def encrypt(self, raw):
        raw = self.__pad(raw)
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        return base64.b64encode(cipher.encrypt(raw))

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        return self.__unpad(cipher.decrypt(enc).decode("utf-8"))


def get_connect_to_link(data , url=SequencingEndpoints.connect_to):
    password = data['client_id'];
    cipher = AESCipher(password, '3n3CrwwnzMqxOssv')
    payload = json.dumps(data)
    enc_str = cipher.encrypt(payload)
    get_vars = {
        'c': hashlib.md5(password).hexdigest(),
        'json': urllib.quote(enc_str.encode('utf-8'))
    }

    return url + urllib.urlencode(get_vars)
