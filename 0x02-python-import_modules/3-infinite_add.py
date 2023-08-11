#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    i = len(sys.argv)
    sum = 0
    for i in range(1, i):
        sum += int(sys.argv[i])
    print(sum)
