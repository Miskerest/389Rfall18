#!/usr/bin/env python2
# from the git repo
import md5py
import socket

#####################################
### STEP 1: Calculate forged hash ###
#####################################

host = "142.93.118.186"
port = 1234

message = 'test'    # original message here

# connect to server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

s.recv(4096) # main prompt
s.send("1\n") # sign some data
s.recv(4096) # get prompt
s.send(message+"\n") # send message to be signed
legit = s.recv(4096) # get  hash
legit = legit[legit.index("hash: ")+6:-1] #get actual hash

# initialize hash object with state of a vulnerable hash
fake_md5 = md5py.new('A' * 64)
fake_md5.A, fake_md5.B, fake_md5.C, fake_md5.D = md5py._bytelist2long(legit.decode('hex'))

malicious = 'asdf'  # put your malicious message here

# update legit hash with malicious message
fake_md5.update(malicious)

# fake_hash is the hash for md5(secret + message + padding + malicious)
fake_hash = fake_md5.hexdigest()
print(fake_hash)



s.recv(4096) # get main prompt
#############################
### STEP 2: Craft payload ###
#############################

for i in range (6,17):


    # TODO: calculate proper padding based on secret + message
    # secret is <redacted> bytes long (48 bits)
    # each block in MD5 is 512 bits long
    # secret + message is followed by bit 1 then bit 0's (i.e. \x80\x00\x00...)
    # after the 0's is a bye with message length in bits, little endian style
    # (i.e. 20 char msg = 160 bits = 0xa0 = '\xa0\x00\x00\x00\x00\x00\x00\x00\x00')
    # craft padding to align the block as MD5 would do it
    # (i.e. len(secret + message + padding) = 64 bytes = 512 bits
    msglen = len(message)
    padding = "\x80" + "\x00"*(64-(msglen+i+9)%64) + chr((msglen+i)*8) +'\x00'*7

    # payload is the message that corresponds to the hash in `fake_hash`
    # server will calculate md5(secret + payload)
    #                     = md5(secret + message + padding + malicious)
    #                     = fake_hash
    payload = message + padding + malicious

    # send `fake_hash` and `payload` to server (manually or with sockets)
    # REMEMBER: every time you sign new data, you will regenerate a new secret!

    print "trying payload: %s" % payload
    s.send("2\n") # verify some data
    s.recv(4096)  # "input hash...""
    s.send(fake_hash+"\n") # send hash
    s.recv(4096) # "input data...."
    s.send( "\\x" + ("\\x".join("{:02x}".format(ord(c)) for c in payload))+"\n") # send data
    ret = s.recv(99999)
    ret += s.recv(90009)
    #print ret
    if "CMSC389R-" in ret:
        print "FOUND AT INDEX: %d" % i
        print ret
        print "\\x" + ("\\x".join("{:02x}".format(ord(c)) for c in payload))
        break
    elif "Hmm" in ret:
        pass
    else:
        print "WHAT: " + ret
   