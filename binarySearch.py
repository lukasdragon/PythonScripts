#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#===============================#
#CODE PROPERTY OF LUKAS G. OLSON#
#https://github.com/lukasdragon #
#===============================#

answer = int(raw_input("Enter a number and we will guess it!: "));


maxnum = 0;
minnum = 0;
guess = maxnum;


while True:

    if maxnum < guess:
        maxnum += 100;


    guess = (maxnum + minnum) / 2;
    print(str(guess))
    if guess == answer:
           break;
    elif guess > answer:
        maxnum = guess;
    elif guess < answer:
        minnum = guess;
print("answer is: " + str(guess));