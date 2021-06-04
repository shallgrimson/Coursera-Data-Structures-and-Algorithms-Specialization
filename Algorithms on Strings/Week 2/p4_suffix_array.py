'''
Problem 4 - Construct the Suffix Array of a String

Soln: just found each suffix, lexicographically them, and then put the index of each first character relative to text in a array
'''

import sys


def build_suffix_array(text):
  """
  Build suffix array of the string text and
  return a list result of the same length as the text
  such that the value result[i] is the index (0-based)
  in text where the i-th lexicographically smallest
  suffix of text starts.
  """
  indexs = [i for i in range(len(text))] #array to hold index of each integer, to be sorted based on suffix array
  suffixs = []
  for i in range(len(text)):
    suffixs.append(text[i:]+text[:i])
  
  result = [x for _, x in sorted(zip(suffixs, indexs), key=lambda pair: pair[0])] #create suffix array
  
  return result


if __name__ == '__main__':
  text = sys.stdin.readline().strip()
  print(" ".join(map(str, build_suffix_array(text))))