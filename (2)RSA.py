from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii
keyPair=RSA.generate(1024)
pubkey=keyPair.publickey()
n=hex(pubkey.n)
e=hex(pubkey.e)
print(("Public key: "))
print(n)
print(e)
pubkeyPEM=pubkey.exportKey()
print(pubkeyPEM.decode('ascii'))
en=hex(pubkey.n)
d=hex(keyPair.d)
print(("Private key:"))
print(en)
print(d)
privkeyPEM=keyPair.exportKey()
print(privkeyPEM.decode('ascii'))
omsg='Abhinav College'
msg=b'omsg'
encryptor=PKCS1_OAEP.new(pubkey)
encrypted=encryptor.encrypt(msg)
result=binascii.hexlify(encrypted)
print("Encrypted: ",result[1:])