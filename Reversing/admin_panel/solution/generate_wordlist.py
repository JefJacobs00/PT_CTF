import math
import hashlib
import random


wordlist = []


file = open("wordlist.txt", "w")
str = ""
halfway = False
for i in range(1716391755, 1716478184):
    random.seed(i)
    str += f"{random.randint(math.pow(10,8), math.pow(10,9))}\n"
    

print("writing wordlist")
file.write(str)
