import random
import sys
import os



global counter

counter = 0

global x
global y

x = [1,2,3,4,5,6,7,8,9,10];
z = [1,2,3,4,5,6,7,8,9,10];





t = random.choice(z);
y = random.choice(x);

b = t + y



def beta():
    print("The number is between 2-20");
    alpha()


def alpha():
    global counter
    global y

    guess = int(input("Guess the number"));

    if guess == b:
        print("That is the number");
        print(b);
        print("Du hast",counter,"Versuche benötigt um die Zahl zufinden.");


    if guess < b:
        print("Guess higher");
        counter = counter + 1
        alpha()
    if guess > b:
        print("Guess lower");
        counter = counter + 1
        alpha()



beta()
