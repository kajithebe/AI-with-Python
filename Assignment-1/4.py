'''In this exercise create two functions
my_split : which splits sentence given as first argument using second argument as a separator character to separate list items. Function returns a list of items.
my_join : which joins list given as first argument to a string separated with character given as second argument. Function returns a string.
In this exercise you are not allowed to use Python split and join functions
Example output:
Please enter sentence:This is a sentence
This,is,a,sentence
This
is
a
sentence
The output of the program must be exactly the same as the example output (the most strict comparison level)'''

def my_split(sentence, separator):
    result = []
    current_word = ""
    for char in sentence:
        if char == separator: # when char is separator, the word is complete
            result.append(current_word)
            current_word = "" # Resetting the current word to start new word
        else:
            current_word += char
    result.append(current_word)  # Add the last word
    return result


def my_join(word_list, separator):
    result = ""
    for word in word_list:
        result += f"{word}\n" #Placing the result in new line
    return result


sentence = input("Please enter sentence: ")
separator = " "


print(my_split(sentence, separator))

print(my_join(my_split(sentence, separator), ","))
