#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#===============================#
#CODE PROPERTY OF LUKAS G. OLSON#
#https://github.com/lukasdragon #
#===============================#

for number in range(1,11):
    if number != 5:
        print number;

print "==";

for number in range(1,11):
    if number == 5:
        continue
    print number;