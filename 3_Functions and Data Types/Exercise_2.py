# Create a Python function called reverse_string that takes a string as input and returns
# the reversed string.

def reverse_string(word):
    if word:
        words = word.split()
        word_reverse = word[-1] + reverse_string(word[:-1])
        return word_reverse
    return ""

string = input('Write a word: ')
reverse_word = reverse_string(string)

print('Your reverse word is: ', reverse_word)
