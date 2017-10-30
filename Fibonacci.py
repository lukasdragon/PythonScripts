#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#===============================#
#CODE PROPERTY OF LUKAS G. OLSON#
#https://github.com/lukasdragon #
#===============================#

#variables
FirstDigit=0;
SecondDigit=1;
Number = 0;
sequence = [FirstDigit, SecondDigit];

sequenceLength = int(raw_input("How many numbers do you want to generate?: "));


for digit in range(sequenceLength - 2):
    Number = FirstDigit + SecondDigit;
    FirstDigit = SecondDigit;
    SecondDigit = Number;
    sequence.append(Number);


Ourfile = open('fibonacci.txt', 'w')
for item in sequence:
   
    print>>Ourfile, item
    print item
