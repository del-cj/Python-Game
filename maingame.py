import pyfiglet
import os
import dicerolls
import combat
import endgame
## import all necessary files above ##

def newgame():
    ## main screen
    title_card = pyfiglet.figlet_format("A KNIGHT\n   IN THE\n  WOODS\n")
    print(title_card)
     
    os.system('pause')
    os.system('cls')

    ## intro to the game
    print("You have received a letter from The King. It reads:\n")
    print('"Brave Knight,\n\n\tHis Royal Majesty has bestowed upon you a critical retrieval mission.\nHe has recognized your past merits and trusts that you may be the only one he can send on this quest.\nThe information soon to be presented is sensitive and should not be shared with anyone who is not His Majesty or his trusted advisors.\nThere has been a research group excavating at the base of the mountain, just past the woods.\nWe have received word that they have found the artifact they were searching for; however, so did some bandits.\nHis Majesty requires you to return the artifact safely to the castle.\n\n')
    
    os.system('pause')
    os.system('cls')

    print('\t"The journey through the woods will take approximately eleven days, and we predict that you will encounter foes who wish to turn a profit with the artifact.\nThey rely on the veil of the night for ambushes, so have caution after dusk.\nHis Majesty has ordered that you are provided with the necessary equipment to traverse the woods and fend off enemies.\nYour mission is a time-sensitive matter, so be on your way."\n\n')
    os.system('pause')
    os.system('cls')

    print('\tYou are given a pack to hold your rations and a cot.\nAlso, you have weapons and armor for three fighting styles: melee, ranged, and magic.\nYou know that some fighting styles may be vulnerable against other fighting styles while also resistant to another.\n\n')
    os.system('pause')
    os.system('cls')

def main():
    running = True
    while running:
        newgame()
        if dicerolls.main():
            endgame.winning()


main() 
