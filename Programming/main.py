import random
import math

VALUE = int(math.pow(10, 8))
def create_randoms(seed, amount):
    random.seed(seed)
    c = []
    for x in range(amount):
        x = math.ceil(random.random() * 10)
        c.append(x)
    return c

def cross_common_values(random, correct):
    equal = 0
    for i in range(len(random)):
        if random[i] == correct[i]:
            equal += 1
        else:
            return equal

    return equal

def test(seed):
    v = 8
    correct = create_randoms(seed, v)
    spreiding = {}
    for s in range(VALUE):
        x = create_randoms(s, v - 1)
        equal = cross_common_values(x, correct[0:10])
        #print(f"The seed: {s} is correct until value: {equal}")
        if equal in spreiding:
            spreiding[equal] += 1
        elif equal is len(x):
            print(f"Possible seed: {s}")
        else:
            spreiding[equal] = 1

    print(spreiding)


seed = int(random.randint(1, VALUE))
print(f"The seed is: {seed}")
test(seed)





