from Crypto.Hash import SHA256
from Crypto.Cipher import DES
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad
from Crypto.Random import get_random_bytes

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

import time

h = SHA256.SHA256Hash('abcdefg'.encode())
print(h.hexdigest())

des_encrypt_decrypt = DES.new(b'ShanDong', DES.MODE_ECB) #key='Shandong'
p = 'Beautiful is better than ugly.'
pp = p.encode() #变为字节码
#按8字节对齐，如PKCS7标准打补丁，缺几补几个数字几。
#c = des_encrypt_decrypt.encrypt(pp.ljust((len(pp)//8+1)*8, '0'.encode()))
pptmp = pad(pp, DES.block_size)
print("pptmp = ",pptmp)
c = des_encrypt_decrypt.encrypt(pptmp)
print("cipher:", c)
cp = des_encrypt_decrypt.decrypt(c)
print("plain:",unpad(cp, DES.block_size).decode()) #cp[0:len(pp)].decode())


'''AES'''
# 要加密的内容
data = b"123456"
# 随机生成16字节（即128位）的加密密钥
key = get_random_bytes(16)
iv = get_random_bytes(16)
# 实例化加密套件，使用CBC模式
cipher = AES.new(key, AES.MODE_CBC, iv)
# 对内容进行加密，pad函数用于分组和填充
encrypted_data = cipher.encrypt(pad(data, AES.block_size))
print(encrypted_data)

cipher = AES.new(key, AES.MODE_CBC, iv)
tmp = cipher.decrypt(encrypted_data)
data = unpad(tmp, AES.block_size)
print(data)

'''RSA'''
#生密钥
print("Begin generating rsa keys....")
start = time.time()
for i in range(100):
    key = RSA.generate(1024)
end = time.time()
print('generatekey time:%d circles using %f seconds'%(100, end-start))

# 提取私钥并存入文件
private_key = key.export_key()
file_out = open("private_key.pem", "wb")
file_out.write(private_key)
file_out.close()

# 提取公钥存入文件
public_key = key.publickey().export_key()
file_out = open("public_key.pem", "wb")
file_out.write(public_key)
file_out.close()

#加密
# 要加密的内容
data = b"123456"
# 从文件中读取公钥
public_key = RSA.import_key(open("public_key.pem").read())
# 实例化加密套件
cipher = PKCS1_OAEP.new(public_key)
# 加密
encrypted_data = cipher.encrypt(data)

# 将加密后的内容写入到文件
file_out = open("encrypted_data.bin", "wb")
file_out.write(encrypted_data)
file_out.close()

#解密
# 从私钥文件中读取私钥
private_key = RSA.import_key(open("private_key.pem", "rb").read())
# 实例化加密套件
cipher = PKCS1_OAEP.new(private_key)
# 从文件中读取加密内容
encrypted_data = open("encrypted_data.bin", "rb").read()
# 解密
data = cipher.decrypt(encrypted_data)
print(data)
