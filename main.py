input("Do you want to play Who Wants to Be a Millionaire? \n")

print("To answer type the corect option. For example you would type A")

print("Question #1. $500")

print("A. Deer \n B. Rabit \n C. Elephant \n D. Donkey")
question_1 = input("What sort of animal is Walt Disney's Dumbo? \n")

if (question_1.lower() == "c"):
  print("correct")

  print("Question #2. $1,000")
  print("A. Manuel \n B. Pedro \n C. Alfonso \n D. Javier")
  question_2 = input("What was the name of the Spanish waiter in the TV sitcom \"Fawlty Towers\"? \n")

  if (question_2.lower() == "a"):
    print("correct")

    print("Question #3. $2,000")
    print("A. Thirty Years War \n B. Hundred Years war \n C. War of the Roses \n D. English Cival war")
    question_3 = input("Which battles took place between the Royal Houses of York and Lancaster? \n")

    if (question_3.lower() == "c"):
      print("correct")

      print("Question #4. $3,000")
      print("A. John Lennon \n B. Paul McCartney \n C. George Harrrison \n D. Ringo Starr")
      question_4 = input("Which former Beatle narrated the TV adventures of Thomas the Tank Engine? \n")

      if (question_4.lower() == "d"):
        print("correct")
        
        print("Question #5. $5,000")
        print("A. James II \n Henry VII \n C. Victoria \n D. William I")
        question_5 = input("Queen Anne was the daughter of which English Monarch?")
        if (question_5.lower() == "a"):
          print("corect")

          print("Question #6. $7,000")
          print("A. Irving Berlin \n B. George Gershwin \n C. Aaron Copland \n D. Cole Porter")
          question_6 = input("who composed \"rhapsody in blue\"? \n")
          if (question_6.lower() == "b"):
            print("correct")

            print("Question #7. $10,000")
            print("A. 15 \n B. 20 \n C. 25 \n D. 30")
            question_7 = input("What is the Celsius equivalent of 77 degrees Fahrenheit?")

            if (question_7.lower() == "c"):
              print("correct")

              print("Question #8. $20,000")
              print("A. Carriage \n B. Wrestling Style \n C. Cocktail \n D. Horse")
              question_8 = input("Suffolk Punch and Hackney are types of what?")

              if (question_8.lower() == "d"):
                print("correct")
                
                print("Question #9. $30,000")
                print("A. Hamlet \n B. Bacbeth \n C. Othello \n D. The Merchent of Venice")
                question_9 = input("Which Shakespeare play features the line \"Neither a borrower nor a lender be\"? \n")

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