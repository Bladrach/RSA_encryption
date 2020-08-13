# Library functions for prime 
import sympy
from math import gcd
import numpy as np
from timeit import default_timer as timer


# Büyük asal sayılar
p = sympy.randprime(2**1023, 2**1024)
q = sympy.randprime(2**1023, 2**1024)

while(p == q):
    q = sympy.randprime(2**1023, 2**1024) 

# (MOD)
n = p * q 
#print(n)

def phi(p, q):
    return (p - 1) * (q - 1)

phiN = phi(p, q)

# Public key
e = 65537  # e = 3 ya da e = 65537 seçilebiliyormuş sanırım
print(gcd(e, phiN))  # bunun 1 dönmesi lazım

# Extended Euclidean Algorithm
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    g, y, x = egcd(b % a, a)
    return (g, x - (b // a) * y, y)

# application of Extended Euclidean Algorithm to find a modular inverse
def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    return x % m

def sifrele(message, key, n):
    a = bin(key)[2:]
    C = 1
    for i in range(len(a) - 1, -1, -1):
        C = C * C % n
        if(int(a[i : i + 1]) == 1):
            C = C * message % n
    return C

def cöz(message, key, n):
    a = bin(key)[2:]
    C = 1
    counter = 0
    start = timer()
    for i in range(0, len(a)):
        C = C * C % n
        if(int(a[i : i + 1]) == 1):
            counter += 1
            C = C * message % n
    end = timer()
    elapsedTime = end - start
    return C, counter, elapsedTime

# private key
d = modinv(e, phiN)
print(pow(e * d, 1, phiN))  # 1 dönmesi lazım

# plain text (gönderilen mesaj)
M = 7
print('Gönderilen Mesaj: ' + str(M))

C = sifrele(M, e, n)
print('Şifrelenmiş Mesaj: ' + str(C))

dC, counter, elapsedTime = cöz(C, d, n)
print('Şifresi Çözülmüş Mesaj: ' + str(dC))
print('Geçen süre: {:.3f} ms'.format(elapsedTime * 1000))
print('Private keydeki 1 sayısı: ' + str(counter))
