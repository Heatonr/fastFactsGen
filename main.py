import random

f = open("C:/Users/Ryan/PycharmProjects/fastFactsGen/letterInfo", "r")
lettersInit = f.read().split("\n")
for index, element in enumerate(lettersInit):
    lettersInit[index] = element.split("\t")
    lettersInit[index][1] = float(lettersInit[index][1][0:-1])
weights = []
letters = []
for element in lettersInit:
    letters.append(element[0])
    weights.append(element[1])
print(weights)

randomList = []
for i in range(0,5):
    randomLetter = random.choices(letters, weights)

    index = letters.index(randomLetter[0])
    letters.pop(index)
    weights.pop(index)

    randomList.append(randomLetter[0])

print(randomList)