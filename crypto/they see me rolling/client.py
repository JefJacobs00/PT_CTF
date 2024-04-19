from vernamcipher.cryptographic import Cryptographic
import random

FLAG = "ctf{FAKE KEY}" # <--- secret key

secret_seed = 123 # <-- secret seed
random.seed(secret_seed)

def generate_nth(n):
    for i in range(n + 1):
        min_value = 10 ** (len(FLAG) - 1)  # Minimum value with n digits
        max_value = (10 ** len(FLAG)) - 1  # Maximum value with n digits
        r = random.randint(min_value, max_value)
        if i == n:
            return str(r)


def encrypt(data, key):
    return Cryptographic.exclusive_operations(data, key)


def button_press(N):
    random_value = generate_nth(N)
    return encrypt(random_value, FLAG)


if __name__ == "__main__":
    N = input()
    button_press(N)





