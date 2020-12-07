import random
import combat
import os
import endgame
 
def main():

    roll = 0
    nights = 1
    apples = 0
    mushroom = False
    
    player_HP = 100

    while nights <= 9:
        print("Night " + str(nights)+"\n")
        print("HP: {}\n".format(player_HP)) 
        roll = dice_roll()
        

        if roll >= 1 and roll <= 6:
            player_HP = combat.combat_main(player_HP, apples, mushroom)
            print("\n")

        elif roll == 7:
            print("Before sleeping you found 1 apple \nDo you want to eat it? \n [1] Yes\n [2] No\n")
            choice = 0
            
            while choice != 1 and choice != 2:
                choice = int(input("(Enter the number of the corresponding option)\n"))

            if choice == 1:
                print("\nYou regain some health.\n")
                player_HP = player_HP + 10 
                if player_HP >= 100:
                    player_HP = 100
                print("HP: {}\n".format(player_HP)) 
            
            else:
                apples = apples + 1
                print("You store the apple in your bag.\n")

        elif roll == 8:
            print("Before sleeping you found 2 apples \nDo you want to eat them? \n [1] Yes\n [2] No\n")
            choice = 0
            
            while choice != 1 and choice != 2:
                choice = int(input("(Enter the number of the corresponding option)\n"))

            if choice == 1:
                print("\nYou regain some health.\n")
                player_HP = player_HP + 20 
                if player_HP >= 100:
                    player_HP = 100
                print("HP: {}\n".format(player_HP)) 
            
            else:
                apples = apples + 2
                print("You store the apples in your bag.\n")
                
        elif roll == 9:
            print("Before sleeping you found 3 apples \nDo you want to eat them? \n [1] Yes\n [2] No\n")
            choice = 0
            
            while choice != 1 and choice != 2:
                choice = int(input("(Enter the number of the corresponding option)\n"))

            if choice == 1:
                print("\nYou regain some health.\n")
                player_HP = player_HP + 30
                if player_HP >= 100:
                    player_HP = 100 
                print("HP: {}\n".format(player_HP)) 
            
            else:
                apples = apples + 3 
                print("You store the apples in your bag.\n")

        elif roll == 10:
            print("Before sleeping you found 4 apples \nDo you want to eat them? \n [1] Yes\n [2] No\n")
            choice = 0
            
            while choice != 1 and choice != 2:
                choice = int(input("(Enter the number of the corresponding option)\n"))

            if choice == 1:
                print("\nYou regain some health.\n")
                player_HP = player_HP + 40
                if player_HP >= 100:
                    player_HP = 100
                print("HP: {}\n".format(player_HP)) 
            
            else:
                apples = apples + 4
                print("You store the apples in your bag.\n")

        elif roll == 11:
            print ("Before sleeping you find an odd looking mushroom and eat it, but nothing interesting happens.\n")
            mushroom = True
             
            
        elif roll == 12:
            print ("Before sleeping you arrived at a campsite! You are able to rest soundly.")
            player_HP = 100
            print("HP: {}\n".format(player_HP))
        
        os.system('pause')
        os.system('cls')

        nights = nights + 1

        if player_HP <= 0:
            endgame.dying()
            break

    if nights == 10:
        print("Final night")
        print("HP: {}\n".format(player_HP)) 
        print ("Before sleeping you arrived at a campsite! You are able to rest soundly.")
        player_HP = 100
        print("HP: {}\n".format(player_HP))

        os.system('pause')
        os.system('cls')

        win = combat.boss_fight(apples, mushroom)

    return win

def dice_roll():
    diceRoll = random.randint(1, 12)
    return diceRoll

     
# main()
