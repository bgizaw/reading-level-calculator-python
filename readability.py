import re

# ask for and read user input of text
def main():
    passage = input("Please enter the passage you would like to check: ")
    letters(passage)


# find the average number of letters per 100 words in the text: L
def letters(passage):
    letter_string = re.sub(r'\W+', '', passage)
    no_whitespace = letter_string.replace(" ", "")
    letters_list = [*no_whitespace]
    letters_num = len(letters_list)

#def sentences(passage)


# find the average number of sentences per 100 words in the text: S



# plug L and S into the coleman-liau index




main()