from Crypto.Cipher import ChaCha20
from Crypto.Random import get_random_bytes
import codecs


m = b"Cha Cha real smooth"
flag = b'test'
key = get_random_bytes(32)
cipher = ChaCha20.new(key=key)

ciphertext1 = cipher.encrypt(m)
ciphertext2 = cipher.encrypt(flag)

# c1 = p1 ^ k
# c2 = p2 ^ k
# c2 ^ c1 = p1 ^ p2 ^ p2 = p1 

print(ciphertext1.hex())
print(ciphertext2.hex())


def xor(v1, v2):
    return bytes([a ^ b for (a, b) in zip(v1, v2)])


enc_msg = ciphertext1.hex()
enc_flag = ciphertext2.hex()

bmsg = codecs.decode(enc_msg, 'hex_codec')
bflag = codecs.decode(enc_flag, 'hex_codec')

print(xor(xor(bflag, bmsg), m))