
######REPLACE LEN(S) WITH N########

'''
Problem 2 - Construct the Suffix Array of a Long String


The goal in this problem is to construct the suffix array of a given string again, but this time for a longer
string. In particular, a quadratic algorithm will not fit into the time limit in this problem. This will require you
to implement an almost linear algorithm bringing you close to the state-of-the-art algorithms for constructing
suffix arrays.

Soln: week 4 slides
'''

import sys

#return character index of character, $=0,A=1,B=2.....
def get_character_index(c):
    if c == '$': #COULD JUST PUT THIS DIRECTLY INTO COUNT SINCE KNOW IT WILL BE LAST POSITION
        return 0
    return ord(c)-64 #ord('A')=65, then set A as index 1
    
#sort charactes in text using count sort
#could directly add $ into this!!!!!
def sort_characters(S):
    order = [0 for _ in range(len(S))]
    count = [0 for _ in range(26)] #26 letters in the alphabet
    
    for c in S:
        count[get_character_index(c)]+=1 #ord('A')=65
    for j in range(1, 26):
        count[j] = count[j-1] + count[j]
        
    for i in range(len(S)-1,-1,-1):
        c=get_character_index(S[i]) #could seperate this in its own function
        count[c] -= 1
        order[count[c]] = i
    
    return order

#sort charcters of string into similar groups
def compute_char_classes(S, order):
    char_classes = [0 for _ in range(len(S))]
    char_classes[order[0]] = 0
    for i in range(1, len(S)):
        if S[order[i]] != S[order[i-1]]:
            char_classes[order[i]] = char_classes[order[i-1]]+1
        else:
            char_classes[order[i]] = char_classes[order[i-1]]
    
    return char_classes
    
    
def sort_double(S,L,order,char_classes):
    count = [0 for _ in range(len(S))]
    newOrder = [0 for _ in range(len(S))]
    for i in range(len(S)):
        count[char_classes[i]] = count[char_classes[i]]+1
    for j in range(1,len(S)):
        count[j] = count[j]+count[j-1]
    
    for i in range(len(S)-1,-1,-1):
        start = (order[i]-L+len(S))%len(S)
        cl = char_classes[start]
        count[cl] = count[cl] - 1
        newOrder[count[cl]] = start
    
    return newOrder

def update_classes(newOrder, char_classes, L):
    n = len(newOrder)
    newCharClass = [0]*n
    newCharClass[newOrder[0]] = 0
    for i in range(1, n):
        prev, cur = newOrder[i-1], newOrder[i]
        midPrev, mid = (prev+L)%n,(cur+L)%n
        if char_classes[cur] != char_classes[prev] or char_classes[mid] != char_classes[midPrev]:
            newCharClass[cur] = newCharClass[prev]+1
        else:
            newCharClass[cur] = newCharClass[prev]
    
    return newCharClass

def build_suffix_array(text):
  """
  Build suffix array of the string text and
  return a list result of the same length as the text
  such that the value result[i] is the index (0-based)
  in text where the i-th lexicographically smallest
  suffix of text starts.
  """
  order = sort_characters(text)
  char_classes = compute_char_classes(text, order)
  L = 1
  while L < len(text):
      order = sort_double(text,L,order,char_classes)
      char_classes = update_classes(order,char_classes,L)
      L=2*L
  # Implement this function yourself
  return order


if __name__ == '__main__':
  text = sys.stdin.readline().strip()
  print(" ".join(map(str, build_suffix_array(text))))

