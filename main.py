input("Do you want to play Who Wants to Be a Millionaire? \n")

print("Question #1. $500")

question_1 = input("What sort of animal is Walt Disney's Dumbo? \n")

if (question_1.lower() == "elephant"):
  print("correct")

  print("Question #2. $1,000")
  question_2 = input("What was the name of the Spanish waiter in the TV sitcom \"Fawlty Towers\"? \n")

  if (question_2.lower() == "manuel"):
    print("correct")

    print("Question #3. $2,000")
    question_3 = input("Which battles took place between the Royal Houses of York and Lancaster? \n")

    if (question_3.lower() == "war of the roses"):
      print("correct")

      
      print("Question #4. $5,000")
      question_4 = input("Which former Beatle narrated the TV adventures of Thomas the Tank Engine? \n")

      if (question_4.lower() == "ringo starr"):
        print("correct")

        question_5 = input("Queen Anne was the daughter of which English Monarch? (hint: The monarch is ____ the second. You need to put name II for it to be counted. For example: Elizibeth II)")
        if (question_5.lower() == "James II"):
          print("corect")

          
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