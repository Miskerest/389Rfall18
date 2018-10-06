Writeup 5 - Binaries I
======

Name: Mike Bailey
Section: 0201

I pledge on my honor that I havie not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Mike Bailey

## Assignment 5 Writeup

Starting off, writing out the process for each function on paper made implementing it a lot easier. Having a list of registers available and a drawn map of the stack/memory space made planning out the implementation a lot easier.

For each of the two functions we had to implement, I organized them into familiar structures. First, I made sure the variables were accessible and initialized, such as the counter, source and destination addresses, and pertinent data that was being moved. After this, I made a "loop" tag for each function that would be entered after initialization. After each loop, the function checks whether it should repeat the loop or exit the function via a `cmp` call, comparing the current index/counter with the "final" value (length).

For the memset function, most of the instructions used were just `mov`s and `adds` for moving data around, such as moving the counter to/from registers for comparison. I also used `movzx` for copying the byte over to the destination address to make sure no extra data was being copied over. `movzx` is a standard `mov`, but pads extra data with zeros. 

The strncpy function had a much similar setup area, initializing counter variables and ensuring we had source & destination pointers available. I again decided to use `movzx` to ensure no extraneous data was copied. 

When debugging, I had to switch around some of the register names to adhere to size/width requirements for the specific `mov` operations. For example, `mov byte [rdx], eax` would have worked since I 0-padded `eax` beforehand, but it was trying to copy a 32-bit value to an 8-bit space, so I had to use the last byte of that register (`al`) in order to perform that operation. Little things like this were hiccups in the coding process, but were overall pretty easy to get around. Once I got memset working, it was pretty easy to adapt and modify it to work as strncpy.