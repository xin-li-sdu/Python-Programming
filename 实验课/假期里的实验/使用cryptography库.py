#pip install cryptography
import time
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding as sym_padding

_TIMEFLAG_ = True

key = os.urandom(32) #AES128->16, AES192->24, AES256->32
iv = os.urandom(16)
cipher = Cipher(algorithms.AES(key), modes.CBC(iv)) #AES-CBC
encryptor = cipher.encryptor()
ct = encryptor.update(b"1 secret message")
ct += encryptor.update(b"2 secret message")
ct += encryptor.finalize()
print("密文为:",ct)
decryptor = cipher.decryptor()
pt = decryptor.update(ct) + decryptor.finalize()
print("解密后的明文为:",pt)

#update_info的使用
# the buffer needs to be at least len(data) + n - 1 where n is cipher/mode block size in bytes
cipher = Cipher(algorithms.AES(key), modes.CBC(iv)) #AES-CBC
encryptor = cipher.encryptor()
buf = bytearray(33)
len_encrypted = encryptor.update_into(b"a secret message", buf)
print("len_encrypted: ",len_encrypted)
# get the ciphertext from the buffer reading only the bytes written to it (len_encrypted)
ct = bytes(buf[:len_encrypted]) + encryptor.finalize()
print("密文为:",ct)
decryptor = cipher.decryptor()
len_decrypted = decryptor.update_into(ct, buf)
# get the plaintext from the buffer reading only the bytes written (len_decrypted)
pt = bytes(buf[:len_decrypted]) + decryptor.finalize()
print("解密后的明文为:",pt)
#=============================   AES-CBC   ==============================
def encrypt_CBC(key, plaintext, iv): #key, plaintext, iv:byte
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    encryptor = cipher.encryptor()
    #PKCS7填充,缺N个就补N个chr(N)
    padder = sym_padding.PKCS7(128).padder()
    padded_data = padder.update(plaintext)
    padded_data += padder.finalize()
    ct = encryptor.update(padded_data) + encryptor.finalize()
    return ct

def decrypt_CBC(key, ciphertext, iv): #key, ciphertext, iv:byte
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    decryptor = cipher.decryptor()
    padded_data = decryptor.update(ciphertext) + decryptor.finalize()
    unpadder = sym_padding.PKCS7(128).unpadder()
    pt = unpadder.update(padded_data)
    pt += unpadder.finalize()
    return pt

if _TIMEFLAG_:
    print("\n=============  测试AESCBC加密速度 ===========\n")
    plaintxt = b"0123456789"*128
    #print("plaintxt:", plaintxt)
    cnt = 10000
    start = time.time()
    for i in range(cnt):
        ciphertext = encrypt_CBC(
            key,
            plaintxt,
            iv
        )
    end =  time.time()
    print("加密 {} 次，use time {} 秒:".format(cnt, end - start))
    print("\n")
    start = time.time()
    for i in range(cnt):
        tmp  = decrypt_CBC(
            key,
            ciphertext,
            iv
        )
    end =  time.time()
    print("解密 {} 次，use time {} 秒:".format(cnt, end - start))
    print("\n")

else:
    ciphertext = encrypt_CBC(
            key,
            b"It's a secret",
            iv
        )
    print("encrypt_CBC 加密后的密文为:",ciphertext)
    print("decrypt_CBC 解密后的明文为:",decrypt_CBC(
        key,
        ciphertext,
        iv
    ))

#=============================   AES-GCM   ==============================
#AES-GCM示例，GCM=GMAC+CTR。 CTR和GCM模式都不需要填充
#GCM是认证加密模式中的一种，能同时确保数据的保密性、完整性及真实性
#输入密钥、明文、附加信息
#输出结果为IV(计数器CTR的初始值)、密文、身份验证标签(MAC值)
def encrypt_GCM(key, plaintext, associated_data):
    # Generate a random 96-bit IV.
    iv = os.urandom(12)

    # Construct an AES-GCM Cipher object with the given key and a
    # randomly generated IV.
    encryptor = Cipher(
        algorithms.AES(key),
        modes.GCM(iv),
    ).encryptor()

    # associated_data will be authenticated but not encrypted,
    # it must also be passed in on decryption.
    encryptor.authenticate_additional_data(associated_data)

    # Encrypt the plaintext and get the associated ciphertext.
    # GCM does not require padding.
    ciphertext = encryptor.update(plaintext) + encryptor.finalize()

    return (iv, ciphertext, encryptor.tag)

#解密。输入密钥，辅助信息，IV，密文，MAC值
#输出明文
def decrypt_GCM(key, associated_data, iv, ciphertext, tag):
    # Construct a Cipher object, with the key, iv, and additionally the
    # GCM tag used for authenticating the message.
    decryptor = Cipher(
        algorithms.AES(key),
        modes.GCM(iv, tag),
    ).decryptor()

    # We put associated_data back in or the tag will fail to verify
    # when we finalize the decryptor.
    decryptor.authenticate_additional_data(associated_data)

    # Decryption gets us the authenticated plaintext.
    # If the tag does not match an InvalidTag exception will be raised.
    return decryptor.update(ciphertext) + decryptor.finalize()

iv, ciphertext, tag = encrypt_GCM(
    key,
    b"a secret message!GCM",
    b"authenticated but not encrypted payload"
)
print("encrypt_GCM 加密后的密文为:",ciphertext)
print("decrypt_GCM 解密后的明文为:",decrypt_GCM(
    key,
    b"authenticated but not encrypted payload",
    iv,
    ciphertext,
    tag
))
#====================  RSA  ========================
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding as asym_padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import utils
from cryptography.exceptions import InvalidSignature

private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)
pripem = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    #encryption_algorithm=serialization.NoEncryption()
    encryption_algorithm=serialization.BestAvailableEncryption(b'mypassword') 
)
public_key = private_key.public_key()
pubpem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)
#RSA-OAEP加解密
message = b"encrypted data"
ciphertext = public_key.encrypt(
    message,
    asym_padding.OAEP(
        mgf=asym_padding.MGF1(algorithm=hashes.SHA256()), #2048bit RSA 加密256字节倍数长度明文
        algorithm=hashes.SHA256(),
        label=None
    )
)
print("RSA-OAEP加密后密文：",ciphertext)
plaintext = private_key.decrypt(
    ciphertext,
    asym_padding.OAEP(
        mgf=asym_padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)
print("RSA-OAEP解密后明文：",plaintext)

#签名验签
chosen_hash = hashes.SHA256()
hasher = hashes.Hash(chosen_hash)
message = b"data & more data"
##hasher.update(b"data & ")
##hasher.update(b"more data")
hasher.update(message)
digest = hasher.finalize()

sig = private_key.sign(
        digest,
        asym_padding.PSS(
            mgf=asym_padding.MGF1(hashes.SHA256()),
            salt_length=asym_padding.PSS.MAX_LENGTH
        ),
        utils.Prehashed(chosen_hash)
)
try:
    public_key.verify(
            sig,
            message,
            asym_padding.PSS(
                mgf=asym_padding.MGF1(hashes.SHA256()),
                salt_length=asym_padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
    )
except InvalidSignature as e:
    print("invalid signature")
else:
    print("valid signature")
