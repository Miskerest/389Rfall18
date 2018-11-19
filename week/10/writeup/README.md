Writeup 10 - Crypto II
=====

Name: Mike Bailey
Section: 0201

I pledge on my honor that I have not given or received anyunauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Mike Bailey

## Assignment 10 Writeup

### Part 1 (70 Pts)

This one took some time to get the script working right, but I chose to make the script communicate directly with the digital notary server. The script first sends some data to be signed, "test", sends it, and gets the resulting legit hash. It then updates the fake_md5 hash with the malicious "asdf" data.

Then, the script begins iterating through all possible secret lengths, between 6 and 16 inclusive. For each length, it re-calculates the padding required, and adds it to the end of the message, ensuring that the malicious payload will be aligned with the block properly.

If the "Hmm..." result is detected, it moves on to the next possible secret length. Otherwise, it prints out the server's response, and the hex-encoded version of the payload that worked. Flag got!

`CMSC389R-{i_still_put_the_M_between_the_DV}`


### Part 2 (30 Pts)


Commands to:
* generate keys
 `$ gpg --gen-key`
* importing someone else's public key
 `$ gpg --import <filename>`
* encrypting a message for that someone else and dumping it to a file
 `$ gpg -e [--armor] -r <recipient> <output_file>`

I signed the assignment message with the following command:
  `$ gpg -e --armor -r UMD test`

which outputs to `test.asc`, so I renamed it to `message.private` per instructions.