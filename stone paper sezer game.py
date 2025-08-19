import random
computer= random.choice([1,2,3])

gameCharacters={"stone":1,"paper":2,"sezer":3}
reversedict={1:"stone",2:"paper",3:"sezer"}

while True:
    user= input("enter your choice: \n 1.stone\n2.paper\n3.sezer\n4.exit\n")
    if(user=="stone" or user=="paper" or user=="sezer"):
        print("hii")
    else:
            print("you entered a unvalid input !")
    if user =="exit":
        print("thanks for playing")
        break

    user_choose = gameCharacters[user]
    computer_choose= reversedict[computer]
    
    print(f"you entered:{user}")
    print(f"computer choose:{computer_choose}")

    if(user_choose== 1 and computer == 3):
     print("you win!")
    elif(user_choose==2 and computer ==2):
         print("it's a  draw !")
    elif(user_choose==2 and computer ==3):
         print("you loose bro")
    elif(user_choose==3 and computer == 3):
         print("it's a draw!")
    elif(user_choose== 1 and computer == 1):
         print("it's a draw!")
    elif(user_choose==3 and computer ==2):
         print("you win !")
    elif(user_choose==1 and computer ==2):
         print("you loose bro")
    elif(user_choose==1 and computer == 3):
         print("you win!")
    elif(user_choose==2 and computer ==1):
         print("you are amazing bro!")
    elif(user_choose==3 and computer == 1):
         print("you loose bro")



except Exception as e:
        print("⚠️ Something went wrong, but the game will continue.")
        continue  # Optional: remove this if you want to stop on real errors