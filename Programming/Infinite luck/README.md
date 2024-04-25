# Challenge

infinite luck [medium]

## Description

I've made a casino like game, you get the flag if you can guess the value 1000 times in a row.  
You would need infinite luck to beat this challenge. Unless you think you can beat the house....

## Solutions

The problem with the game is that the random number generator is seed based. So everytime a player tries the game they get the same sequence.
There are two ways from here to solve this challenge. You can go for a local or remote brute force attack. 

For the local attack you guess x values and brute force the seed. For the remote attack you just keep guessing the values. 
I opted for the local attack since it's way less noisy. It looks to the administrator that a player is just activly playing the game. Lets say you need the first 10 digets to bruteforce the seed that gives 225 requests + the 1000 requests to solve the CTF; In total 1225 requests 10ms per request --> 12,25 seconds. 

The seed is in range 1/ 1 000 000. Lets say you generate 5 numbers per seed on average. that means you have to generate 5 million numbers. Someone has posted that they can generate 1 million random numbers in 0.9 seconds. That means in 5 seconds you could have the seed. Total time would take ~20 seconds. 

The remote attack is way less time efficient. The attacker has to try 5 times on average to guess the number. They have to do that 1000 times and each time they have to send the n previous numbers this gives an avg request amount of $\sum_{n=1}^1000 5n$. That gives 2497500 requests, lets say each request takes 10ms. That would give us about 7 hours of completion time. 

Possible, but not so nice in a CTF. 


Solution: 
```python
import random

from pwn import *

IP = "127.0.0.1"
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
    if "next round!!" not in response:
        print("exiting")
        break
    i += 1

connection.sendlineafter(b"#>", f"{seed}".encode())
response = connection.recvall(timeout=0.2).decode('utf-8')
print(response)
connection.interactive()
```

## flag 
ctf{s33ds_4r3_us3l3ss!}
