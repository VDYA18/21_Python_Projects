import random

while True:
    print("welcome to the start")

    print("------------------")

    print("so, it is simple rock ,paper, scissors game")

    print("------------------")

    question=(input("if you want to play this game enter 1 and exit enter 2   "))

    print("------------------")

    if question!="1":
        exit()
        
    else:
        print("let's start")
        
        
        attempts=0
        
        max_attempts=3
        
        player=0
        
        computer=0
        
        option=["rock","paper","scissor"]
        
        
        while attempts<max_attempts:
            computer_chance=random.choice(option)
            start=(input("enter anyone rock,paper,scissor  "))
            print("----------") 
            print(f"You {start} X Computer:{computer_chance}")
            
            
            if start==computer_chance:
        
                print("----------")
                print("tie")
                
            elif(start=="rock" and computer_chance=="scissor"):
                
                print("----------")
                print("you wins")
                print("----------")
                print("you got 1 point")
                player+=1
            
            elif(start=="paper" and computer_chance=="rock"):
            
                print("----------")
                print("you wins")
                print("----------")
                print("you got 1 point")
                player+=1
                
                
            elif(start=="scissor" and computer_chance=="paper"):
                print("----------")
                print("you wins")
                print("----------")
                print("you got 1 point")
                player+=1
                
            else:
                print("computer wins")
                print("----------")
                print("computer got 1 point")
                computer+=1

            attempts+=1
            
        print(str( computer))
        print("---------------")
        print(str(player)) 
        
        if computer<player:
            print("you wins")
            print("----------")
            print("congralutions")
            
        else:
            print("computer wins")
            print("----------")
            print("better luck next time")
            
        play_again = input("Do you want to play again? Enter 1 for yes or 2 for no: ")
        print("----------------------------------")
        
        if play_again != "1":
            print("Goodbye!")
            exit()

        
        

    
    


        

        




        