#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#===============================#
#CODE PROPERTY OF LUKAS G. OLSON#
#https://github.com/lukasdragon #
#===============================#

#Imports
from urllib2 import urlopen
import json
import os
import time

class Severity():
    log = 0;
    message = 1;
    warning = 2;
    failure = 3;


#Settings
class Settings:
    url = "https://pastebin.com/api_scraping.php";
    Key_Words = ["discord.gg", "minecraft", "leak",
                 "password", "discord", "credit",
                 "debit", "bank",
                 "username", "leak", "code"];
    filePath = "/files/"; #relative to script
    idleTime = 40.0; #in seconds
    LogSeverity = Severity.log;


######################################
#DONT MODIFY ANYTHING PAST THIS POINT#
###UNLESS YOU KNOW WHAT YOURE DOING###
######################################

#Color Codes!
COKGREEN = '\033[92m'; #0
COKBLUE = '\033[94m'; #1
CWARNING = '\033[93m'; #2
CFAIL = '\033[91m'; #3
CRESET ='\033[0m';
CBOLD = '\033[01m';



def log_message(severity,string):
    color = "";
    if severity == Severity.log:
        color = COKGREEN;
    elif severity == Severity.message:
        color = COKBLUE;
    elif severity == Severity.warning:
        color = CBOLD + CWARNING;
    elif severity == Severity.failure:
        color = CBOLD + CFAIL;
    if severity >= Settings.LogSeverity:
        print(color + string + CRESET);

#Gets the json file
def get_jsonparsed_data(url):
    response = urlopen(url);
    data = str(response.read());
    return json.loads(data);

#Saves a text file
def save_file(content, title):
    file = open(Settings.filePath + title + ".txt", "w");
    file.write(content);
    file.close();

#Checks for keywords
def is_interesting(dictionary, content):
    for word in dictionary:
        if word in content.lower():
            return True;


#Creates the paste save folder if it doesn't exist
Settings.filePath = (os.path.dirname(os.path.realpath(__file__)) + Settings.filePath);
try:
    os.makedirs(Settings.filePath);
except:
    pass;

starttime=time.time()
ticks = 0;
rescannedFiles = 0;
viewedFiles = [];

#Startup Image
log_message(1,"========BY=======");
log_message(1,"PasteBin Scrapper");
log_message(1,"======Lukas======");



while True:
    #Gets the pastebin recent pastes
    data = get_jsonparsed_data(Settings.url);

    #Loops through each entry

    for paste in data:
        #Opens the individual pastes so that we can extract key words
        page = urlopen(paste["scrape_url"]);
        if not viewedFiles.__contains__(paste["key"]):
            log_message(0,"Found a paste: " + paste["key"])
            content = page.read();
            viewedFiles.append(paste["key"]);

        #Goes through the page and checks for keywords
            if is_interesting(Settings.Key_Words, content):
                save_file(content, paste["key"])
                log_message(1,"Found a match!: " + paste["key"]);
                save_file(content, paste["key"])
        else:
            rescannedFiles += 1;
            log_message(0, "Paste already scanned... Increasing wait time!")
    ticks+=1;
    idletime = ((rescannedFiles * 2) / ticks );
    log_message(1, "Finished Tick!, waiting " + str(Settings.idleTime + idletime) + " seconds!");


    time.sleep((Settings.idleTime +idletime) - ((time.time() - starttime) % (Settings.idleTime + idletime)));
