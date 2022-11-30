#!/usr/bin/python3
"""prints the ASCII alphabet, in lowercase, not followed by a new line except q,and e"""

for alphabet in range(97, 123):
    if alphabet != 101 and alphabet != 113:
        print("{}".format(chr(alphabet)), end="")
