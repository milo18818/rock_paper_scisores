from random import randint
RCPscore = 0
pcscore = 0

print("select gamemode")
gametype = input()
if gametype == ("s"):
    print("special powers enabled")
print("best of ___")
round = input()
for x in range (int(round)):
    player = input("pick: rock (R), paper (P), scisores (S)")
    player = player.lower()
    print(player,"vs", end=" ")
    chosen = randint(1,3)
    computer = 0
    if (chosen == 1):
        computer = "r"
    elif(chosen == 2):
        computer = "p"
    else:
        if(chosen == 3):
            computer = "s"
    print (computer)

    if player == computer:
        print("draw")
    elif(player == "r" and computer == "s"):
        print("player wins")
        RCPscore += 1
    elif(player == "r" and computer == "p"):
        print("computer wins")
        pcscore += 1
    elif(player == "p" and computer == "r"):
        print("player wins")
        RCPscore += 1
    elif(player == "p" and computer == "s"):
        print("computer wins")
        pcscore += + 1
    elif(player == "s" and computer == "p"):
        print("player wins")
        RCPscore += 1
    elif(player == "s" and computer == "r"):
        print("computer wins")
        pcscore += 1
    elif(player == "g"):
        print("player wins")
        RCPscore += 1
    else:
        if player == "p" and computer == "s":
          print("computer wins")

    if gametype == ("s"):
        if player == "d" and computer == "r":
            print("test")
            pcscore -= 1
        if player == "d" and computer == "p":
            print("test")
            pcscore -= 1
        if player == "d" and computer == "s":
            print("test")
            pcscore -= 1
        if player == "b" and computer == "r":
            print("blocked")
        if player == "b" and computer == "p":
            print("blocked")
        if player == "b" and computer == "s":
            print("blocked")
print("your score is " + str(RCPscore) + " the computers score is " + str(pcscore))
if RCPscore > pcscore:
    print("!PLAYER WINS!")
elif RCPscore < pcscore:
    print("!COMPUTER WINS!")
else:
    print("!DRAW!")