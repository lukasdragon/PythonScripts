#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#===============================#
#CODE PROPERTY OF LUKAS G. OLSON#
#https://github.com/lukasdragon #
#===============================#

def Replace(string, word, replacement):
        while True:
            position = string.find(word);
            if position == -1:
                break;
            Length = len(word);
            string = string[:position] + replacement + string[position + Length:]
        return string;


sentence = raw_input("Enter a sentence!: ")
replace = raw_input("What do you want to replace?: ")
replacement = raw_input("What do you want to replace that with?: ")


print Replace(sentence, replace, replacement);
#to compare if its correct
print (sentence.replace(replace, replacement));