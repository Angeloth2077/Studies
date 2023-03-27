import random

num = random.randint(0,10)
prompt = int(input("whrite"))

def start(prompt):
    if num > prompt:
        print(str(num) + " Is higher")
        prompt = int(input("Whrite\n"))
        print(str(prompt))
    elif num < prompt:
        print(str(num) + " Is lower")
        prompt = int(input("Whrite\n"))
        print(str(prompt))
    
    return prompt

while num != prompt:
    prompt = start(prompt)
