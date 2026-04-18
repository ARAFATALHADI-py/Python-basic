def add_number(num1, num2):
    result = num1 + num2
    return result

sum_result = add_number(5,3)
print(sum_result)

Parameters String
def greet(name, time_of_day):
    greeting = "Good " + time_of_day + ", " + name + "!"
    return greeting

name_value = input("Your name: ")
time_of_day_value = input("What time (morning, noon, afternoon, evening): ")

greeting_message = greet(name_value, time_of_day_value)
print(greeting_message)