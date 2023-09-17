import random


def didplayerwin(name, amount):
    one = random.choice([1, 2, 3])
    two = random.choice([1, 2, 3])
    three = random.choice([1, 2, 3])
    reward = 0
    if one == two == three:
        reward = one * amount
        print(f"Congrats {name} you won {reward}")
        return reward
    else:
        print(f"Sorry you lost..{name}")
        return -1
