#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#===============================#
#CODE PROPERTY OF LUKAS G. OLSON#
#https://github.com/lukasdragon #
#===============================#

alpha = [];

for letter in range(ord("a"), ord("z") + 1):
    alpha.append(chr(letter));

print alpha
print alpha[1:alpha.index("k") + 1]
