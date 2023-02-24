#!/usr/bin/python3

#This script aims to repair damaged gzip files.
#The script removes \r and \n that may corrupt the file.
#It is possible that this script may not work for all types of corruption, so i recommend having a backup.
#I am not responsible for any loss of information.

import sys
from pwn import *

if len(sys.argv) < 3:
    print("### FIX GZ ###")
    print("Usage: python3 {} <badfile.gz> <filefixed.gz>".format(sys.argv[0]))
    sys.exit(0)


input_file = sys.argv[1]
output_file = sys.argv[2]

try:
    with open (input_file, "rb") as in_file:

        with open (output_file, "wb") as out_file:
            b1 =  in_file.read(1)
            b2 =  in_file.read(1)
            #print(b1)
            #print(b2)
            pg = log.progress("Analyzing")
            pg.status(".......")
            while b2 != b"":
                pg.status(str(b1))
                if b1 != b"\r" or b2 != b"\n":
                    out_file.write(b1)
                b1 = b2
                b2 = in_file.read(1)
            out_file.write(b1)
        print("\n The file was successfully repaired \n")

except:
    print("### FIX GZ ###")
    print("No such file or directory: '{}'".format(sys.argv[1]))

