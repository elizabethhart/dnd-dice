#!/usr/bin/python

import sys
import random

def main():
    die = int(input("Which die would you like to use? "))
    quantity = int(input("How many would you like to roll? "))

    advantage = "n"

    roll_quantity = quantity
    
    if quantity == 1:
      advantage = input("With advantage? (y/n)")

    if advantage == "y":
      roll_quantity += 1

    roll_list = []

    print("Rolling " + str(quantity) + "D" + str(die) + "...")    

    for i in range(roll_quantity):
      roll = random.randint(1,die)
      roll_list.append(roll)

    print("Results: " + str(roll_list))

    if advantage == "y":
      print("Total: " + str(max(roll_list)))
    else:
      print("Total: " + str(sum(roll_list)))

if __name__ == '__main__':
	main()