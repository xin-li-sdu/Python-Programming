from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import time#生密钥
start = time.time()
for i in range(100): key = RSA.generate(1024)
end = time.time()
print('generatekey time:%d circles using %f seconds'%(100, end-start))# 提取私钥并存入文件
private_key = key.export_key() #提取私钥
file_out = open("private_key.pem", "wb")
file_out.write(private_key)
file_out.close()# 提取公钥存入文件
public_key = key.publickey().export_key() #提取公钥
file_out = open("public_key.pem", "wb")
file_out.write(public_key)
file_out.close()
#加密
data = b"123456"
public_key = RSA.import_key(open("public_key.pem").read()) #读取公钥
cipher = PKCS1_OAEP.new(public_key) # 实例化加密套件
encrypted_data = cipher.encrypt(data)# 加密
# 将加密后的内容写入到文件
file_out = open("encrypted_data.bin", "wb")
file_out.write(encrypted_data)
file_out.close()
#解密
private_key = RSA.import_key(open("private_key.pem", "rb").read()) #读取私钥
cipher = PKCS1_OAEP.new(private_key) # 实例化加密套件
encrypted_data = open("encrypted_data.bin", "rb").read() # 读取加密内容
data = cipher.decrypt(encrypted_data)# 解密
print(data)
