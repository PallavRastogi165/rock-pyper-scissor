import random
import os
import time

def cls():
    os.system("CLS")

print("LETS PLAY ROCK PAPER SCISSOR!")
print("INSTRUCTIONS:-\nTYPE  -'R' FOR ROCK,\n      -'P' FOR PAPER,\n      -'S' FOR SCISSOR ")
userscr = 0
aiscr = 0
gcnt = 0
listchoice = ["R", "P", "S", "P", "R", "S", "P", "S", "R"]
while 1:
    gcnt += 1
    print("\n-------------\n  ROUND -", gcnt, "\n-------------")
    userchoice = input("ENTER YOU CHOICE, (R , P , S) \n").upper()
    cls()
    aichoice = random.choice(listchoice)

    if userchoice == "R":
        userpr_choice = "ROCK"
    if userchoice == "P":
        userpr_choice = "PAPER"
    if userchoice == "S":
        userpr_choice = "SCISSOR"

    if aichoice == "R":
        aipr_choice = "ROCK"
    if aichoice == "P":
        aipr_choice = "PAPER"
    if aichoice == "S":
        aipr_choice = "SCISSOR"
    if userchoice != "S" and userchoice != "P" and userchoice != "R":
        print("ERROR --- PLEASE ENTER A VALID CHOICE")
        
#        --------------------------------------------------------------------------------------------------------

    if userchoice == aichoice:
        print(f"\nYOU CHOOSE {userpr_choice}  AND\nAI CHOOSE {aipr_choice}\n")
        print("IT'S A DRAW")
    elif userchoice == "R":
        if aichoice == "P":
            print(f"\nYOU CHOOSE {userpr_choice}  AND\nAI CHOOSE {aipr_choice}\n")
            print("YOU LOST THIS ROUND!")
            aiscr += 1

        elif aichoice == "S":
            print(f"\nYOU CHOOSE {userpr_choice}  AND\nAI CHOOSE {aipr_choice}\n")
            print("YOU WON THIS ROUND!")
            userscr += 1

    elif userchoice == "P":
        if aichoice == "S":
            print(f"\nYOU CHOOSE {userpr_choice}  AND\nAI CHOOSE {aipr_choice}\n")
            print("YOU LOST THIS ROUND!")
            aiscr += 1

        elif aichoice == "R":
            print(f"\nYOU CHOOSE {userpr_choice}  AND\nAI CHOOSE {aipr_choice}\n")
            print("YOU WON THIS ROUND!")
            userscr += 1

    elif userchoice == "S":
        if aichoice == "R":
            print(f"\nYOU CHOOSE {userpr_choice}  AND\nAI CHOOSE {aipr_choice}\n")
            print("YOU LOST THIS ROUND!")
            aiscr += 1

        elif aichoice == "P":
            print(f"\nYOU CHOOSE {userpr_choice}  AND\nAI CHOOSE {aipr_choice}\n")
            print("YOU WON THIS ROUND!")
            userscr += 1
    else:
        print("PLEASE ENTER A VALID CHOICE")
    
    print(f"YOUR SCORE = {userscr}\nAI's SCORE = {aiscr}")
    time.sleep(2)
    cls()
    if gcnt == 10:
        break
    else:
        continue


print("TOTAL DRAWS = ", 10 - (aiscr + userscr))

print()
if userscr > aiscr:
    print("CONGRATULATION !! YOU WON")
elif userscr == aiscr:
    print("GAME ENDED IN A DRAW")
else:
    print("BETTER LUCK NEXT TIME")


exitkey = input("PRESS ENTER TO EXIT\n")
