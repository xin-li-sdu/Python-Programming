import random
#import eulerlib
import math
import time

# 用辗转相除求最大公因子
def gcd(a,b):
    if(a%b==0):
        return b
    else:
        return gcd(b,a%b)
    
# 欧拉函数-暴力循环版
def euler(a):
    count=0
    for i in range(1,a):
        if gcd(a,i)==1:
            count+=1
    return count

# 欧拉函数-素数版
def euler_prime(a):
    return a-1

def findModInverse(a, m): #扩展欧几里得
    if gcd(a, m) != 1:
        return None #如果a和m不互质，则不存在模逆
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3 # //是整数除法运算符
        v1 , v2, v3, u1 , u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1 , v2, v3
    return u1 % m


def rabinMiller(num): #The Rabin-Miller Primality Test
    '''
    Returns True if num is a prime number.
    num -1 = 2^{t}*s
    或者a^{s}=1 mod num
    或者存在某个i使得a^{2^{t-i}*s}=1 mod num = num-1

    '''
    s = num - 1
    t = 0
    while s % 2 == 0:
        # keep halving s while it is even (and use t to count how many times we halve s)
        s = s // 2
        t += 1

    for trials in range(5): # try to falsify num's primality 5 times
        a = random.randrange(2, num - 1)
        v = pow(a, s, num) #a^{s} mod num
        if v != 1: # this test does not apply if v is 1.
            i = 0
            while v != (num - 1): #顺便测试了一下a^{s}是否等于-1
                if i == t - 1:
                    return False
                else:
                    i = i + 1
                    v = (v ** 2) % num  #a^{2s},a^{4s},...,a^{2^{t}*s} mod num
    return True

def isPrime_rabin_miller(num):
    # Return True if num is a prime number. This function does a quicker
    # prime number check before calling rabinMiller().

    if (num < 2):
        return False # 0, 1, and negative numbers are not prime

    #print(primeSieve(1000))
    lowPrimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53,
                 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113,
                 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181,
                 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251,
                 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331,
                 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409,
                 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487,
                 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577,
                 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653,
                 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743,
                 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829,
                 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929,
                 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]

    if num in lowPrimes:
        return True
    # See if any of the low prime numbers can divide num
    for prime in lowPrimes:
        if (num % prime == 0):
            return False
    # If all else fails, call rabinMiller() to determine if num is a prime.
    return rabinMiller(num)

#生密钥  
start = time.time()  
for i in range(100): key = RSA.generate(1024)  
end = time.time()  
print('generatekey time:%d circles using %f seconds'%(100, end-start))  
# 提取私钥并存入文件  
private_key = key.export_key()   #提取私钥  
file_out = open("private_key.pem", "wb")  
file_out.write(private_key)  
file_out.close()  
# 提取公钥存入文件  
public_key = key.publickey().export_key() #提取公钥  
file_out = open("public_key.pem", "wb")  
file_out.write(public_key)  
file_out.close() 


data = b"202100460065"  
public_key = RSA.import_key(open("public_key.pem").read()) #读取公钥  
cipher = PKCS1_OAEP.new(public_key) # 实例化加密套件  
encrypted_data = cipher.encrypt(data) # 加密  
# 将加密后的内容写入到文件  
file_out = open("encrypted_data.bin", "wb")  
file_out.write(encrypted_data)  
file_out.close()  

#编写RSA加密和解密函数。
private_key = RSA.import_key(open("private_key.pem", "rb").read()) #读取私钥  
cipher = PKCS1_OAEP.new(private_key) # 实例化加密套件  
encrypted_data = open("encrypted_data.bin", "rb").read() # 读取加密内容  
data = cipher.decrypt(encrypted_data) # 解密  
print(data) 
