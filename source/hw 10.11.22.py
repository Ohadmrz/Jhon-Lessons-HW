'''
HW 10.11.22
'''

'''
MATOSIM: 1
seats_layout = input("insert sits layout: ")
seats_split = seats_layout.split(" ")
if len(seats_split) > 1:
    if len(seats_split) > 2:
      print(len(seats_split[0]) , len(seats_split[1]) , len(seats_split[2]))
    else: print(len(seats_split[0]) , len(seats_split[1]))
else: print(len(seats_split[0]))
'''
''''''

'''
MATOSIM: 2
seat_number = input("insert seat number: ")
seats_layout = input("insert seats layout: ")
chair = seat_number[-1]
row_number = seat_number[:-1]
seats_split = seats_layout.split(" ")
if len(seats_split) > 1:
    if len(seats_split) > 2:
        if chair == seats_split[0][0] or chair == seats_split[0][-1] or chair == seats_split[1][0] or chair == seats_split[1][-1] or chair == seats_split[2][0] or chair == seats_split[2][-1]:
            if chair == seats_split[0][0] or chair == seats_split[2][-1]:
                chair_location = "window"
            else: chair_location = "aisle"
        else: chair_location = "middle"
    elif chair == seats_split[0][0] or chair == seats_split[1][-1]: chair_location = "window"
    elif chair == seats_split[0][-1] or chair == seats_split[1][0]: chair_location = "aisle"
    else: chair_location = "middle"
elif chair == seats_split[0][0] or chair == seats_split[0][-1]: chair_location = "window"
else: chair_location = "middle"
print("chair: ", chair)
print("row number: ", row_number)
print("chair's location: ", chair_location)
''''''

''''''
Q.1
''''''
word = input("insert any word: ")
print("word lengh: " , len(word))
'''

'''
Q.2
''''''
word = input("insert any word: ")
reverse_word = word[::-1]
if word == reverse_word:
    print("This string is a palindrome :) ")
else: print("This string is not a palindrome :( ")
'''

'''
Q.3
''''''
text = input("insert any text: ")
space_text = text.split(" ")
print("amount of words:" , (len(space_text)))
print("amount of charts:" , (len(text)))
print("amount of non-whitespace charts:" , (len(text)) - (text.count(" ")))
print("amount of vowels:" , int(text.count("a")) + int(text.count("i")) + int(text.count("e")) + int(text.count("o")) + int(text.count("u")) + int(text.count("y")))
'''

'''
Q.4
''''''
word = input("insert any word: ")
if word[-1] == "a":
 print("True: the word ends with a vowel")
elif word[-1] == "e":print("True: the word ends with a vowel")
elif word[-1] == "i":print("True: the word ends with a vowel")
elif word[-1] == "o":print("True: the word ends with a vowel")
elif word[-1] == "u":print("True: the word ends with a vowel")
elif word[-1] == "y":print("True: the word ends with a vowel")
else: print("False: the word doesn't ends with a vowel")
'''

'''
word = input("insert a word: ")
count_space = word.count(" "[0:])
len_word = len(word)
if count_space == len_word:
 print("only spaces")
else: print("not only spaces")
'''

'''
sentence = input("insert any sentence: ")
print(word.title())
'''

MATOSIM: 2
seat_number = input("insert seat number: ")
seats_layout = input("insert seats layout: ")
chair = seat_number[-1]
row_number = seat_number[:-1]
seats_split = seats_layout.split(" ")
if len(seats_split) > 1:
    if len(seats_split) > 2:
        if chair == seats_split[0][0] or chair == seats_split[0][-1] or chair == seats_split[1][0] or chair == seats_split[1][-1] or chair == seats_split[2][0] or chair == seats_split[2][-1]:
            if chair == seats_split[0][0] or chair == seats_split[2][-1]:
                chair_location = "window"
            else: chair_location = "aisle"
        else: chair_location = "middle"
    elif chair == seats_split[0][0] or chair == seats_split[1][-1]: chair_location = "window"
    elif chair == seats_split[0][-1] or chair == seats_split[1][0]: chair_location = "aisle"
    else: chair_location = "middle"
elif chair == seats_split[0][0] or chair == seats_split[0][-1]: chair_location = "window"
else: chair_location = "middle"
print("chair: ", chair)
print("row number: ", row_number)
print("chair's location: ", chair_location)