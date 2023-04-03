code = []
with open("./characters.py", "r", encoding= 'utf-8') as f:
    for line in f:
        code.append(line)

for line in code:
    print(line)
