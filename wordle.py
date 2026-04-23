while True:
    

    print("Let's play wordle!")
    while True:
        try:
            no_of_letters = int(input("Enter how many letter word you want to guess: "))
            break
        except ValueError:
            print("Enter a valid number!")


    human_input = input(f"Enter a {no_of_letters} letter word: ")
    secret_word = "world"
    
    result = []

    human_input_letters = list(human_input)
    secret_word_letters = list(secret_word)

    for i, secret_word_letters in enumerate(secret_word_letters):
        if secret_word_letters == human_input_letters[i]:
            result.append("G")
        elif 
            result.append("Y")
        else:
            result.append("R")



    print(no_of_letters)
    print(human_input)
    print(human_input_letters)
    print(secret_word)
    print(secret_word_letters)
    print(result)
    break
