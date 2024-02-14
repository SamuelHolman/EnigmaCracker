f = open("marvel_data.txt", "r", encoding="utf-8")
Text = f.read()
length = len(Text)

letters = "abcdefghijklmnopqrstuvwxyz1234567890!., -_'\":;/"

Values = {}

for i in letters:
    TempValues = {}
    for j in letters:
        TempValues[str(j)] = 0
    Values[str(i)] = TempValues
    
        

for i, j in enumerate(Text):
    if i == length - 1:
        continue
    
    if j.lower() and Text[i + 1].lower() in letters:
        try:
            Values[j.lower()][Text[i + 1].lower()] += 1
        except:
            continue

print(Values)