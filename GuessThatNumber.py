#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#===============================#
#CODE PROPERTY OF LUKAS G. OLSON#
#https://github.com/lukasdragon #
#===============================#

import random;

Wins = 0;
AverageGuesses = 0;

while True:
    chosenNumbers = [];
    UserAnswer = -1;

    answer = random.choice(range(1,101));

    print "=======[",Wins,"]======="
    while UserAnswer != answer:
        UserAnswer = int(raw_input("Guess The Number!: "))

        #Game Logic
        if UserAnswer <= 0:
            print "Please choose a number larger than zero!";
        elif UserAnswer in chosenNumbers:
            print "You have already tried that number! Try Again...";
            continue;
        elif UserAnswer > answer:
            print "The Number Is Lower";
            chosenNumbers.append(UserAnswer);
        elif UserAnswer < answer:
            print "The Number Is Larger";
            chosenNumbers.append(UserAnswer);

    #Guess Count Logic
    Guesses = len(chosenNumbers) + 1;
    if Wins > 0:
        AverageGuesses = (AverageGuesses + Guesses) / 2;
    else:
        AverageGuesses = Guesses;

    print "We Have A Winner!!! It only took you", Guesses, "guesses! The Average number of guesses is: ", AverageGuesses;

    #Play Again Logic
    if raw_input("Do you want to play again?: ").lower() == "no":
        print "Thanks For Playing!";
        break;

    #Win Counter
    Wins += 1;
