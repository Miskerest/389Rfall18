#!/usr/bin/env python
#-*- coding:utf-8 -*-

# importing a useful library -- feel free to add any others you find necessary
import hashlib
import string

# this will work if you place this script in your writeup folder
wordlist = open("wordlist.txt", 'r')
hashlist = open("../hashes", "r")

# a string equal to 'abcdefghijklmnopqrstuvwxyz'.
salts = string.ascii_lowercase
words = wordlist.read().replace("\r", "").split("\n")
hashes = hashlist.read().split("\n")

for salt in salts:
    for word in words:
        pw = salt+word
        h = hashlib.sha512(pw).hexdigest()
        if h in hashes or (h+"\n") in hashes:
            print "PASSWORD FOUND " + pw + "\n=> " + h