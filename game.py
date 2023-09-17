import random


def didplayerwin(name, amount):
    one = random.choice([1, 2, 3])
    two = random.choice([1, 2, 3])
    three = random.choice([1, 2, 3])

    if (one == two and two == three):

        print(f"Congrats {name} you won {amount}")
    else:
        return False
