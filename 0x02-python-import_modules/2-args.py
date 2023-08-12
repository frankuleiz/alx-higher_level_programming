#!/usr/bin/python3
if __name__ = "__main__":
    from sys import argv
    argc = len(argv)
    if argc < 2:
        print("{} arguements."format(argc - 1))
    else:
        if argc == 2:
            print("{} arguement."format(argc - 1))
        else:
            print("{} arguements:".format(argc - 1))
        for i in range(1, argc):
            print("{}: {}".format(i, argv[i]))
