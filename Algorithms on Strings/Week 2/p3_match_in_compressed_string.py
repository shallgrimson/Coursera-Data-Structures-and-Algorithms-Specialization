'''
Problem 3 - Matching against a compressed string

Perform patten matching on Burrows-Wheeler transform, pattern is really matched against the original text but do not need to transform back

'''

import sys


def PreprocessBWT(bwt, let_index):
  """
  Preprocess the Burrows-Wheeler Transform bwt of some text
  and compute as a result:
    * starts - for each character C in bwt, starts[C] is the first position 
        of this character in the sorted array of 
        all characters of the text.
    * occ_count_before - for each character C in bwt and each position P in bwt,
        occ_count_before[C][P] is the number of occurrences of character C in bwt
        from position 0 to position P inclusive.
  """
  starts = {}
  occ_counts_before = [[0 for _ in range(len(let_index))] for __ in range(len(bwt)+1)] ###maybe just need to store every occurence??
  for i,c  in enumerate(bwt):
    if c not in starts:
      starts[c] = i
    #this is probably very slow
    occ_counts_before[i+1][:] = occ_counts_before[i][:]
    if c != '$': #we know only one of these so to save space don't save it
        occ_counts_before[i+1][let_index[c]]+=1
    
      


  return starts, occ_counts_before


def CountOccurrences(pattern, bwt, starts, occ_counts_before, let_index):
  """
  Compute the number of occurrences of string pattern in the text
  given only Burrows-Wheeler Transform bwt of the text and additional
  information we get from the preprocessing stage - starts and occ_counts_before.
  """
  top = 0
  bottom = len(bwt)-1
  pat_ind = len(pattern)-1
  while top <= bottom:
    if pat_ind >= 0:
      c = pattern[pat_ind]
      pat_ind-=1
      col = let_index[c]
    #   if c=='$':
    #       top, bottom = starts[c], starts[c]#only occurs once
    #       continue
      top = starts[c] + occ_counts_before[top][col]
      bottom = starts[c] + occ_counts_before[bottom+1][col]-1
    else:
      return bottom-top+1
            
  return 0 #not found
     


if __name__ == '__main__':
  bwt = sys.stdin.readline().strip()
  pattern_count = int(sys.stdin.readline().strip())
  patterns = sys.stdin.readline().strip().split()
  # Preprocess the BWT once to get starts and occ_count_before.
  # For each pattern, we will then use these precomputed values and
  # spend only O(|pattern|) to find all occurrences of the pattern
  # in the text instead of O(|pattern| + |text|).  
  let_index = {'A':0,'C': 1,'G':2,'T':3} #index for each letter in bwt, per problem only 4 used
  starts, occ_counts_before = PreprocessBWT(bwt, let_index)
  occurrence_counts = []
  for pattern in patterns:
    occurrence_counts.append(CountOccurrences(pattern, bwt, starts, occ_counts_before, let_index))
  print(' '.join(map(str, occurrence_counts)))