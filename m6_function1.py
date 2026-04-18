def calculate_average():
    scores = [70, 85, 90, 65, 80]
    total = 0

    for score in scores:
        total += score
    
    average = total/len(scores)

    if average >= 70:
        status = "Pass"
    else:
        status = "Fail"

    print ("Average score: ", average)
    print ("Pass status: ", status)

print("Exam Score Average Calculator")


calculate_average()