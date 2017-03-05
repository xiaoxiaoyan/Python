from __future__ import print_function

import random


def guss_num(num):
    while True:
    	a = int(raw_input("input the number:"))
	if ( a > num ):
	    print("the number is less the you input")
	elif (a < num ):
	    print("the number is lager the you input")
	else:
	    print("you are great!")
	    break

def main():
    num = random.randint(1,99)
    guss_num(num)

if __name__ == "__main__":
    main()

