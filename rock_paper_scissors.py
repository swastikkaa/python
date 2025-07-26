import random
while True:
    computer_choice=random.choice(["rock","paper","scissors"])
    yourchoice=input("enter your choice:").lower()
    if(computer_choice==yourchoice):
        print("its a draw!")
    elif(
       (computer_choice=="rock" and yourchoice=="paper") or
       (computer_choice=="paper" and yourchoice=="scissors") or
       (computer_choice=="scissors" and yourchoice=="rock")
       ):
       print("you win!!")
       print(f"computer chose:{computer_choice}")
    else:
        print("you lose:(") 
        print(f"computer chose:{computer_choice}")
    
    answer=input("do you wanna play again?(yes/no):").lower()
    if answer=="no":
         break
