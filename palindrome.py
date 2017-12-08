#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#===============================#
#CODE PROPERTY OF LUKAS G. OLSON#
#https://github.com/lukasdragon #
#===============================#
word = raw_input("Enter your word: ");

if word == "".join(reversed(word)):
    print("Word is a palindrome");
else:
    print("Your word is not a palindrome");