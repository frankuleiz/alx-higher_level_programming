#!/usr/bin/python3
"""The ``0-read_file`` module"""


def read_file(filename=""):
"""A function that reads a text file(utf-8) and prints to stdout"""
    with open(filename, "r", encoding = "utf-8") as f:
        read_data = f.read()
        print(read_data, end="")

