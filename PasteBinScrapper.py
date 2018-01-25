#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#===============================#
#CODE PROPERTY OF LUKAS G. OLSON#
#https://github.com/lukasdragon #
#===============================#

#Imports
from urllib2 import urlopen
from ConfigParser import SafeConfigParser
import json
import os
import time
import sys
from multiprocessing.dummy import Pool as ThreadPool




######################################
#DONT MODIFY ANYTHING PAST THIS POINT#
###UNLESS YOU KNOW WHAT YOURE DOING###
#ONLY MODIFY SETTINGS WITH CONFIG.INI#
######################################


class Severity():
    log = 0;
    message = 1;
    warning = 2;
    failure = 3;

class Settings:
    url = "";
    Key_Words = [];
    filePath = "";
    idleTime = 0;
    LogSeverity = Severity.log;
    threads = 4;

#Color Codes!
COKGREEN = '\033[92m'; #0
COKBLUE = '\033[94m'; #1
CWARNING = '\033[93m'; #2
CFAIL = '\033[91m'; #3
CRESET ='\033[0m';
CBOLD = '\033[01m';


def log_message(severity,string):
    color = "";
    prefix = "";
    if severity == Severity.log:
        color = COKGREEN;
        prefix = "LOG: "
    elif severity == Severity.message:
        color = COKBLUE;
        prefix = "MSG: "
    elif severity == Severity.warning:
        color = CBOLD + CWARNING;
    elif severity == Severity.failure:
        color = CBOLD + CFAIL;
    if severity >= Settings.LogSeverity:
        print(color + prefix + string + CRESET);


#read and write config file
try:
    config = SafeConfigParser();
    config.read('config.ini');
    Settings.url = config.get('main', 'api_url')
    Settings.idleTime = config.getfloat('main', 'waitperiod')
    Settings.filePath = config.get('main','filePath')
    Settings.LogSeverity = config.getint('main','logLevel')
    Settings.Key_Words = [e.strip() for e in config.get('main', 'keyWords').split(',')]
    Settings.threads = config.getint('main', 'threads')
except:
    log_message(Severity.failure,"config.ini not found! Making one...")
    config = SafeConfigParser()
    config.read('config.ini')
    config.add_section('main')
    config.set('main', 'api_url', "https://pastebin.com/api_scraping.php")
    config.set('main', 'filePath', '/files/')
    config.set('main', 'waitperiod', '40.0')
    config.set('main', 'threads', '4')
    config.set('main', '; Minimum log severity', '')
    config.set('main', '; 0 = log | 1 = message | 2 = warning | 3 = failure', '')
    config.set('main', 'logLevel', '0')
    config.set('main', '; The keywords required to download a file, seperated by commas', '')
    config.set('main', 'keyWords', "discord.gg,bank,leak")
    with open('config.ini', 'w') as f:
        config.write(f)
    log_message(Severity.failure, "Please edit config.ini and relaunch the script!")
    sys.exit();


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

def scanData(page):
    rescannedFiles = 0;
    if not viewedFiles.__contains__(paste["key"]):
        log_message(0,"Found a paste: " + paste["key"])
        content = page.read();
        viewedFiles.append(paste["key"]);

    if is_interesting(Settings.Key_Words, content):
        save_file(content, paste["key"])
        log_message(1,"Found a match!: " + paste["key"]);
        save_file(content, paste["key"])
    else:
        rescannedFiles += 1;
        log_message(0, "Paste already scanned... Increasing wait time!")
    return rescannedFiles;

#Startup Image
log_message(1,"========BY=======");
log_message(1,"PasteBin Scrapper");
log_message(1,"======Lukas======");

#Creates the paste save folder if it doesn't exist
Settings.filePath = (os.path.dirname(os.path.realpath(__file__)) + Settings.filePath);
try:
    os.makedirs(Settings.filePath);
except:
    pass;

starttime=time.time()
ticks, rescannedFiles = 0;
viewedFiles = [];

#starts threading stuff
pool = ThreadPool()
pool = ThreadPool(Settings.threads)


while True:
    try:
        data = get_jsonparsed_data(Settings.url);

        #Loops through each entry
        page = [];
        for paste in data:
            page.append(urlopen(paste["scrape_url"]));

        results = pool.map(scanData, page);
        pool.close()
        pool.join()
        page = [];


        for x in results:
            rescannedFiles += x;

        ticks+=1;
        idletime = ((rescannedFiles * 2) / ticks );
        log_message(1, "Finished Tick!, waiting " + str(Settings.idleTime + idletime) + " seconds!");
    except:
        pass;

    time.sleep((Settings.idleTime +idletime) - ((time.time() - starttime) % (Settings.idleTime + idletime)));
