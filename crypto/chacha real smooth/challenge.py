from Crypto.Cipher import ChaCha20
from Crypto.Random import get_random_bytes

m = "chacha real smooth"
flag = 'ctf{temp flag}'
key = get_random_bytes(32)
cipher = ChaCha20.new(key=key)

ciphertext1 = cipher.encrypt(m)
ciphertext2 = cipher.encrypt(flag)

# c1 = p1 ^ k
# c2 = p2 ^ k
# c2 ^ c1 = p1 ^ p2 ^ p2 = p1 

print(ciphertext1)
print(ciphertext2)

