from player import Player

players = []


def createPlayer(name, balance):
    players.append(Player(name, balance))


def hgamble(player, amount):
    player.gamble(amount)


def game():
    if len(players) == 0:
        print("you need to create a player\n")
        name = input('Enter the name of Player\n')
        balance = input('Enter the starting amount for the Player\n')
        balance = int(balance)
        createPlayer(name, balance)

    print("1.Press 1 to gamble \n2.Press 2 to create new Player\n3.Press anything else to quit the game")

    while True:
        x = input("\nenter your choice : ")
        x = int(x)
        if x == 1:
            tries = int(
                input("How many times do you want to try to gamble? : "))
            while tries > 0:
                amount = input("\nEnter the amount to be bid: ")
                amount = int(amount)
                if players[-1].money - amount < 0:
                    print("You cannot bid this much!!\n")
                    break
                players[-1].gamble(amount)
                tries -= 1
        elif x == 2:
            name = input('\nEnter the name of Player\n')
            balance = input('Enter the starting amount for the Player\n')
            balance = int(balance)
            createPlayer(name, balance)
        else:
            break


game()
