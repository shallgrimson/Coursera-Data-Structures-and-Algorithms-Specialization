'''
Problem 4 - Substring equality

Use hashing to answers values about a string
'''
import random


def main():
    m1 = 1000000007
    m2 = 1000000009
    w = input() ##get full string
    n = len(w)
    ##precompute hash function values
    x = 263 ##this should be a random value

    hm1 = [0 for i in range(n+1)] #to make further ahead work use matrix of size n+1
    hm2 = [0 for i in range(n+1)]

    hm1[1], hm2[1] = ord(w[0]), ord(w[0])
    
    
    for i in range(2, n+1):
        hm1[i] = (ord(w[i-1])+x*hm1[i-1])%m1 #this is how mod functions are distributive
        hm2[i] = (ord(w[i-1])+x*hm2[i-1])%m2 #this is how mod functions are distributive
    
    numQuery = input()
    q=[]
    for i in range(numQuery):
        q.append(map(int, input().split()))

    xm1 = [-1 for i in range(n)]
    xm2 = [-1 for i in range(n)]

    for a,b,l in q:
        if xm1[l-1] == -1:
            xm1[l-1] = x**l%m1 #could save this for querires of the same l
            xm2[l-1] = x**l%m2

        hashLeftm1 = (hm1[a+l] - xm1[l-1]*hm1[a])%m1
        hashRightm1 = (hm1[b+l] - xm1[l-1]*hm1[b])%m1

        hashLeftm2 = (hm2[a+l] - xm2[l-1]*hm2[a])%m2
        hashRightm2 = (hm2[b+l] - xm2[l-1]*hm2[b])%m2

        if hashLeftm1 == hashRightm1 and hashLeftm2 == hashRightm2:
            print('Yes')
        else:
            print('No')

if __name__ == "__main__":
    main()
