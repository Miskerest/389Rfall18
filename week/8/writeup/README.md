Writeup 8 - Forensics II, Network Analysis and File Carving/Parsing
=====

Name: Mike Bailey
Section: 0201

I pledge on my honor that I have not given or received anyunauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Mike Bailey

## Assignment 8 Writeup

### Part 1 (45 Pts)
1. `csec.umiacs.umd.edu`

2. c0uchpot4doz and laz0rh4x

3. 206.189.113.189 (c0uchpot4doz) and 104.248.224.85 (laz0rh4x). First is from London, the other is from New Jersey.

4. 2749

5. They mentioned some "plans" occurring at 15:00. 

6. https://drive.google.com/file/d/1McOX5WjeVHNLyTBNXqbOde7l8SAQ3DoI/view?usp=sharing, can be read with the "parser" previously exchanged

7. Tomorrow, assumedly at 3:00 PM for their "plans"

### Part 2 (55 Pts)

*Report your answers to the questions about parsing update.fpff below.*

1. Thursday, October 25, 2018 00:40:07 GMT

2. laz0rh4x

3. 9 reported, but there are 11. I allowed the loop in my script to run until it couldn't parse any more data, and it found two extra sections.

4. 

```
------- HEADER -------
MAGIC: 0xdeadbeef
VERSION: 1
TIME: 1540428007
AUTHOR: laz0rh4x
SECTIONS: 9
-------  BODY  -------
Section 0:
type: 9 - ASCII
length: 51
Value: Call this number to get your flag: (422) 537 - 7946


Section 1:
type: 5 - WORDS
length: 60
Value:
(3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9)


Section 2:
type: 6 - COORD
length: 16
(3.7409243980478225e-27, 3.054621934890747)


Section 3:
type: 7 - SEC_REF
length: 4
Value: 1


Section 4:
type: 9 - ASCII
length: 60
Value: The imfamous security pr0s at CMSC389R will never find this!


Section 5:
type: 9 - ASCII
length: 991
Value: The first recorded uses of steganography Can be traced back to 440 BC when Herodotus Mentions two exampleS in his Histories.[3] Histicaeus s3nt a message to his vassal, Arist8goras, by sha9ving the hRead of his most trusted servan-t, "marking" the message onto his scal{p, then sending him on his way once his hair had rePrown, withl the inastructIon, "WheN thou art come to Miletus, bid _Aristagoras shave thy head, and look thereon." Additionally, demaratus sent a warning about a forthcoming attack to Greece by wrIting it dirfectly on the wooden backing oF a wax tablet before applying i_ts beeswax surFace. Wax tablets were in common use then as reusabLe writing surfAces, sometimes used for shorthand. In his work Polygraphiae Johannes Trithemius developed his so-called "Ave-Maria-Cipher" that can hide information in a Latin praise of God. "Auctor Sapientissimus Conseruans Angelica Deferat Nobis Charitas Gotentissimi Creatoris" for example contains the concealed word VICIPEDIA.[4}


Section 6:
type: 6 - COORD
length: 16
(1.6298377578105594e-12, 3.0546178817749023)


Section 7:
type: 1 - PNG
length: 245614


Section 8:
type: 9 - ASCII
length: 22
Value: AF(saSAdf1AD)Snz**asd1


Section 9:
type: 9 - ASCII
length: 45
Value: Q01TQzM4OVIte2gxZGQzbi1zM2N0MTBuLTFuLWYxbDN9



Section 10:
type: 2 - DWORDS
length: 48
Value: (4, 0, 8, 0, 15, 0, 16, 0, 23, 0, 42, 0)

```

5. `CMSC389R-{PlaIN_IfF_FLAG}` (this one was a bit janky), `CMSC389R-{h1dd3n-s3ct10n-1n-f1l3}`, `CMSC389R-{c0rn3rst0ne_airlin3s_to_the_m00n}`
