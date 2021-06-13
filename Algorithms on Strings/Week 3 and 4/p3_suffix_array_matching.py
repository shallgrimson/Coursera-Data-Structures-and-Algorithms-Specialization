'''
Problem 3 - Pattern Matching with the Suffix Array

In this problem, we will let you use the suffix array to solve the Multiple Pattern Matching Problem. This
is what actually happens when one needs to solve the pattern matching problem for a massive string like
the human genome: instead of downloading the genome itself, one downloads its suffix array and solves the
pattern matching problem using the array.
'''
import sys

'''
This is from problem 2
'''
###############################################################################
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
###############################################################################
#find number of occurences in a pattern
def find_occurrences(text, patterns):
    text = text + '$'
    occs = set()
    suffix_array = build_suffix_array(text)
    tn = len(text)
    for p in patterns:
        pn = len(p)
        check = False
        for i in suffix_array:
            pi = 0
            ti = i
            #see if we can find our pattern
            while ti < tn and p[pi] == text[ti]:
                check = True
                if pi == pn-1:
                    occs.add(i)
                    break
                pi+=1
                ti+=1
                
            #suffix array sorted lexicographically, therefore if ord(p[pi]) < ord(text[ti]) we have already passed the chance of finding out pattern
            #use check so don't always have to compare ord
            if check == True and ord(p[pi]) < ord(text[ti]): #not sure if worth the time savings
              break
                
            

    return occs

if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    pattern_count = int(sys.stdin.readline().strip())
    patterns = sys.stdin.readline().strip().split()
    #text, pattern_count, patterns = 'AAA', 1, ['A']
    #text, pattern_count, patterns = 'ATA', 3, ['G','C', 'C']
    #text, pattern_count, patterns = 'ATATATA', 3, ['ATA','C', 'ATATATATA']
    occs = find_occurrences(text, patterns)
    print(" ".join(map(str, occs)))