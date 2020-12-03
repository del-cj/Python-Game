import os

def dying():
    if ate_mushroom():
        print("The magical effects of that mushroom you ate activates and you have been revived.")
        return 50
    else:
        print("You have died. \nWould you like to start a new game? \n [1]Yes \n [2]No")
        choice = 0
        while choice < 1 or choice > 3:
            choice = int(input("(Enter the number of the corresponding option)\n"))

        if choice == 1:
            newgame()
        else:
            os.system('cls')
            print("Thank you for playing!")
    return 0    