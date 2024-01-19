import json
import random

try:
    file = open("land-trivia/countries.json")
except FileNotFoundError:
    file = open("countries.json")

print("helvete")

countries = json.load(file)

score = 0
questionCount = 0
keepAsking = True

while keepAsking:
    questionCount += 1
    index = random.randint(0, len(countries))
    land = countries[index]
    capital = (str(x) for x in land)
    comp_capital = (x.lower for x in capital )

    answer = input(f"What is the the capitol of {land['name']['common']}? ")
    answer = answer.lower()

    ascii_sum_solution = []
    ascii_sum_answer = 0
    
    for i in comp_capital: 
        for c in comp_capital[i]:
            ascii_sum_solution[i] += ord(c) - 96
        
    for c in answer:
        ascii_sum_answer += ord(c) - 96

    if answer in comp_capital or ascii_sum_answer/ascii_sum_solution > 0.8:
        score += 1
        print(f"Correct. Your total score is now {score}, with an average correctness of {100*score/questionCount:.1f}%. ")
    else:
        if ascii_sum_answer/ascii_sum_solution > 0.5:
            print(f"You might have spelt the name wrong. The correct answer was {capital}")
        else:
            print(f"Wrong answer. The correct answer was {capital}")

    invalidInput = True

    while invalidInput:
        try:
            yesNo = input("Do you want another question? (y/n) ")
            yesNo.lower()
            if yesNo == "y":
                keepAsking = True
            else:
                print("Restart the program if you change your mind. ")
                keepAsking = False
            invalidInput = False
        except ValueError:
            print("Answer yes or no with a y or an n")

file.close()