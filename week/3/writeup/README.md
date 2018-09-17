Writeup 3 - OSINT II, OpSec and RE
======

Name: Mike Bailey
Section: 0201

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Mike Bailey

## Assignment 3 Writeup

### Part 1 (100 pts)


#### 1. Readable Git Repository 

The first issue that should be addressed is the Git repository that's present on the main website. Giving everyone in the world access to this repository could provide potential attackers with information regarding how your webserver's backend is configured. This could allow for malicious parties to discover attack vectors against your site. This is in part due to the fact that the Git repo shows commit log history, and if there was ever sensitive info or files that were present in the repository, the attacker would now know where to look for them. Someone might even be able to discern entire parts of code that manage the service running, such as database passwords, hardcoded sensitive information, etc.

#### 2. Open/Cleartext Remote Access 

Next up is the remote access server running on port 1337 on the "admin" host. This service's port is open to the world and seemingly unfiltered. While it only provides access to a container, this container has `essential flight info` on it that could be a security risk if compromised. I mean like, hijacking-a-plane-security. The communications over this service are also unencrypted, INCLUDING username/password transmission. This means that anyone monitoring traffic in between the client and the server could easily extract the admin credentials.


#### 3. Password Complexity

Lastly, the password used to access the administration console shell is way too weak. Not only does it consist of only 7 all lowercase letters, it's a common word/phrase that's present in a lot of wordlists. It also wouldn't be too difficult to guess if you follow Fred's Instagram. This makes it highly susceptible to brute force attacks using a wordlist, and even if a hashed version of the password got out, it would be easily crackable. Not to mention, if the attacker used a wordlist-generator like Bewgor, it would likely be one of the first attempted passwords. The username should likely also be different than the one used for his public email address.