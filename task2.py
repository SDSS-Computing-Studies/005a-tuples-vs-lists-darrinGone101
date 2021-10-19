#!python3

"""
Create a variable that contains an empy list.
Ask a user to enter 5 words.  Add the words into the list.
Print the list
inputs:
string 
string
string
string
string

outputs:
string

example:
Enter a word: apple
Enter a word: worm
Enter a word: dollar
Enter a word: shingle
Enter a word: virus

['apple', 'worm', 'dollar', 'shingle', 'virus']
"""
word1 = str(input("enter a word: "))
word2 = str(input("enter a word: "))
word3 = str(input("enter a word: "))
word4 = str(input("enter a word: "))
word5 = str(input("enter a word: "))
list=[]
list.append(word1)
list.append(word2)
list.append(word3)
list.append(word4)
list.append(word5)
print(list)