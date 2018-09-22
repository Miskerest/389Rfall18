Writeup 3 - Pentesting I
======

Name: Mike Bailey
Section: 0201

I pledge on my honor that I havie not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Mike Bailey

## Assignment 4 Writeup

### Part 1 (45 pts)
The server was indeed vulnerable to command injection. I first connected and ran a ping command just to test the service. After that worked, I then tried pinging google.com, and added a semicolon at the end, followed by `ls`. Lo, and behold, the root filesystem structure was printed out. I looked in `/etc/passwd` for the flag via the input `google.com; cat /etc/passwd` and ended up finding it in `/home/flag.txt` with the input `; cat /home/flag.txt`. 
And the flag is printed out to us, along with the default output of running `$ ping` just as if we had simply run `$ cat /home/flag.txt`. 

And here is our flag: `Good! Here's your flag: CMSC389R-{p1ng_as_a_$erv1c3}`

This command injection works because if you insert a semicolon, it ends the current command. The command in the script is `ping -w 5 -c 2 <input>` allowing you to enter "nested" commands in the $input field. 

I found the script used to run the actual service:

```
#!/bin/bash echo [...] 
echo "Network Administration Panel -- Uptime Monitor "
echo -n "Enter IP address: "
read input >&2 echo "[$(date)] INPUT: $input" 
cmd="ping -w 5 -c 2 $input" 
output=$(eval $cmd) 
echo $output
```

It looks pretty ugly, but it seems to just pipe input into an `eval` command. To make the service more secure, filtering the `$input` variable by passing it through a `grep` regex filter, matching only IP addresses (since that's what the script is supposed to be taking in). Something like:

`$input" cmd="ping -w 5 -c 2 $input | grep \"^\d\.\d\.\d\.\d\$\" " output=$(eval $cmd) echo $output`

To only allow IP address-like input. Alternatively, Fred could sanitize the input some other way, perhaps by wrapping the `ping` call in a Python script that removes all text that allows for injection, such as `;`, `&&`, `||`, et. cetera. He could also use a Python library such as `ping` to prevent programs to be executed from a shell at all. This is likely the safest solution, as there is no opportunity for commands to be injected at all, allowing only actual ping-ing to be done.

### Part 2 (55 pts)

I made the shell by wrapping a simple command parser in a while loop. The command parser checks user input to see if it is equal to `shell`, `exit`, `pull` or `help`. The shell command opens a TCP connection to the server for each new command passed into the shell, executing it by using the vulnerability above. This is performed in another, nested while loop, allowing for consequential commands to be entered and executed on the remote server. 
When sending commands, the format is `; <command>`. The command can be any valid string that would normally execute in a shell. The output of whatever command(s) were sent to the remote machine are then recieved back and printed out to the local shell. Exit quits the shell, and pull pulls a file from the remote server to your local machine. This is done by `cat`ing the file on the remote server and storing it in a buffer locally. The buffer is then written to the output file specified. With regards to the `help` command, in the main shell, if any text entered is not one of the 3 other commands, it will print the help text.
