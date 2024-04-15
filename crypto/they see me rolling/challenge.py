from vernamcipher.cryptographic import Cryptographic
import random

FLAG = "ctf{they_see_me_rolling_over_the_encryption_key}"
random.seed(2570334840819712139117301843868267838046992)
N = 0


def generate_random():
    global N
    N += 1
    return random.randint(0, (1 << 145) - 1)


def main():
    print(f"N: {N}")
    value = input()
    expected_value = str(generate_random())
    expected_value_encrypted = Cryptographic.exclusive_operations(expected_value, FLAG)
    print(expected_value + ' ----> ' + expected_value_encrypted)
    if value == expected_value_encrypted:
        print("Opening the gate")
    else:
        print("closing the gate")

if __name__ == "__main__":
    main()
