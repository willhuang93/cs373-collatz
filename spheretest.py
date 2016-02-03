#!/usr/bin/env python3

import sys, math

# ----
# main
# ----


"""
% cat RunCollatz.in
1 10
100 200
201 210
900 1000



% RunCollatz.py < RunCollatz.in > RunCollatz.out



% cat RunCollatz.out
1 10 1
100 200 1
201 210 1
900 1000 1



% pydoc3 -w Collatz
# That creates the file Collatz.html
"""
#!/usr/bin/env python3

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2016
# Glenn P. Downing
# ---------------------------

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
    max_c = 1
    s = min(i,j)
    e = max(i,j)
    
    while s != e:
        count = 1
        temp = s
        while temp > 1:
        	if temp%2 == 0:
        		temp = temp/2
        		count = count + 1
        	else:
        		temp = math.floor(temp + temp/2 + 1)
        		count = count + 2


        if count > max_c:
            max_c = count

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
    	if s.strip():
	        i, j = collatz_read(s)
	        v    = collatz_eval(i, j)
	        collatz_print(w, i, j, v)


def main():
	collatz_solve(sys.stdin, sys.stdout)


if __name__ == "__main__" :
	main()