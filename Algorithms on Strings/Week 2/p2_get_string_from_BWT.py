'''
Problem 2 - Reconstruct a String from its Burrows–Wheeler Transform

Soln: perform inverse Burrows-Wheeler Transform
'''

import sys

#output reconstruct Burrows-Wheeler Transform
def InverseBWT(bwt):
    #sort bwt by letter as firt key and index as second
    bwt_first_col = sorted([(i, c) for i, c in enumerate(bwt)], key=lambda x: (x[1],x[0]))

    #reconstruct text
    final_text = []
    p1 = 0
    end_index = 0
    for i in range(len(bwt)):
        if bwt[p1] == '$': #find where this symbol is located as inputed string ends with this character
            end_index = i
        final_text.append(bwt[p1])
        p1 = bwt_first_col[p1][0]


    return ''.join(final_text[end_index+1:]+final_text[:end_index+1])


if __name__ == '__main__':
    bwt = sys.stdin.readline().strip()
    print(InverseBWT(bwt))
   