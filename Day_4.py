import random

print("Do you want to play stone paper scissor?")
while True:
    p=int(input("Input \"1\" for \"stone\"\n\"2\" for \"paper\"\n\"3\" for \"scissor\""))    
    if(p==1):
        c="stone"
    elif(p==2):
        c="paper"
    elif(p==3):
        c="scissor"
    else:
        print("Choose correct option!")
        continue
    p1=random.randint(1,3)
    if(p1==1):
        c1="stone"
    elif(p==2):
        c="paper"
    elif(p==3):
        c1="scissor"
    print(f"You choose {c}! \nComputer choose {c1}!")
    if(p==p1):
        print(f"You both choose {c}! Its a tie!")
    elif((p-p1)==1):
        print(f"{c} beats {c1}! You won!")
    elif((p1-p)==1):
        print(f"{c1} beats {c}! Computer won!")
    elif((p-p1)==2):
        print(f"{c1} beats {c}! Computer won!")
    elif((p1-p)==2):
        print(f"{c} beats {c1}! You won!")
    s=input("do you want to continue")
    if(s=="no"):
        break