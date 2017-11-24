import random
import sys
import os
import math
import time




global gold
global apple

apple = 0
gold = 0


def start():
    print("Hello and welcome to the game");
    print("")
    choice = input("Are you ready? Yes or No?\n")
    if choice == 'Yes' and 'yes' and 'Y' and 'y':
        print("So lets begin");
        print("")
        begining()

    if choice == 'No' and 'no' and 'n' and 'N':
        print("okay, see you next time");
        time.sleep(3);
        sys.exit();

def begining():
    global apple
    global gold
    print("The task of the game is to collect "
          "apples and to sell them for gold");
    print("Oh wow you lucky boy. "
          "There is an apple on the ground");
    print("")
    begin()

def begin():
    global apple
    global gold

    choice1 = input("Do you wanna pick it up? Yes or No?\n");
    if choice1 == 'Yes' and 'Y' and 'yes' and 'y':
        print("You'v just picked up an apple, well done");
        apple = apple + 1
        print("You now have",apple,"apple");
        follow()

    if choice1 == 'no' and 'No':
        end()


def follow():
    global apple
    global gold
    choice2 = input("There is an other apple do you wanna pick em up ? Yes or No?\n");
    if choice2 == 'Yes':
        print("You'v just picked up an apple, well done");
        apple = apple + 1
        print("You now have", apple, "apples");
        while apple < 100:
            follow()
    if choice2 == 'No':
        end()


def end():
    global gold
    global apple
    print("Okay, you'v cashed out")
    print("")
    time.sleep(2)
    if gold <10:
        gold = apple * 10
    if gold > 10:
        gold = apple * 15

    print("You have",gold,"gold in your bank")
    time.sleep(3);
    choice3 = input("What do you want to do with your gold?\n"
                    "you can pay it to the sphynx or eat it\n");
    if choice3 == 'Pay':
        print("")
        time.sleep(2);
        print("The Spyhnx thanks you, but she has to kill you ")
        killed()
    if choice3 == 'Eat':
        print("")
        time.sleep(2);
        print("OMG, how stupid you are, you'v just tried to eat gold.\nfor this, i have to shoot y in your face.")
        killed()


def killed():
    time.sleep(2);
    print("You'v died.")
    print("Do it better in the next game....")
    time.sleep(2)
    sys.exit();

start()
input()
