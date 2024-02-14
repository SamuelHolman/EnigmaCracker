import random

def generate(letters):
    Dictionary = {}
    for i in letters:
        Dictionary[i] = i
    return Dictionary

def shuffle(dictionary):
    x, y = random.sample(dictionary.keys(), 2)
    TempDictionary = dictionary.copy()
    TempDictionary[x], TempDictionary[y] = TempDictionary[y], TempDictionary[x]
    return TempDictionary

def decipher(mystery, dictionary):
    DecipheredMessage = ""
    for i, j in enumerate(mystery):
        DecipheredMessage += dictionary[j.lower()]
    return DecipheredMessage

def evaluate(mystery, dictionary):
    Total = 0
    for i, j in enumerate(mystery):
        if i == 0:
            continue
        Total += dictionary[mystery[i - 1]][j]
    return Total