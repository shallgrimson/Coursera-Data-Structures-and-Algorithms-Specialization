'''
Problem 1 - Burrow-wheeler transform
'''

import sys

#Return burrow-wheeler transform
def BWT(text):
    #get set of cycle rotations
    cyc_rot = []
    for i in range(len(text)):
        cyc_rot.append(text[i:]+text[:i])
    
    #I could implement this myself but whatever
    cyc_rot.sort()
    
    return ''.join([cyc_rot[i][-1] for i in range(len(text))])

if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    #text = 'ACACACAC$' #output: CCCC$AAAA
    #text = 'AGACATA$'  #output: ATG$CAAA
    print(BWT(text))

