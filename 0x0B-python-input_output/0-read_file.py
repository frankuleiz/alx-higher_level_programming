#!/usr/bin/python3
"""
The ``0-read_file`` module
"""


def read_file(filename=""):
"""A function that reads a file (utf-8) and prints it to the sdtout"""
with open(filename, 'r', encoding='utf-8') as f:
read_data = f.read()
    print(read_data, end='')
