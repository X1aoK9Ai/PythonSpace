#!/usr/bin/python3
# Filename: sys-argv_import.py
import sys
print("You can only use sys.argv after import the whole sys:")
print(sys.argv[1:])
print("You can't use argv without sys. before from..import.")
