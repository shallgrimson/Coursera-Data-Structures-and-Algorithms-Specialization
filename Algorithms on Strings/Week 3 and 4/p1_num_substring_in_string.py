'''
Problem 1 - Find All Occurrences of a Pattern in a String

Soln: Knuth–Morris–Pratt algorithm
'''
import sys

#Compute the prefix function
#Description of how well the string matches itself, computes overlap
def compute_prefix_function(P):
    len_p = len(P)
    s = [0 for _ in range(len_p)]
    border = 0
    for i in range(1,len_p):
        while border>0 and P[i] != P[border]:
            border = s[border-1]
            
        if P[i] == P[border]:
            border+=1
        # else:
        #     border = 0
        s[i] = border
    
    return s
    
def find_pattern(pattern, text):
  """
  Find all the occurrences of the pattern in the text
  and return a list of all positions in the text
  where the pattern starts in the text.
  """
  pt = '$'.join([pattern, text])
  s = compute_prefix_function(pt)
  result = []
  for i in range(len(pattern)+1,len(pt)):
      if s[i] == len(pattern):
        result.append(i-2*len(pattern))
  return result


if __name__ == '__main__':
  pattern = sys.stdin.readline().strip()
  text = sys.stdin.readline().strip()
  result = find_pattern(pattern, text)
  print(" ".join(map(str, result)))