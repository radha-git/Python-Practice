import random
from unicodedata import digit

def get_guess():
    return list(input("What is your guess"))


def generate_code():
    digits=[str(num) for num in range(10)]


    random.shuffle(digits)

    return digit[:3]

def generate_cluess(code,user_guess):

    if user_guess==code:
        return "CODE CRACKED!"
    clues=[]
    
    for ind,num in enumerate(user_guess):
        if num ==code[ind]:
            clues.append('match')
        elif num in code:
            clues.append('Close')

    if clues==[]:
        return["Nope"]
    else:
        return clues

print('Welcome code Breaker!!')

secret_code=generate_code()

clue_report =[]
while clue_report != "code cracked!":
    guess = get_guess()

    clue_report=generate_cluess(guess,secret_code)
    print('here is the result of your guess: ')
    for clue in clue_report:
        print(clue)
