from random import randint
RCPscore = 0
pcscore = 0
for x in range(3):
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
        (chosen == 3)
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
        (player == "p" and computer == "s")
        print("computer wins")
print("your score is " + str(RCPscore) + " the computers score is " + str(pcscore))
if RCPscore > pcscore:
    print("player wins")
elif RCPscore < pcscore:
    print("computer wins")
else:
    print("draw")