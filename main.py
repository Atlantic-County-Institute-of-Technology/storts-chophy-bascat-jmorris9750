import random

word_list = []
word_len = 6


# extracts words that are as long as word_len
def extract_words():
    try:
        with open("assets/words_alpha.txt", "r") as file:
            for word in file:
                if len(word) == word_len:
                    word_list.append(word.strip())
                else:
                    pass

    except FileNotFoundError:
        print("file not found")


# checks if user inputted integers or spaces
def check_guess(guess):
    if guess.__contains__(" ") or guess.__contains__("1") or guess.__contains__("2")\
            or guess.__contains__("3") or guess.__contains__("4") or guess.__contains__("5")\
            or guess.__contains__("5") or guess.__contains__("6") or guess.__contains__("7")\
            or guess.__contains__("8") or guess.__contains__("9") or guess.__contains__("0"):
        return False


# finds a random word from the list made by extract_words
def find_word():
    extract_words()

    number = [random.randint(0, len(word_list)) for i in range(1)]
    word_guess = word_list[number[0]]
    return word_guess


def main():
    tries = 5
    target = find_word()

    # starts the response with bascat
    response = ["bascat" for i in range(len(target))]

    solved = False
    while not solved:
        print(f"{tries} tries left")
        # asks user for input then checks for compatibility with parameters
        guess = input("5 letter words:")
        if len(guess) != word_len-1:
            print(f"[!] enter {word_len-1} letter words only")
        elif check_guess(guess) is False:
            print(f"[!] enter {word_len-1} letter words with no spaces or numbers")
        else:
            tries -= 1
            if guess == target:
                print("solved")
                solved = True

            else:
                # finds whether each letter is chopy or storts
                for g_digit in range(len(guess)):
                    for t_digit in range(len(target)):

                        if guess[g_digit] == target[t_digit]:
                            if g_digit == t_digit:
                                response[g_digit] = "chopy"

                            else:
                                response[g_digit] = "storts"


                print(response)
            # ends game if word has not been solved
            if tries == 0:
                print(f"You Lost \n it was {target}")
                solved = True


if __name__ == "__main__":
    main()
