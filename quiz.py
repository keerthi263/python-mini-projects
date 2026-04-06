#quiz
#by using simple if else statement and for loop

questions=("What is the capital of India?",
           "Which is the largest planet in our solar system? ",
           "What is the national animal of India?",
           "What do honeybees do to communicate the location of a food source?")
options=(("A.New delhi", "B.Nepal", "C.Assam", "D.Chandigarh"),
         ("A.Mercury", "B.Jupiter", "C.Venus", "D.Mars"),
         ("A.Lion", "B.Tiger", "C.Elephant", "D.Monkey"),
         ("A.Waggle", "B.Classical", "C.Folk", "D.None"))
answers=("A","B","B","A")
guesses=[]
score=0
question_num=0
for question in questions:
    print("------------------------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    guess=input("enter ur answer:").upper()
    guesses.append(guess)
    if guess==answers[question_num]:
        score+=1
        print("CORRCT!!!")
    else:
        print("INCORRECT!!!")
        print(f"{answers[question_num]}is the correct answer")
    question_num+=1

print("-----------------------------------------")
print("          RESULT       ")
print("-----------------------------------------")

print("answers:",end="")
for answer in answers:
    print(answer,end="")
print("\n")

print("guesses:",end="")
for guess in guesses:
    print(guess,end="")
print("\n")

score=int(score/len(questions)*100)
print(f"your score is:{score}%c")

