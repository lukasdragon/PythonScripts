# -*- coding: utf-8 -*-
#!/usr/bin/python
#===============================#
#CODE PROPERTY OF LUKAS G. OLSON#
#https://github.com/lukasdragon #
#===============================#
   

#variables
num = 320
num = int(input("Enter a number: "))

print "The factors for ", num, "are:"
for i in range(1, num + 1):
    if num % i == 0:
        print(i)
