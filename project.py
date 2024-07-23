score=0
print("welcome to the quiz game")

print(" here we are testing your general knowledge")


# some rules
print("for 1 right answer,you got 1 point")

print("if you want to play games .enter 1 or you want to exit games enter 2 ")
while True:
    question=(input("enter number 1 0r 2  "))
    if question=="1":
          print("let start the game")
          
    else:
        exit()
        
    print("1. **Question:** Which is the smallest continent by land area?")

    print("A.Asia\nB. Australia\nC. Europe\nD. Antarctica")

    answer=(input("enter your answer a,b,c,d "))

    if answer=="b":
         score+=1

    else:
         score+=0
        
    print("2. **Question:** Who invented the telephone?")
    print("A.Thomas Edison\nB.Alexander Graham Bell\n C. Nikola Tesla\nD. Isaac Newton")

    answer=(input("enter your answer a,b,c,d "))
    
    if answer.upper()=="b":
        score+=1
            
    else:
         score+=0
        
        
    print("3. **Question:** What is the capital city of Brazil?")
    print("A. Buenos Aires\nB. Santiago\nC. Brasília\n D. Rio de Janeiro")

    answer=(input("enter your answer a,b,c,d "))
    
    if answer.upper()=="c":
         score+=1
    
    else:
         score+=0

    print("4. **Question:** Which planet is known as the \"Morning Star\" or \"Evening Star\"?")
    print("A. Venus\n B. Mars \nC. Mercury\n D. Jupiter")

    answer=(input("enter your answer a,b,c,d "))

    if answer.upper()=="a":
          score+=1
    
    else:
         score+=0
         
         
    print("5. **Question:** Who wrote the famous novel \"War and Peace\"?")
    print(" A. Leo Tolstoy\n B. Fyodor Dostoevsky \n C. Anton Chekhov\n D\n Vladimir Nabokov")   
 
    answer=(input("enter your answer a,b,c,d "))

    if answer.upper()=="a":
         score+=1
   
    else:
         score+=0
    
    print("6. **Question:** What is the chemical symbol for water?")
    print("A. H2O B. CO2 C. NaCl D.CH4")

    answer=(input("enter your answer a,b,c,d "))

    if answer.upper()=="a":
         score+=1
    
    else:
         score+=0   


    print("7. **Question:** Which of these countries is not in Africa?")
    print(" A. Nigeria\n B. Brazil\n C. Egypt\n D. South Africa")

    answer=(input("enter your answer a,b,c,d "))

    if answer=="b":
         score+=1
    
    else:
         score+=0  


    print("8. **Question:** Who painted the famous artwork \"The Starry Night\"?")
    print("A. Claude Monet \nB. Vincent van Gogh\n  C.Pablo Picasso \n D.Salvador Dalí")

    answer=(input("enter your answer a,b,c,d "))

    if answer=="b":
         score+=1
    
    else:
         score+=0  


    print("9. **Question:** Which ocean is the largest by area?")
    print("A. Atlantic Ocean\n B. Indian Ocean\n C.Arctic Ocean\n D. Pacific Ocean")

    answer=(input("enter your answer a,b,c,d "))

    if answer=="d":
         score+=1
    
    else:
         score+=0  

    print("10. **Question:** What is the largest organ in the human body?")
    print(" A. Brain\n B.Liver\n C.Skin\n D. Heart")

    answer=(input("enter your answer a,b,c,d "))

    if answer=="c":
         score+=1
    
    else:
         score+=0
         
    result= score
    print("you got",result)




