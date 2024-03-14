
import random
import os
import draw

def clear():
    os.system('clear')

def menu():
    print("Hangman")
    print("Difficulty:")
    print("1: easy")
    print("2: medium")
    print("3: hard")
    print("If you want to quit, type quit.")
    possible_difficulty = [1, 2, 3]
    while True:
        difficulty = input("Choose difficulty: ")
        if difficulty.lower() == "quit":
            clear()
            quit()
        if int(difficulty) in possible_difficulty:
            return int(difficulty)

def choose_category():
    print("Categories:")
    print("1: countries")
    print("2: capitals")
    while True:
        chosen_category = int(input("Choose category: "))
        if chosen_category == 1:
            return "countries"
        elif chosen_category == 2:
            return "capitals"

def read_value_from_file(category):
    word_pool = []
    with open("countries-and-capitals.txt", encoding="UTF-8") as f:
        for line in f:
            words = line.strip().split(" | ")
            if category == "countries":
                word_pool.append(words[0])
            if category == "capitals":
                word_pool.append(words[1])
    return word_pool

def values(difficulty, word_pool):
    lives = 0
    word_to_guess = []
    if difficulty == 1:
        lives = 7
        for word in word_pool:
            if len(word) <= 6:
                word_to_guess.append(word)
    if difficulty == 2:
        lives = 5
        for word in word_pool:
            if len(word) >= 5 and len(word) <= 7:
                word_to_guess.append(word)
    if difficulty == 3:
        lives = 3
        for word in word_pool:
            if len(word) >= 6:
                word_to_guess.append(word)
    secret = random.choice(word_to_guess)
    return lives, secret

def big_secret(secret):
    hidden_guess = ""
    for syl in secret:
        if syl == " ":
            hidden_guess += " "
        elif syl == "-":
            hidden_guess += "-"
        else:
            hidden_guess += "_"
    return hidden_guess

def ask_user(already_tried_letters):
    while True:
        letter = input("Write a letter: ").lower()
        if letter == "quit":
            clear()
            quit()
        elif letter.isalpha() is False or len(letter) != 1:
            print("Try one letter only!")  
        elif letter in already_tried_letters:
            print("You tried this letter.")
        else:
            break
    return letter

def game():
    clear()
    difficulty = menu()
    clear()
    category = choose_category()
    clear()
    word_pool = read_value_from_file(category)
    lives, secret = values(difficulty, word_pool)
    hidden_secret = big_secret(secret)
    already_tried_letters = []
    if " " in secret:
        already_tried_letters.append(" ")
    while lives > 0:
        draw.painting(lives, difficulty)
        print("\n" + " ".join(hidden_secret) + "\n")
        print(f"Lives: {lives}") 
        print(already_tried_letters)
        guess = ask_user(already_tried_letters)
        already_tried_letters.append(guess)
        if guess in str(secret).lower():
            for i, letter in enumerate(secret):
                if str(letter).lower() == str(guess).lower():
                    hidden_secret = hidden_secret[:i]+letter+hidden_secret[i+1:]
        else:
            lives -= 1
        if lives == 0:
            clear()
            draw.painting(lives, difficulty)
            print("You loose!")
            print(f"This was the secret: {secret}")
            input("Press enter to continue...")
            game()
        win = True
        for syllable in str(secret).lower():
            if str(syllable).lower() not in already_tried_letters:
                win = False
        if win is True:
            clear()
            draw.victorypaint()
            print("You won!")
            print(f"This was the secret: {secret}")
            input("Press enter to continue...")
            game()
        print(hidden_secret)
        clear()
game()
