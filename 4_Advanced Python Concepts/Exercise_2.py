# Create a Python program that reads a text file and counts the occurrences of each
# word using a dictionary. The program should print the words and their counts.

def text_file_reader(text):
    array_text = text.split(' ')
    counter_word = {}
    value = 1
    for word in array_text:
        if word in counter_word:
            counter_word[word] += 1
        else:
            counter_word[word] = 1

    print('Counter_word is: ', counter_word)

message = 'hola como estas hola como estas estas bien o que'
text_file_reader(message)