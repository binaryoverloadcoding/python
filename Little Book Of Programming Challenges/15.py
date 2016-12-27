#Challenge 15 - William Oldham

import easygui as eg

sentence = ""

eg.msgbox("This program will count the number of words in a sentence!")
sentence = eg.enterbox("Enter the sentence to count the number of words in: ")

index = sentence.rfind(".")
if index == -1:
    newSentence = sentence;
else:
    newSentence = sentence[index];
words = newSentence.split(" ")
eg.msgbox("There are " + str(len(words)) + " words in this sentence!")