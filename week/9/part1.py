#!/usr/bin/env python
#-*- coding:utf-8 -*-

# importing a useful library -- feel free to add any others you find necessary
import hashlib
import string

# this will work if you place this script in your writeup folder
wordlist = open("../probable-v2-top1575.txt", 'r')
hashlist = open("../hashes", "r")

# a string equal to 'abcdefghijklmnopqrstuvwxyz'.
salts = string.ascii_lowercase
words = wordlist.readlines()
hashes = hashlist.readlines()

for salt in salts:
    for word in words:
        pw = salt+word
        if hashlib.sha512(pw).digest() == pw:
            print "PASSWORD FOUND" + pw