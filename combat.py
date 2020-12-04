import random
import os
import endgame

fighting_styles = {1:"melee", 2:"range", 3:"magic"}
vulernable_to = {1:2,2:3,3:1}
resistant_to = {1:3,2:1,3:2}
enemy_types = {1:"A knight", 2:"An archer", 3:"A wizard"}



def picking_style():
    print("Choose your fighting style:\n [1] Melee\n [2] Range\n [3] Magic")

    player_style = 0

    while player_style < 1 or player_style > 3:
        player_style = int(input("(Enter the number of the corresponding style)\n"))
    
    os.system('cls')
    return player_style

def dealing_damage(attacker, defender):
    if defender == vulernable_to.get(attacker):
        multiplier = 2
    elif defender == resistant_to.get(attacker):
        multiplier = 0.5
    else: 
        multiplier = 1
    
    base = 10
    damage = int(base * multiplier)

    return damage

def combat_main():
    player_HP = 100  ## to be changed when put all together for main
    enemy_HP = 100
    enemy_style = random.randint(1,3)
    print("{} has appeared out of the darkness.".format(enemy_types.get(enemy_style)))
    mushroom = True
    apples = 0

    player_style = picking_style()

    round = 1
    while player_HP > 0 or enemy_HP > 0:
        print("Round {}".format(round))

        if round % 2 == 0:  ## enemy's turn
            damage = dealing_damage(enemy_style, player_style)
            print("The enemy deals {} damage to you.".format(damage))
            player_HP = player_HP - damage
            round = round + 1
            if player_HP <= 0:
                if endgame.ate_mushroom(mushroom):
                    player_HP = 50
                    mushroom = False
                else:
                    endgame.dying()
                    break
        
        else: ## player's turn
            print("HP: {}\t Enemy HP: {}\t Fighting style: {}".format(player_HP, enemy_HP, fighting_styles.get(player_style).capitalize()))
            print("What would you like to do this round?\n [1] Attack\n [2] Eat an apple\n [3] Change fighting style")
            round_action = 0
            while round_action < 1 or round_action > 3:
                round_action = int(input("(Enter the number of the corresponding option)\n"))
            os.system('cls')
            
            if round_action == 1:  ## attacking
                damage = dealing_damage(player_style, enemy_style)
                print("Round {}\nYou deal {} damage to the enemy.".format(round,damage))
                enemy_HP = enemy_HP - damage
                round = round + 1
                if enemy_HP <= 0:
                    print("You have successfully defeated the enemy!")
                    return player_HP
            elif round_action == 2: ## healing
                print("Apples: {}".format(apples))
                if apples > 0:
                    print("You ate an apple and it restores some health.\n")
                    player_HP += 10
                    round += 1
                else:
                    print("You do not have any apples. Choose another option.\n")
            else:  ## changing fighting style
                player_style = picking_style()
                round = round + 1
                os.system('cls')

combat_main()