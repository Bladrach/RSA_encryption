# Library functions for prime 
import sympy
from math import gcd
import numpy as np


# Büyük asal sayılar
p = sympy.randprime(2**1023, 2**1024)
q = sympy.randprime(2**1023, 2**1024)

while(p == q):
    q = sympy.randprime(2**1023, 2**1024) 

print(len(bin(p)))
print(len(bin(q)))

# (MOD)
n = p * q 
print(len(bin(n)))

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

# private key
d = modinv(e, phiN)
print(pow(e * d, 1, phiN))  # 1 dönmesi lazım

# plain text (gönderilen mesaj)
M = input("Lütfen bir mesaj giriniz:\n")
print('Gönderilen Mesaj: ' + str(M))

numbers = []
C = []
i = 0
if(isinstance(M, str)):
    for letter in M:
        number = ord(letter)
        numbers.append(number)
        C.append(pow(numbers[i], e, n))
        i+=1

print('Şifrelenmiş Mesaj: ' + str(C))

# şifre çözme
chars = []
dC = []
if(isinstance(C, list)):

    for i in range(len(C)):
        dC.append(pow(C[i], d, n))
        chars.append(chr(dC[i]))

        solved = ''.join([str(elem) for elem in chars])

print('Şifresi Çözülmüş Mesaj: ' + str(solved))

def bitCount(int_no):
    c = 0
    while(int_no):
        int_no &= (int_no - 1)
        c += 1
    return c

print('Private anahtarın içerdiği 1 sayısı: ' + str(bitCount(d)))
