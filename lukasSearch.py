#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#===============================#
#CODE PROPERTY OF LUKAS G. OLSON#
#https://github.com/lukasdragon #
#===============================#

number = 100;
answer = 10;

while True:
    if number == answer:
        break;
    elif number > answer:
        number = number / 2;
    elif number < answer:
        number = number + (number / 2);
    print("Tried: " + str(number));
print number;