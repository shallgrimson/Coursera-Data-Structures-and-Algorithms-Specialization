'''
Problem 3 - Implement Rabin Karps algorithm
'''
def print_occurrences(output):
    print(' '.join(map(str, output)))

#this can be sped up through continously finding the hash value
def find_hash_value(string):
    x = 263
    m = 1000000009
    hs = 0
    for i in range(len(string)):
        hs = (hs*x + ord(string[i]))%m

    return hs

def main():
    indexes = []
    pattern = input()
    string = input()
    n = len(pattern)
    hp = find_hash_value(pattern) #get has value of pattern

    for i in range(len(string)-len(pattern)+1):
        substr = string[i:i+n]
        hs = find_hash_value(substr) #this could be sped up

        if hs == hp:
            cnt = 0
            for j in range(n):
                if pattern[j] != substr[j]:
                    break
                cnt+=1
            
            if cnt == n:
                indexes.append(i)
    
    return print_occurrences(indexes)
        


if __name__ == '__main__':
    main()