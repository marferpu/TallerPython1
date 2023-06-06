# Write a Python function called is_palindrome that checks if a given word is a
# palindrome. The function should have proper error handling and be tested with
# unittest.

class InvalidLengthWord(Exception):
    pass

def is_palindrome(word):
    length_word = len(word)
    if length_word % 2 != 0:
        array_word = word.split()
        middle = int(round((length_word -1)//2))
        # print(f'middle: {middle}')
        counter = 0
        for i in range(0,middle):
            if array_word[i] == array_word[-i]:
                counter +=1
        if counter == middle:
            print (f'The word **{word}** is a palindrome')
        else:
             print (f'The word **{word}** is not a palindrome' )
    else:
        raise InvalidLengthWord(f'The word **{word}** is not a palindrome')  


w = 'oso'
is_palindrome(w)
print('************************** ################### *********************************')
w = 'osoris'
is_palindrome(w)