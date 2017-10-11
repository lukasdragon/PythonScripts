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



#Constants
Cquarter = 25;
Cdime = 10;
Cnickel = 5;
Cpenny = 1;

#Variables
change = int(raw_input('Please enter change amount in cents: '));
quarters = 0;
dimes = 0;
nickels = 0;
pennies = 0;

#Quarters
while (change >= Cquarter):   
    change = change - Cquarter;
    quarters = quarters + 1;   

#Dimes
while (change >= Cdime):   
    change = change - Cdime;
    dimes = dimes + 1; 

#Nickels
while (change >= Cnickel):   
    change = change - Cnickel;
    nickels = nickels + 1; 

#Pennies
while (change >= Cpenny):   
    change = change - Cpenny;
    pennies = pennies + 1; 


print ("Quarters: ",quarters,"|Dimes: ",dimes,"|Nickels: ",nickels,"|Pennies: ",pennies)
