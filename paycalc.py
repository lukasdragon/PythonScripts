# -*- coding: utf-8 -*-
#!/usr/bin/python
#===============================#
#CODE PROPERTY OF LUKAS G. OLSON#
#https://github.com/lukasdragon #
#===============================#

#Color Codes!
COKBLUE = '\033[94m';
COKGREEN = '\033[92m';
CWARNING = '\033[93m';
CFAIL = '\033[91m';
CRESET ='\033[0m';
CBOLD = '\033[01m';
CREVERSE = '\033[07m';
COTHER = '\033[33m';


#Floats
#Mcdonalds
mcd = 0.5;
paymcd = 0.0;

#Janitor
#We need to get janitor pay as pennies because im lazy with the display code
jad = 10000 * 100.0;
payjan = 0.0;

#length in days
length = int(raw_input(CWARNING + "How many days is your employment?: " + CRESET));

#McDonalds
for days in range(length):
    mcd = mcd * 2;
    paymcd = paymcd + mcd;
   
#Janitor
for days in range(length):    
    payjan = payjan + jad;

#display
print CWARNING, "==========[","Mcdonalds","]=========="
print COKBLUE,"final daily $:", mcd / 100
print COKGREEN,"final total $:", paymcd / 100
     
print CWARNING, "==========[","Janitor","]=========="
print COKBLUE,"final daily $:", jad / 100
print COKGREEN,"final total $:", payjan / 100

print CRESET
