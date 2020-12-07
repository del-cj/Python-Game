import os

def ate_mushroom(mushroom):
    if mushroom:
        print("The magical effects of that mushroom you ate activates and you have been revived.")
        return True
    else:
        return False

def restart():
    print("Would you like to start a new game? \n [1]Yes \n [2]No")
    choice = 0
    while choice != 1 and choice != 2:
        choice = int(input("(Enter the number of the corresponding option)\n"))
    if choice == 1:
        return True
    else:
        os.system('cls')
        print("Thank you for playing!")
    running = False
    return running

def dying():
    print("You have died. \n")
    restart()

def winning():
    print("You finally arrive at the castle walls and are hastily greeted by royal guards. \nAfter a short while, the circle of guards part, and His Majesty appears before you.\n")
    os.system('pause')
    os.system('cls')

    print('"Brave Knight! \nI knew that you could do it! \nMy deepest gratitude to you for delivering the prized artifact safely. \nAs your king, I shall reward you handsomely."\n')
    os.system('pause')
    os.system('cls')

    print("Congratulations! \nYou have completed A Knight in the Woods!\n\nCreated by Carla Jane Delima and Aditi Rao\n")
    os.system('pause')
    os.system('cls')

    restart()