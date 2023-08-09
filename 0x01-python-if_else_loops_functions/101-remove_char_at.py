#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0:
        return str
    count = 0
    copy = ""
    for element in str:
        if count == n:
            count += 1
            continue
        copy += str[count]
        count += 1
    return copy
