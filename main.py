input("Do you want to play Who Wants to Be a Millionaire? \n")

print("To answer type the corect option. For example you would type A")

print("Question #1. $500")

question_1 = input("What sort of animal is Walt Disney's Dumbo? \n A. Deer \n B. Rabit \n C. Elephant \n D. Donkey \n")

if (question_1.lower() == "c"):
  print("correct")

  print("Question #2. $1,000")
  question_2 = input("What was the name of the Spanish waiter in the TV sitcom \"Fawlty Towers\"? \n A. Manuel \n B. Pedro \n C. Alfonso \n D. Javier \n")

  if (question_2.lower() == "a"):
    print("correct")

    print("Question #3. $2,000")
    question_3 = input("Which battles took place between the Royal Houses of York and Lancaster? \n A. Thirty Years War \n B. Hundred Years war \n C. War of the Roses \n D. English Cival war \n")

    if (question_3.lower() == "c"):
      print("correct")

      print("Question #4. $3,000")
      question_4 = input("Which former Beatle narrated the TV adventures of Thomas the Tank Engine? \n A. John Lennon \n B. Paul McCartney \n C. George Harrrison \n D. Ringo Starr \n")

      if (question_4.lower() == "d"):
        print("correct")
        
        print("Question #5. $5,000")
        question_5 = input("Queen Anne was the daughter of which English Monarch? \n A. James II \n Henry VII \n C. Victoria \n D. William I \n")
        if (question_5.lower() == "a"):
          print("corect")

          print("Question #6. $7,000")
          question_6 = input("who composed \"rhapsody in blue\"? \n A. Irving Berlin \n B. George Gershwin \n C. Aaron Copland \n D. Cole Porter \n")
          if (question_6.lower() == "b"):
            print("correct")

            print("Question #7. $10,000")
            question_7 = input("What is the Celsius equivalent of 77 degrees Fahrenheit? \n A. 15 \n B. 20 \n C. 25 \n D. 30 \n")

            if (question_7.lower() == "c"):
              print("correct")

              print("Question #8. $20,000")
              question_8 = input("Suffolk Punch and Hackney are types of what? \n A. Carriage \n B. Wrestling Style \n C. Cocktail \n D. Horse \n")

              if (question_8.lower() == "d"):
                print("correct")
                
                print("Question #9. $30,000")
                question_9 = input("Which Shakespeare play features the line \"Neither a borrower nor a lender be\"? \n A. Hamlet \n B. Bacbeth \n C. Othello \n D. The Merchent of Venice \n")

                if (question_9.lower() == "a"):
                  print("correct")

                  print("Question #10. $50,000")
                else:
                  print("Sorry that is not right. Run this program agian to play agian.")  
              else:
                print("Sorry that is not right. Run this program agian to play agian.")
            else:
              print("Sorry that is not right. Run this program agian to play agian.")
          else:
            print("Sorry that is not right. Run this program agian to play agian.")
        else:
          print("Sorry that is not right. Run this program agian to play agian.")
      else:
        print("Sorry that is not right. Run this program agian to play agian.")
    else:
      print("Sorry that is not right. Run this program agian to play agian.")
  else:
     print("Sorry that is not right. Run this program agian to play agian.")
else:
  print("Sorry that is not right. Run this program agian to play agian.")