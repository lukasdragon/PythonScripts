#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#===============================#
#CODE PROPERTY OF LUKAS G. OLSON#
#https://github.com/lukasdragon #
#===============================#
import random;
d = {};
for x in range(ord("a"), ord("z")+1):
    d[chr(x)] = random.randint(0,100);
for x in sorted(d):
    print x,":",d[x];