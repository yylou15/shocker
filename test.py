import base64
from pyDes import *

key = "d4c3b2a1"
iv = "\x01\x02\x03\x04\x05\x06\x07\x08"
cipher = des(key, CBC, iv, pad=None, padmode=PAD_PKCS5)


def encrypt(raw):
    return base64.b64encode(cipher.encrypt(raw))


def decrypt(pwd):
    return cipher.decrypt(base64.b64decode(pwd))

# raw = 'testMsg'
# print(raw)
# en = DesEncrypt(raw)
# print(en)
# de = DesDecypt(en)
# print(de)