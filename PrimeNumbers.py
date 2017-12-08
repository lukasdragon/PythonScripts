#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#===============================#
#CODE PROPERTY OF LUKAS G. OLSON#
#https://github.com/lukasdragon #
#===============================#

def is_prime(number):
    for x in range(2, number):
        if number%x ==0:
            return False;
    return True;



number = 2;
primes = [];
while True:
    if is_prime(number):
        primes.append(number);
        print primes
    number+=1;
