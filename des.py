import base64
from pyDes import *

iv = "\x01\x02\x03\x04\x05\x06\x07\x08"


def encrypt(raw):
    en_cipher = des("d4c3b2a1", CBC, iv, pad=None, padmode=PAD_PKCS5)
    return base64.b64encode(en_cipher.encrypt(raw))


def decryptReq(pwd):
    de_cipher = des("d4c3b2a1", CBC, iv, pad=None, padmode=PAD_PKCS5)
    return de_cipher.decrypt(base64.b64decode(pwd))


def decrypt(pwd):
    de_cipher = des("12345678", CBC, iv, pad=None, padmode=PAD_PKCS5)
    return de_cipher.decrypt(base64.b64decode(pwd))
