import random
import pandas as pd

excel_file = "Test.xlsx"
df = pd.read_excel(excel_file)
words = df["besede"]

def yellow(letter_u, sec_w_letters, no):
    for i in range(no):
        if sec_w_letters[i] == letter_u:
            return True
    return False

def secret_word_gen(no_of_letters):
    return a[no_of_letters][random.randrange(1, len(a[no_of_letters]) + 1)]

a = []
for w in words:
    try:
        if (len(a) - 1) >= len(w):
            a[len(w)].append(w)
        else:
            for i in range(len(w) - (len(a) - 1)):
                a.append([])
            a[len(w)].append(w)
    except:
        a[4].append("null")


print("Let's play wordle!")

while True:
    try:
        no_of_letters = int(input("Enter how many letter word you want to guess: "))
        if no_of_letters < 1 or no_of_letters > 13:
            print("Pick a number from 1 to 13.")
            continue
        break
    except ValueError:
        print("Enter a valid number!")

secret_word_letters = list(secret_word_gen(no_of_letters))
game_result = False
win = ["G" for i in range(no_of_letters)]
no_of_attempts = 0

for round_no in range(no_of_letters + 1):
     
    result = []
    no_of_attempts += 1
    
    while True:
        human_input = input(f"Enter a {no_of_letters} letter word: ")
        human_input_letters = list(human_input)
        if len(human_input_letters) == no_of_letters:
            break
        else:
            continue

    for i, s_letter in enumerate(secret_word_letters):
        if s_letter == human_input_letters[i]:
            result.append("G")
        elif yellow(human_input_letters[i], secret_word_letters, no_of_letters):
            result.append("Y")
        else:
            result.append("R")
    if result == win:
        print(result)
        game_result = True
        break
    else:
        print(result)
        print(f"You have {no_of_letters - round_no} attempts left.")

if game_result == False:
    print("You lost!")
else:
    print(f"You won in {no_of_attempts} attempts!")

print(f"The secret word was {secret_word_gen(no_of_letters)}.")