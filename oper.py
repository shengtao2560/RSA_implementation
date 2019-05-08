import gmpy2
import random
from gmpy2 import mpz


def get_RSAKey():
    RSAKey = {}
    prime_arr = []
    while len(prime_arr) < 2:
        num = random.randint(pow(10, 100), pow(10, 101))
        prime_num = gmpy2.next_prime(num)
        if prime_num not in prime_arr:
            prime_arr.append(prime_num)
    p, q = prime_arr[0], prime_arr[1]
    n = p * q
    s = (p - 1) * (q - 1)
    e = 30109
    d = gmpy2.invert(e, s)
    print "p =", p
    print "q =", q
    print "n =", n
    print "e =", e
    print "d =", d
    print "s =", s
    puk = [n, e]
    prk = [n, d]
    RSAKey['puk'] = puk
    RSAKey['prk'] = prk
    return RSAKey


def encrypt(message, key):
    return gmpy2.powmod(message, key[1], key[0])


def decrypt(secret, key):
    return gmpy2.powmod(secret, key[1], key[0])


def char2num(string):
    num = ''
    for char in string:
        if char.isdigit():
            num = num + '0' + char
        elif ord(char) > 96:
            num = num + str(ord(char) - 87)
        else:
            num = num + str(ord(char) - 29)

    return int(num)


def num2char(num, endflag):
    numlist = []
    if len(str(num)) == 4:
        numlist.append(int(str(num)[0:2]))
        numlist.append(int(str(num)[2:4]))
    elif len(str(num)) == 3:
        numlist.append(int(str(num)[0]))
        numlist.append(int(str(num)[1:3]))
    elif num == 0 and not endflag:
        numlist.append(0)
        numlist.append(0)
    else:
        numlist.append(int(num))

    char = ''
    for ch in numlist:
        if ch >= 36:
            char = char + chr(ch + 29)
        elif ch >= 10:
            char = char + chr(ch + 87)
        else:
            char = char + str(ch)

    return char


def encryptfile(inputfile, outputfile, key):
    with open(inputfile, 'r') as f:
        plaintext = f.read()

    text = ''.join(c for c in plaintext if c.isalnum())

    with open(outputfile, 'w') as s:
        for i in range(0, len(text), 2):
            num = char2num(text[i:i + 2])
            secret = encrypt(num, key)
            s.write(str(secret) + '\t')


def decryptfile(inputfile, outputfile, key):
    with open(inputfile, 'r') as s:
        list = s.read().split('\t')
    list = list[0:len(list) - 1]

    decryption = ''
    for sec in list:
        if sec == list[-1]:
            decryption = decryption + num2char(decrypt(mpz(sec), key), True)
        else:
            decryption = decryption + num2char(decrypt(mpz(sec), key), False)

    print decryption

    with open(outputfile, 'w') as f:
        f.write(decryption)
