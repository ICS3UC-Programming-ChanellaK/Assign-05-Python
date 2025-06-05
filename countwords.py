#!/usr/bin/env python3
# Created By: chanella
# Date: May 17, 2025
# This program counts the number of words in sentences
# and prints the number of words in each sentence


def count_words(sentence):
    count = 0  # this is a counter to store the number
    # of words in the sentence
    in_word = False  # this tells us if we are in a word or not

    try:
        # loop through each letter in a sentence
        # if a letter is not a space and we are
        # not inside a word, a new word has started
        for letter in sentence:
            if letter != " " and in_word == False:
                in_word = True
                count += 1  # we increment the count

            # if the letter is a space, it means the word ended
            elif letter == " ":
                in_word = False  # we are no longer inside the word

    except:
        print("Something went wrong ")
        return count  # it returns the current count
        # in case of an exception
    return count  # return the total number of words

if __name__ == "__main__":
    sentence = input("Enter a sentence:") # ask the user to enter a sentence
    result = count_words(sentence)  # count the words in a sentence
    print("Number of words in the sentence:", result)  # show the result