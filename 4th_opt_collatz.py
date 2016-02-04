#!/usr/bin/env python3

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2016
# Glenn P. Downing
# ---------------------------
import math
# ------------
# collatz_read
# ------------

def collatz_read (s) :
    """
    read two ints
    s a string
    return a list of two ints, representing the beginning and end of a range, [i, j]
    """
    a = s.split()
    return [int(a[0]), int(a[1])]

# ------------
# collatz_eval
# ------------

def collatz_eval (i, j) :
    """
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    return the max cycle length of the range [i, j]
    """
    # <your code>

    # 10 1000
    # 501 1000
    max_c = 1
    s = min(i,j)
    e = max(i,j)

    assert (s > 0)

    s = math.floor((e / 2 + 1)) if s < (e / 2 + 1) else s

    cache = dict()

    print("S: ", s, "\tE: ", e)
    
    while s <= e:
        count = 1
        temp = s

        # print("CALCULATING:\t\t", temp)
        while temp > 1:
            if temp in cache:
                count = count + cache[temp] - 1
                # print(temp, " is in cache, with value: ", cache[temp], "\tCOUNT: ", count)
                temp = 1

            else:
                # print(temp, " is not in cache with count: ", count)
                if temp % 2 == 0:
                    temp = temp/2
                    count = count + 1
                else:
                    temp = math.floor(temp + temp/2 + 1)
                    count = count + 2
                # print("checking: ", temp, " next with count: ", count)

        cache[s] = count
        # print("cached\t", s," : ",count)
        if count > max_c:
            max_c = count
        # print("")
        s = s + 1
    return max_c

# -------------
# collatz_print
# -------------

def collatz_print (w, i, j, v) :
    """
    print three ints
    w a writer
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    v the max cycle length
    """
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# collatz_solve
# -------------

def collatz_solve (r, w) :
    """
    r a reader
    w a writer
    """
    for s in r :
        i, j = collatz_read(s)
        v    = collatz_eval(i, j)
        collatz_print(w, i, j, v)
