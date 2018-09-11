Writeup 2 - OSINT (Open Source Intelligence)
======

Name: Mike Bailey
Section: 0201

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Mike Bailey

## Assignment 2 writeup

### Part 1 (45 pts)
1. What is kruegster1990's real name?

Fred Krueger

2. List all personal information (including social media accounts) you can find about him. For each, briefly detail how you discovered them.

https://twitter.com/kruegster1990/ - Twitter. Found by Googling the username.

https://www.instagram.com/kruegster1990/ - Found with namechk

http://www.cornerstoneairlines.co/about.html  - He is the owner of this definitely real airline. He also couldn't be bothered to get a LetsEncrypt certificate...

https://www.reddit.com/user/kruegster1990 - a Reddit account

3. What is the IP address of the webserver hosting his company's site? How did you discover this?

142.93.118.186 - $ nslookup cornerstoneairlines.co

4. List any hidden files or directories you found on this website. Did you find any flags?

/secret listed in robots.txt. Flag found in page source code
/.git found with nmap. I always forget to check for this. Yielded a flag below.

5. Did you find any other IP addresses associated with this website? What do they link to, or where did you find them?

142.93.117.193 - listed in the admin panel.

142.93.118.186 - Actual website 

6. If you found any associated server(s), where are they located? How did you discover this?

142.93.117.193 - Info attained from iplocation.net. Server is located in North Bergen, New Jersey. Hosted by DigitalOcean. Adds up.

142.93.118.186 - Same as above

7. Which operating system is running on the associated server(s)? How did you discover this?

Nmap seems to think both are running a version of Linux v. 3.10-4.8. They are specifically running Ubuntu. I found this out by getting a 404 error and seeing this output: 
`Apache/2.4.18 (Ubuntu) Server at www.cornerstoneairlines.co Port 80`

8. **BONUS:** Did you find any other flags on your OSINT mission? (Up to 9 pts!)

`CMSC389R-{h1dden_fl4g_in_s0urce}` - flag hidden in page source on main website

`CMSC389R-{fly_th3_sk1es_w1th_u5}` - found on his website. Checked robots.txt -> /secrets -> commented out in page source

`CMSC389R-{y0u_found_th3_g1t_repo}` - found on hidden git repo on his website, /.git

`CMSC389R-{dns-txt-rec0rd-ftw}` - found in DNS records for cornerstoneairlines.co

### Part 2 (55 pts)

Running a port scan on the two IP addresses we discovered above, I noticed a service was running on port 1337 on the admin server. True to form, this is what we're supposed to be looking for. The service was a login prompt which asked for a username and password. I modified the stub.py script to brute force the password with rockyou.txt. After running it over the weekend with usernames [kruegster1990, fred, root], I forgot that his email address simply used the name "kruegster." Running my script with this username yielded a hit in about 15 minutes. How convenient...

Now that I had shell (read: container) access, I could look up flight records, which were all kept nicely in the /home directory. From his Instagram, I noted he posted his boarding pass for flight `AAC27670`. So...

```
$ cat /home/flight_records/AAC27670.txt
CMSC389R-{c0rn3rstone-air-27670}
```

Nothing fun in /etc/passwd or /etc/shadow (container). `$ ps -aux` showed nothing special running.
I doubt we're supposed to find any containerd zero-days for this assignment, and with the neutered shell we had in the container I think this was the extent of the exercise. The second ssh server running on port 2222 and HTTP server on 10010 gives me pause though...

I also noted these *quips* from the Docker init script:

```
if [[ $cmd = *"emacs"* ]]; then
            echo "Error: you should really use vim"
        fi
```

and 

```
if [[ $cmd = *"rm -rf"* ]]; then
        echo "No funny business..."
else
        $cmd
fi
```

Also, this line commented out:

# echo "$cmd\n" | nc 129.2.94.135 3321

Looks like a University IP address. Maybe used for logging purposes? The host wasn't up when I scanned it, so I figure it was left over from building the exercise.