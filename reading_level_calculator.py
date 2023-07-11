import re


# ask for and read user input of text
def main():
    passage = input("Please enter the passage you would like to check: ")
    letters_num = letters(passage)
    words_num = words(passage)
    sentences_num = sentences(passage)
    S = average_sentences(words_num, sentences_num)
    L = average_letters(letters_num, words_num)
    reading_level(S, L)


# count the number of letters in the input
def letters(passage):
    # remove all non-alphabet characters from the user's input
    letter_string = re.sub(r'\W+', '', passage)
    no_whitespace = letter_string.replace(" ", "")
    letters_list = [*no_whitespace]
    letters_num = len(letters_list)
    return letters_num


# count the number of sentences in the input
def sentences(passage):
    sentence_num = str.count(passage, '.')
    sentence_num += str.count(passage, '?')
    sentence_num += str.count(passage, '!')
    return sentence_num


# count the number of words in the input
def words(passage):
    words_num = str.count(passage, " ") + 1
    return words_num


# find the average number of letters per 100 words in the text: L
def average_letters(letters_num, words_num):
    L = letters_num / words_num * 100
    return L


# find the average number of sentences per 100 words in the text: S
def average_sentences(words_num, sentences_num):
    S = sentences_num / words_num * 100
    return S


# plug the variables L and S into the coleman-liau index
def reading_level(S, L):
    level_unrounded = 0.0588 * L - 0.296 * S - 15.8
    # round the final answer to the nearest whole number
    level = round(level_unrounded)
    print("Your reading level is ", end="")
    if 1 <= level < 16:
        print("grade", level)
    elif level < 1:
        print("before grade 1")
    else:
        print("grade 16+")


main()
