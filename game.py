import time
import random
name=input("What is ur name?")

print("hello," +name, "time to play!")
#wait for 1 second
time.sleep(1)

print("start guessing...")
time.sleep(0.5)

kelimeler = ["ability","about","above","absolute","accessible","accommodation",
             "accounting","beautiful","bookstore","calculator","clever","engaged",
             "engineer","enough","handsome","refrigerator","opposite","socks",
             "interested","strawberry","backgammon","anniversary","confused",
             "dangerous","entertainment","exhausted","impossible","overweight",
             "temperature","vacation","scissors","accommodation","appointment",
             "decrease","development","earthquake","environment","brand",
             "environment","necessary","luggage","responsible","ambassador",
             "circumstance","congratulate","frequent",]

#here we set the secret
#word = "secret"
word = random.choice(kelimeler)


#create a variable with an empty value
guesses=""

#determine numbe of turns
turns=10

#check if the turns are more than zero
while(turns >0):

    #make a counter that starts with zero
    failed=0

    #for every character in secret_word
    for char in word:
        #see  if the character is in the players guess
        if char in guesses:
            print(char)

        else:
             #if not found,print dash
             print("_")

             failed  +=1

    if failed==0:
        print("you won")
        break

    guess=input("guess a character:")

    #set the players guess to guesses
    guesses+=guess

    #if the guess is not found in the secret word
    if guess not in word:

        #turns counter decreases with 1
        turns-=1

        print("wrong")
        #how many turns are left
        print("you have", +turns, 'more guesses')

        #if the turns are equal to zero
        if turns ==0:
           print("you loose")




    
