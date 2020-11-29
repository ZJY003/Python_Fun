import time
import random
name = input("what's your name?")
print ("Hello, "+name+ ", time to play hangman~")

answerlist = ["word", "look", "hello", "goodbye"]
random.shuffle(answerlist)

answer = list(answerlist[0])

display = []

used = []

display.extend(answer)

used.extend(display)

for i in range(len(display)):
    display[i] = "_"

print (" ".join(display))

print ()

count = 0

while count < len(answer):
    guess = input("please guess a letter  ")
    guess = guess.lower()
    print (count)

    for i in range(len(answer)):
        if answer[i] == guess and guess in used:
            display[i] = guess
            count += 1
            used.remove(guess)
    
    if guess not in display:
        print ("sorry, wrong guess")

    print ("you have guessed : ", count, "corrent letters")

    print (" ".join(display))
    print ()

print ("well done, you geussed the word")






