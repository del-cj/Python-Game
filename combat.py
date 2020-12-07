import random
import os
import endgame

fighting_styles = {1:"melee", 2:"ranged", 3:"magic"}
vulernable_to = {1:2,2:3,3:1}
resistant_to = {1:3,2:1,3:2}
enemy_types = {1:"a knight", 2:"an archer", 3:"a wizard"}



def picking_style():
    print("Choose your fighting style:\n [1] Melee\n [2] Ranged\n [3] Magic")

    player_style = 0

    while player_style != 1 and player_style != 2 and player_style != 3:
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

def combat_main(player_HP, apples, mushroom,):

    enemy_HP = 100
    enemy_style = random.randint(1,3)
    enemy_type = enemy_types.get(enemy_style)
    print("{} has appeared out of the darkness.".format(enemy_type.capitalize()))

    player_style = picking_style()

    round = 1
    while player_HP > 0 or enemy_HP > 0:
        print("\nRound {}".format(round))

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
                    return player_HP
        
        else: ## player's turn
            print("HP: {}\t Enemy HP: {}\t Fighting style: {}".format(player_HP, enemy_HP, fighting_styles.get(player_style).capitalize()))
            print("What would you like to do this round?\n [1] Attack\n [2] Eat an apple\n [3] Change fighting style")
            round_action = 0
            while round_action != 1 and round_action != 2 and round_action != 3:
                round_action = int(input("(Enter the number of the corresponding option)\n"))
            os.system('cls')
            
            if round_action == 1:  ## attacking
                damage = dealing_damage(player_style, enemy_style)
                print("Round {}\nYou deal {} damage to the enemy.".format(round,damage))
                enemy_HP = enemy_HP - damage
                round = round + 1
                if enemy_HP <= 0:
                    print("\nYou have successfully defeated the enemy!")
                    return player_HP
            
            elif round_action == 2: ## healing
                print("Apples: {}".format(apples))
                if apples > 0:
                    print("You ate an apple and it restores some health.\n")
                    player_HP += 10
                    apples -= 1
                    round += 1
                else:
                    print("You do not have any apples. Choose another option.\n")
            else:  ## changing fighting style
                player_style = picking_style()
                round = round + 1
                os.system('cls')

def boss_fight(apples, mushroom):

    player_HP = 100
    enemy_HP = 250
    boss_turn = 0
    enemy_style = random.randint(1,3)
    enemy_type = enemy_types.get(enemy_style)
    print("Your sleep is suddenly interrupted and you find yourself surrounded by all sorts of bandits.\n")
    print("{} steps forward and tries to attack.".format(enemy_type.capitalize()))

    player_style = picking_style()

    round = 1
    while player_HP > 0 or enemy_HP > 0:
        print("\nRound {}".format(round))

        if round % 2 == 0:  ## enemy's turn
            damage = dealing_damage(enemy_style, player_style)
            print("The enemy deals {} damage to you.".format(damage))
            player_HP = player_HP - damage
            round = round + 1
            boss_turn+=1
            if boss_turn == 3:
                enemy_style = random.randint(1,3)
                print("The enemy falls back into the crowd and {} steps forward.".format(enemy_types.get(enemy_style)))
                boss_turn = 0
            if player_HP <= 0:
                if endgame.ate_mushroom(mushroom):
                    player_HP = 50
                    mushroom = False
                else:
                    return player_HP

        else: ## player's turn
            print("HP: {}\t Enemy HP: {}\t Fighting style: {}".format(player_HP, enemy_HP, fighting_styles.get(player_style).capitalize()))
            print("What would you like to do this round?\n [1] Attack\n [2] Eat an apple\n [3] Change fighting style")
            round_action = 0
            while round_action != 1 and round_action != 2 and round_action != 3:
                round_action = int(input("(Enter the number of the corresponding option)\n"))
            os.system('cls')
            
            if round_action == 1:  ## attacking
                damage = dealing_damage(player_style, enemy_style)
                print("Round {}\nYou deal {} damage to the enemy.".format(round,damage))
                enemy_HP = enemy_HP - damage
                round = round + 1
                if enemy_HP <= 0:
                    print("\nYou have successfully defeated the final enemies!\n")
                    return True
            
            elif round_action == 2: ## healing
                print("Apples: {}".format(apples))
                if apples > 0:
                    print("You ate an apple and it restores some health.\n")
                    player_HP += 10
                    apples -= 1
                    round += 1
                else:
                    print("You do not have any apples. Choose another option.\n")
            else:  ## changing fighting style
                player_style = picking_style()
                round = round + 1
                os.system('cls')


##combat_main()
# apples = 0
# mushroom = False
# boss_fight(apples, mushroom)