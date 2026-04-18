fruits = ["Apple", "Mango", "Banana", "Orange"]
fruits.append("Grapes")
fruits.append("Melon")
fruits.insert(2, "Pineapple")
fruits.remove("Apple")
fruits.remove("Orange")
fruits.sort()
print(fruits)

exam_score = [75, 50, 80, 45, 65, 90, 100]
exam_score.sort()
print("Score lowest to hightest : ",exam_score )

remidial = exam_score[0:3] # Index 0--3
passed = exam_score[3:]
print("Remidial score : " + str(remidial))
print("Passed score :" + str(passed))   

song = {
    'Tittle' : "All of me",
    "Singer" : "John Legend",
    "Release" : 2013
}
print(song["Tittle"])

song.update({"genre" : "R&B/Soul"})
song["Tittle"] = "We Loved It"
del song["Singer"]
print(song)
import random
buah = ["Apel", "Anggur", "Jeruk", "Pir"]
print(random.choice(buah))
first_name = ["Bowo", "Jack", "Lilbah"]
last_name = ["Legend", "Lapja", "Oil"]
first_name = random.choice(first_name)
last_name = random.choice(last_name)
random_number = random.randint(100, 1000)
nickname = first_name + last_name + str(random_number)
print(nickname)


for i in range(6):
    print (i)
i = 0
while i<=5:
    print(i)
    i+=1