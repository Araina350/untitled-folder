import random
print("HOLA,HI,NAMASTE,BOUNJOUR.WELCOME COME TO THE NUMBER GUESS .A RANDOM NUMBER WILL BE GENERATED AND YOU HAVE T0 GUESS THAT\n YOU HAVE 7 CHANCES . GOOD LUCK!")
number_to_guess=random.randrange(100)
guess_counter=0
chances=7
while guess_counter<chances:
    guess_counter+=1
    myguess=int(input("PLEASE ENTER YOUR GUESS : "))
    if myguess==number_to_guess:
        print("CONGRATS YOU WON")
        break
    elif myguess<number_to_guess:
        print("YOUR GUESS IS LESSER")
    elif myguess>number_to_guess:
        print("YOUR GUESS IS GREATER") 
    elif guess_counter >= chances and myguess!= number_to_guess:
        print("Oops you lost")      