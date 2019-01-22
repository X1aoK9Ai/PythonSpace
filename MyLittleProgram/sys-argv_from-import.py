#!/usr/bin/python3
# Filename: sys-argv_from-import.py
from sys import argv
print("You can use argv without sys after from..import")
print(argv[1:])
print("You can't use sys.argv after from..import")
print("You can't use other part of sys after from..import either.")
