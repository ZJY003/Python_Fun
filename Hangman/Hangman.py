import time
import random
name = input("what's your name?")
print ("Hello, "+name+ ", time to play hangman~")

answerlist = ["word", "look", "hello", "goodbye"]
random.shuffle(answerlist)

answer = list(answerlist[0])

display = []

display.extend(answer)

for i in range(len(display)+3):
    display[i] = "_"

print (" ".join(display))

print ()

count = 0

while count < len(answer):
    guess = input("please guess a letter  ")
    guess = guess.lower()
    print (count)

    for i in range(len(answer)):
        if answer[i] == guess:
            display[i] = guess
            count += 1
    
    print (" ".join(display))
    print ()






