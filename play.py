# -*- coding:utf-8 -*-

from __future__ import print_function
import random


def guss_num(num):
    while True:
        try:
            input_num = int(raw_input("pls input your number:"))
        except ValueError , e:
            print(e)
        if  input_num > num :
            print("the number is less the you input")
        elif input_num < num :
            print("the number is lager the you input")
        else:
            print("you are great!")
            print("===========================")
            break


def play_game():
    """
    begin play game
    """
    main()
    while True:
        res = raw_input("Do you want to play again,pls input yes or no:")
        if  res in ("y","yes"):
            main()
        else:
            print("========bye bye=========")
            break

	    
def main():
    print("=======paly game=======")
    num = random.randint(1,99)
    guss_num(num)

if __name__ == "__main__":
    play_game()



