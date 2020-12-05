import pyfiglet
import os
## import all necessary files above ##

def newgame():
    ## main screen
    title_card = pyfiglet.figlet_format("A KNIGHT\n    IN THE\n   WOODS\n")
    print(title_card)
    
    key_press = " "
    while len(key_press) > 0:
        key_press = str(input("(Press ENTER to continue)"))
        os.system('cls')

    ## intro to the game
    print("You have received a letter from The King. It reads:")
    print('"Brave Knight,\n \tHis Royal Majesty has bestowed upon you a critical retrieval mission. He has recognized your past merits and trusts that you may be the only one he can send on this quest. The information soon to be presented is sensitive and should not be shared with anyone who is not His Majesty or his trusted advisors. There has been a research group excavating at the base of the mountain, just past the woods. We have received word that they have found the artifact they were searching for; however, so did some bandits. His Majesty requires you to return the artifact safely to the castle.')

newgame() 
