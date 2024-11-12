# encoding:utf-8
#pip uninstall crypto pycryptodome
#pip install pycryptodome
#关闭代理

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad
from Crypto import Random
import base64


#CBC
key=b'12345678901234561234567890123456'
iv=bytearray(16)
print(len(iv))
cipher=AES.new(key,AES.MODE_CBC,iv)

text=b'secret text11111111111111111secret text11111111111111111secret text11111111111111111secret text11111111111111111'
padtext=pad(text,16,style='pkcs7')
cipherText=cipher.encrypt(padtext)
cipherText = base64.b64encode(cipherText)
print(padtext)
print(cipherText)

#bs = AES.block_size
#print((bs))
#iv = Random.new().read(bs)

cipherText= base64.b64decode(cipherText)
decrypter=AES.new(key,AES.MODE_CBC,iv)
plaintext=decrypter.decrypt(cipherText)
unpadtext=unpad(plaintext,16,'pkcs7')
print(plaintext)
print(unpadtext)


#ECB
key=b'12345678901234561234567890123456'
cipher=AES.new(key,AES.MODE_ECB)

text=b'secret text11111111111111111secret text11111111111111111secret text11111111111111111secret text11111111111111111'
cipherText=cipher.encrypt(text)
cipherText = base64.b64encode(cipherText)
print(text)
print(cipherText)



cipherText= base64.b64decode(cipherText)
decrypter=AES.new(key,AES.MODE_ECB)
plaintext=decrypter.decrypt(cipherText)
print(plaintext)
