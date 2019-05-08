# coding:utf-8
import oper

print "RSA密钥生成===================================================================="
RSAKey = oper.get_RSAKey()

print "使用公钥加密plaintext.txt输出到secret_puk.txt==================================="
oper.encryptfile('plaintext.txt', 'secret_puk.txt', RSAKey['puk'])

print "使用私钥解密secret_puk.txt输出到plaintext_puk.txt==============================="
oper.decryptfile('secret_puk.txt', 'plaintext_puk.txt', RSAKey['prk'])

print "使用私钥加密plaintext.txt输出到secret_prk.txt==================================="
oper.encryptfile('plaintext.txt', 'secret_prk.txt', RSAKey['prk'])

print "使用公钥解密secret_prk.txt输出到plaintext_prk.txt==============================="
oper.decryptfile('secret_prk.txt', 'plaintext_prk.txt', RSAKey['puk'])
