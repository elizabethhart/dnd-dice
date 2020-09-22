#!/usr/bin/python

import sys
import random

def main():
    gp = int(input("How many GP received? "))
    members = int(input("How many members in the campaign? "))

    distributed_amt = round(gp/members)

    print(str(distributed_amt) + " GP per person")   

if __name__ == '__main__':
	main()