import random
import numpy as np

while True:
    print("\n", "Stone-Paper-Sissor Game".center(50, '='),"\n")
    
    computer = np.random.randint(1,4,1)[0]
    print("Press 1 for Stone\nPress 2 for Paper\nPress 3 for Sissor")
    ch = int(input("Enter your choice : "))
    print(f"Computer : {computer}")
    if computer==1 and ch==2:
        print("You are Win")
    elif computer==2 and ch==3:
        print("You are Win")
    elif computer==3 and ch==1:
        print("You are Win")
    elif computer==2 and ch==1:
        print("You Loss")
    elif computer==3 and ch==2:
        print("You Loss")
    elif computer==1 and ch==3:
        print("You Loss")
    elif computer==1 and ch==1:
        print("Match Dro")
    elif computer==2 and ch==2:
        print("Match Dro")
    elif computer==3 and ch==3:
        print("Match Dro") 
    else:
        print("You Enter Invalid Value")
    

    print("\nPress 1 for play again\nPress 2 for Exit")
    n = int(input())
    if n==1:
        pass
    elif n==2:
        print("Sure You are Exit ?\nPress 1 for Yes\nPress 2 for No")
        n = int(input())
        if n==1:
            print("Game Close".center(50, '-'))
            break
        elif n==2:
            pass
        else:
            print("You Enter Invalid Value")
    else:
        print("You Enter Invalid Value")

