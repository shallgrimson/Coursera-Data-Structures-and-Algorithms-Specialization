#quickly time inverse transform

import time
import numpy as np
from p2_get_string_from_BWT import InverseBWT
from p1_burrow_wheeler_transform import BWT
from p3_match_in_compressed_string import PreprocessBWT, CountOccurrences
from p4_suffix_array import build_suffix_array

def random_string(chars,n):
  # note that chars should be a list, but not include the
  # termination character, i.e. list('ACGT')
  return ''.join(np.random.choice(chars) for _ in range(n)) 


if __name__ == "__main__":
  ibwt_time = 0.0
  n = 3
  for i in range(n):
    bwt = random_string(['A', 'C', 'G', 'T'], 10000)+'$' #get random string. just test max length
    # p = []
    # for _ in range(1000):
    #   p.append(random_string(['A', 'C', 'G', 'T'], 5000))
    
    start = time.time()
    ##############
    r = build_suffix_array(bwt)
    # let_index = {'A':0,'C': 1,'G':2,'T':3}
    # starts, occ_counts_before = PreprocessBWT(bwt, let_index)
    # for pattern in p:
    #   CountOccurrences(pattern, bwt, starts, occ_counts_before, let_index)
    ####################
    end = time.time()
    ibwt_time+=(end-start)
    
  print('ibwt avg time: ' + str(ibwt_time/float(n)))
    