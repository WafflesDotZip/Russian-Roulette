# Developed by AFK-Waffles on github


import time
import random
import sys




#print(bcolors.HEADER + "This is the color format" + bcolors.ENDC)



print("""\n ▄▀▀▄▀▀▀▄  ▄▀▀▀▀▄   ▄▀▀▄ ▄▀▀▄  ▄▀▀▀▀▄     ▄▀▀█▄▄▄▄  ▄▀▀▀█▀▀▄  ▄▀▀▀█▀▀▄  ▄▀▀█▄▄▄▄ 
█   █   █ █      █ █   █    █ █    █     ▐  ▄▀   ▐ █    █  ▐ █    █  ▐ ▐  ▄▀   ▐ 
▐  █▀▀█▀  █      █ ▐  █    █  ▐    █       █▄▄▄▄▄  ▐   █     ▐   █       █▄▄▄▄▄  
 ▄▀    █  ▀▄    ▄▀   █    █       █        █    ▌     █         █        █    ▌  
█     █     ▀▀▀▀      ▀▄▄▄▄▀    ▄▀▄▄▄▄▄▄▀ ▄▀▄▄▄▄    ▄▀        ▄▀        ▄▀▄▄▄▄   
▐     ▐                         █         █    ▐   █         █          █    ▐   
                                ▐         ▐        ▐         ▐          ▐        """)


print("\nRussian Roulette game • ═════════════════════ • Developed by AFK-Waffles / Waffles#6893\n")



###### 
print("""┌─┐┌─┐┌┬┐┬ ┬┌─┐
└─┐├┤  │ │ │├─┘
└─┘└─┘ ┴ └─┘┴  \n""")



######

print("• Step 1 -- How many people are playing this game?")
players = int(input(">>> ")) #players that began playing the game
alive = players #number of players currently alive


print("\n• Step 2 -- Your revolver has 6 empty chambers. How many rounds will be placed inside?\n [ value can only be within 1 - 6 ]")

rounds = int(input(">>> ")) #takes input of rounds
survival = 6 - rounds #calculates survival rate
int(rounds) #converts rounds to an integer

if rounds == 1 or rounds == 2 or rounds == 3 or rounds == 4 or rounds == 5 or rounds == 6: #not optimized but it works
    int(rounds)
    if players > 1:
        print("\n• {} rounds are placed into the cylinder.\n• There is a {} in 6 chance of survival right now.\n• {} people are playing.".format(rounds,survival,players))
    elif players == 1:
        print("\n• {} rounds are placed into the cylinder.\n• There is a {} in 6 chance of survival right now.\n• {} person is playing... interesting.".format(rounds,survival,players)) #



   
elif rounds != 1 or rounds != 2 or rounds != 3 or rounds != 4 or rounds != 5 or rounds != 6: #it works
    print("Value must be between 1 - 6. Please restart the program.")
    time.sleep(2)
    input("[ ENTER ] to end program.")
    exit()
    
time.sleep(1)
for x in range(10000): #not the best way to make a loop, but it works
    input("\n════════════════════════\n\n>>> Press [ ENTER ] to spin and pull the trigger...\n")
    
    time.sleep(0.2)
    
    print("•", end = ' ')
    
    time.sleep(0.2)
    
    print("•", end = ' ')
    time.sleep(0.2)
    
    print("•", end = ' ')
    time.sleep(0.3)
    

    chamber = random.randint(1,6)
    if alive >= 3:
        if chamber > int(rounds):
            print("\n\n         √√ - *CLICK* ... you SURVIVED. [ next player's turn ]\n") #alive
            print("• {} people are alive".format(alive))
        else:
            print("\n\n         XX - *BANG* ... you are DEAD.  [ next player's turn ]\n") #dead
            alive -= 1
            print("• {} players remain".format(alive))
        
            if int(rounds) > 1:
                int(rounds)             #I dont know why I have to convert it to an integer again but it works
                rounds -= 1
                if int(rounds) == 1:
                    print("• There is only 1 round left in the cylinder.")
                elif int(rounds) > 1:
                    print("• There are now {} rounds left in the cylinder.".format(rounds))
            else:
                print("XX - All rounds have been fired, therefore the game can no longer continue.\n• out of {} people, {} came out alive.".format(players,alive)) # can only happen if there are less rounds than actual players.
                input("\n>>> Press [ ENTER ] to end the program.")
                exit()


    elif alive == 2:
        if chamber > int(rounds):
            print("\n\n         √√ - *CLICK* ... you SURVIVED. [ next player's turn ]\n") #alive
            print("• {} people are alive".format(alive))
        else:
            print("\n\n         XX - *BANG* ... you are dead. [ other player won ].\n") #dead
            print("• one player remains alive. congratulations.")
            input("\nGame is over ... [ ENTER ]")
            exit()

    elif players == 1:
        if chamber > int(rounds):
            print("\n\n         √√ - *CLICK* ... you SURVIVED. \n") #alive
        else:
            print("\n\n         XX - *BANG* ... you are DEAD.  [ game can no longer continue ]\n") #dead
            
            input("\n>>> Press [ ENTER ] to end the program.")
            exit()
