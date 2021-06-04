'''
Problem 5 - : Find the Shortest Non-Shared Substring of Two Strings

Description: Check the shortet non shared substring in Text1 that is not in Text2

Soln: Constrcut suffix tree of Text1#Text2$ - where # and $ are sumbols
->search suffix tree and find where always see $ len(Text2) digits after #
'''


import sys

def solve (p, q):
	result = p
	return result

p = sys.stdin.readline ().strip ()
q = sys.stdin.readline ().strip ()

ans = solve (p, q)

sys.stdout.write (ans + '\n')