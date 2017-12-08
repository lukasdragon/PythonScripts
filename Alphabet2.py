#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#===============================#
#CODE PROPERTY OF LUKAS G. OLSON#
#https://github.com/lukasdragon #
#===============================#

Alphabet = [];

Start_Letter = "A";
End_Letter = "Z";
StartInt = ord(Start_Letter)
EndInt = ord(End_Letter)
for x in range(ord(Start_Letter)-64,ord(End_Letter) -63):
    print x
    print x*chr(x+64)