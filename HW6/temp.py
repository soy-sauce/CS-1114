'''
Danny Lin
dl3201
hw8q2c.py
This code utilizes the functions created in part a and part b.
My reverse() function takes the first 
'''

def first_word(string):
    first_space_pos = string.find(" ")
    word = string[0:first_space_pos]
    return word

def last_words(string):
    first_space_pos = string.find(" ")
    words = string[first_space_pos+1:]
    return words

def reverse(string):
    #counts the number of words in the string
    words = string.count(" ") +1
    count = 1
    #empty string to store temp values
    string_reversed = ""
    #while loop to add first_word of last_word() to the back
    while count < words:
        string_reversed = first_word(string) + str(" ") + string_reversed
        string = last_words(string)
        count += 1
    new_string = string + " " + string_reversed
    #prints the string in reverse
    return new_string

print(reverse("The quick brown fox"))