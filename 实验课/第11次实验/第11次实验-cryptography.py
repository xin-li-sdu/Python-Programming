import os
import cryptography
import cryptography.hazmat.primitives.ciphers.aead
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

class AESCrypto(object):
    @classmethod
    def encrypt(cls, data, mode='cbc'):
        func_name = '{}_encrypt'.format(mode)
        func = getattr(cls, func_name)
        return func(data)

    @classmethod
    def decrypt(cls, data, mode='cbc'):
        func_name = '{}_decrypt'.format(mode)
        func = getattr(cls, func_name)
        return func(data)

    @staticmethod
    def pkcs7_padding(data):
        if not isinstance(data, bytes):
            data = data.encode()

        padder = padding.PKCS7(algorithms.AES.block_size).padder()

        padded_data = padder.update(data) + padder.finalize()

        return padded_data

    @classmethod
    def encrypt_CBC(cls,key,plaintext,iv):
        if not isinstance(plaintext, bytes): #判断数据是否是字节串类型
            plaintext = plaintext.encode()

        cipher = Cipher(algorithms.AES(key),
                        modes.CBC(iv),
                        backend=default_backend())
        encryptor = cipher.encryptor()
        padded_data = encryptor.update(cls.pkcs7_padding(plaintext))
        return padded_data

    @classmethod
    def decrypt_CBC(cls, key,ciphertext,iv):
        if not isinstance(ciphertext, bytes):
            ciphertext = ciphertext.encode()

        cipher = Cipher(algorithms.AES(key),
                        modes.CBC(iv),
                        backend=default_backend())
        decryptor = cipher.decryptor()

        uppaded_data = cls.pkcs7_unpadding(decryptor.update(ciphertext))

        uppaded_data = uppaded_data.decode()
        return uppaded_data

    @staticmethod
    def pkcs7_unpadding(padded_data):
        unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
        data = unpadder.update(padded_data)
        try:
            uppadded_data = data + unpadder.finalize()
        except ValueError:
            raise Exception('无效的加密信息!')
        else:
            return uppadded_data

a=AESCrypto()
key=os.urandom(32)
iv=os.urandom(16)
plaintext=input("please enter the plaintext:")
print(a.encrypt_CBC(key, plaintext, iv))
ciphertext=a.encrypt_CBC(key, plaintext, iv)
print(a.decrypt_CBC(key, ciphertext, iv))
