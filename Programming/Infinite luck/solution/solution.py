import random
from pwn import *


#IP = "127.0.0.1"
IP = "108.143.241.81"
PORT = 65432

numbers = []
attempt = {}


def solve_game(n, depth):
    if depth >= n:
        return
    if depth not in attempt:
        attempt[depth] = 1
    else:
        attempt[depth] = attempt[depth] + 1
    connection = remote(IP, PORT)
    for i in range(depth):
        connection.sendlineafter(b">", f"{numbers[i]}".encode())

    print(f"Guessing value: {attempt[depth]}")
    connection.sendlineafter(b">", f"{attempt[depth]}".encode())
    response = connection.recvall(timeout=0.2).decode('utf-8')
    print(response)
    if "Nice" in response:
        numbers.append(attempt[depth])
        print(f"The number on depth: {depth} is {numbers[depth]}")
        solve_game(n, depth + 1)
    elif "Sorry" in response:
        return solve_game(n, depth)
    else:
        connection.interactive()
    return connection


def plausable_seed(numbers, seed):
    random.seed(seed)
    for i in range(len(numbers)):
        x = random.randint(1, 10)
        if x != numbers[i]:
            return False
    return True


def guess_seed(numbers):
    seed = 0
    while True:
        if plausable_seed(numbers, seed):
            return seed
        else:
            seed += 1



LIMIT = int(math.pow(10, 6))
c = solve_game(10, 0)

#numbers = [10, 7, 3, 6, 6, 4, 3, 1, 4, 1]
print(numbers)
print("Bruteforce the seed....")
seed = guess_seed(numbers)
print(f"Found the seed: {seed}")

connection = remote(IP, PORT)
random.seed(seed)
i = 0
while i < 1000:
    number = random.randint(1, 10)
    connection.sendlineafter(b">", f"{number}".encode())
    response = connection.recvline().decode('utf-8')
    print(response)
    print(i)
    if "next round!!" not in response:
        print("exiting")
        break
    i += 1

connection.interactive()
connection.sendlineafter(b"#>", f"{seed}".encode())
response = connection.recvall(timeout=0.2).decode('utf-8')
print(response)
connection.interactive()
