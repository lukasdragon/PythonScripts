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
Cpopulation = 7.5E9;
CinfectionMultiplier = 2;


#Variables
infected = 0;
infectionspread = 1;
days = 1;


while infected < Cpopulation:
    days += 1;
    infected = infected + infectionspread;
    infectionspread = infectionspread * CinfectionMultiplier;
    

    
print CWARNING, "==========[","Results","]=========="
print COKBLUE,"Entire Population Infected within:", days,"days..."
print COKGREEN,"Estimated Infected Population:", infected
print COKGREEN,"INFECTION PERCENTAGE:", (infected / Cpopulation) * 100, "%";
print CRESET;