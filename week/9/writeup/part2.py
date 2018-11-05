#!/usr/bin/env python
#-*- coding:utf-8 -*-

# importing useful libraries -- feel free to add any others you find necessary
import socket
import hashlib
import string

host = "142.93.117.193"   # IP address or URL
port = 7331     # port

# use these to connect to the service
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

data = s.recv(1024)
print(data)

while "hash of" in data:
# receive some data

    to_hash =  data[data.index("of")+3:data.index("of")+3+10]

    if "sha1" in data:
        resp = hashlib.sha1(to_hash).hexdigest()
    elif "sha224" in data:
        resp = hashlib.sha224(to_hash).hexdigest()
    elif "sha256" in data:
        resp = hashlib.sha256(to_hash).hexdigest()
    elif "sha384" in data:
        resp = hashlib.sha384(to_hash).hexdigest()
    elif "sha512" in data:
        resp = hashlib.sha512(to_hash).hexdigest()
    elif "md5" in data:
        resp = hashlib.md5(to_hash).hexdigest()
    
    print resp
    s.send(resp+"\n")

    data = s.recv(1024)
    print(data)
# close the connection
s.close()
