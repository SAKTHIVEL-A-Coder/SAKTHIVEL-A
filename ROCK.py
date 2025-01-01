import random
print("THIS MY ROCK PAPER SCISSORS GAME DO YOU WANT TO PLAY IT")
print("*******************************************************")
#RULES CAN BE FOLLWED BY THE PARTICIPENTS
print("___IT IS RULES___")
print("0===rock")
print("1===paper")
print("2===scissors")
print("IT SOME TIMES IT DOES NOT WORK PROPERLY")
#input function
MY_turn=int(input("What is your choose?,enter {0} for ROCK and {1} for PAPER and {2} for SCISSORS: "))
SYSTEM_turn=random.randint(0,2)
print(f'Sysyem choose :{SYSTEM_turn}')
#conditions
if(MY_turn==0 and SYSTEM_turn==2):
    print("YOU WILL WIN")
elif(SYSTEM_turn>MY_turn):
    print("SYSTEMS WILL  WINS")
elif(SYSTEM_turn==MY_turn):
    print("The match was drawn")
else:
    print("YOU ENTERD A INVALID NUMBER")
