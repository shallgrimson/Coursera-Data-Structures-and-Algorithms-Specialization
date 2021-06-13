#quickly time inverse transform

import time
import numpy as np
from p2_suffix_array_long import build_suffix_array
from p3_suffix_array_matching import find_occurrences

def random_string(chars,n):
  # note that chars should be a list, but not include the
  # termination character, i.e. list('ACGT')
  return ''.join(np.random.choice(chars) for _ in range(n)) 


if __name__ == "__main__":
  ibwt_time = 0.0
  n = 3
  for i in range(n):
    text = random_string(['A', 'C', 'G', 'T'], 10000)+'$' #get random string. just test max length
    p = []
    for _ in range(1000):
      p.append(random_string(['A', 'C', 'G', 'T'],10000))
    print('ddd')
    start = time.time()
    ##############
    #build_suffix_array(bwt)
    find_occurrences(text, p)
    ####################
    end = time.time()
    ibwt_time+=(end-start)
    
  print('ibwt avg time: ' + str(ibwt_time/float(n)))
    