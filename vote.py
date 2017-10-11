# -*- coding: utf-8 -*-
#!/usr/bin/python
#===============================#
#CODE PROPERTY OF LUKAS G. OLSON#
#https://github.com/lukasdragon #
#===============================#


#Color variables!
COKBLUE = '\033[94m';
COKGREEN = '\033[92m';
CWARNING = '\033[93m';
CFAIL = '\033[91m';
CRESET ='\033[0m';
CBOLD = '\033[01m';
CREVERSE = '\033[07m';
COTHER = '\033[33m';


#Helper methods


 


#header
print "{0}{1}=================".format(COTHER, CBOLD);
print "Voting Calculator";
print "================={0}".format(CRESET);


Canadian = True if raw_input(COKGREEN + "Are you Canadian? [Yes|No]: " + CRESET).lower() == 'yes' else False

if Canadian:
    #Age
    Age = raw_input("{0}How old are you?: {1}".format(COKGREEN,CRESET));
    Fetus = 0;
    Baby = 4;
    Child = 17;
    Adult = 130;
    Vampire = 130;

    #parse
    try:
	    Age = int(Age);
    except:
	    print CFAIL + "ERROR! INCORRECT VALUE";


    #Check Age
    if Age <= Fetus:
            print CBOLD + "You are aren't born yet! Come back later!";
    elif Age <= Baby:
	        print CBOLD + "Get away from me baby! You shouldn't even be able to read this!";
    elif Age <= Child:
            print CBOLD + "You are a child! You cannot vote! Come back when you become a human!";
    elif Age <= Adult:
            if raw_input(COKGREEN + "Are you a registered voter? [Yes|No]: " + CRESET).lower() == 'yes':
                print CBOLD + "Congratulations! You are an adult and are able to vote!";
            else:
                print CFAIL + CBOLD + "YOU NEED TO REGISTER TO VOTE! GO DO THAT ASAP!!!!";
    else:
            print CBOLD + CWARNING + "GET AWAY FROM ME SATAN!";

else:
    print CFAIL + "GET OUT OF HERE YOU FILTHY FOREIGNER!"





print CRESET;
