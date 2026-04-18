# def check_guess():
#     global score
#     still_guessing = True
#     attempt = 0
    
#     while still_guessing and attempt < 3:
#         guess = input("Guess: ")
#         if guess.lower() == answer.lower():
#             print("Correct answer!")
#             score += 1 
#             still_guessing = False
        
#         else:
#             if attempt < 2:
#                 print("Wrong answer!")
#             attempt += 1

# score = 0
# print("Guess the country!")

# print("By size, what is the largest country in the world?")
# answer = "Russia"
# check_guess()

# print("Wich country has a unicorn as its national animal?")
# answer = "Scotland"

# print("In wich country would find the currency Bath")
# answer = "Thailand"
# check_guess()

questions = {
    #questions : answer
    "By size, what is the largest country in the world": "Russia",
    "Wich country has a unicorn as its national animal?": "Scotland",
    "In wich country would you find the current Bath?": "Thailand"

}

def check_guess():
    global score
    still_guessing = True
    attempt = 0

    for question, answer in questions.items():
        print(question)
        while still_guessing and attempt < 3:
            guess = input("Guess: ")
            if guess.lower() == answer.lower():
                print("Correct answer!")
                score += 1
                still_guessing = False
            else:
                if attempt < 2:
                    print("Wrong Answer!")
                attempt += 1

        still_guessing = True
        attempt = 0
score = 0 
print("Guess the Country!")
check_guess()
print("Your score is " + str(score))
