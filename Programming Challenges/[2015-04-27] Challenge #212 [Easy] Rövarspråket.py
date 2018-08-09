def discombobulation():
    normal_word = input("Please enter the word you want to Rövarspråket: ")
    vowels = ["a", "e", "i", "o", "u", "y", "å", "ä", "ö"]
    encoded_word = ""

    for letter in normal_word.lower():
        if letter.isalpha() and letter not in vowels:
            encoded_word += letter + "o" + letter.lower()
        else:
            encoded_word += letter

    print(encoded_word.capitalize())


discombobulation()
