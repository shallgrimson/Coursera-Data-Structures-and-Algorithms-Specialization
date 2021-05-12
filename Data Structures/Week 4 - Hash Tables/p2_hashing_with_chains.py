'''
Problem 2 - Hashing with chains

In this problem you will implement a hash table using the chaining scheme. Chaining is one of the most
popular ways of implementing hash tables in practice. The hash table you will implement can be used to
implement a phone book on your phone or to store the password table of your computer or web service (but
dont forget to store hashes of passwords instead of the passwords themselves

Program should be able to perform following queries
add string
del string
find string
check string

input:bucket size, number of queries, queries
'''
#usd to get inputs
class Query:
    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.data = int(query[1])
        else:
            self.data = query[1]

##used to get hash values
class hasher:
    def __init__(self, x, maxLength, p, m):
        self.hashFunc = [x**i for i in range(maxLength)] #words of max size 15
        self.p = p
        self.m = m #number of buckets

    def getHash(self, word):
        hashNum = 0
        for i in range(len(word)):
            hashNum = hashNum + (ord(word[i])*self.hashFunc[i])
        
        return hashNum % self.p % self.m

#eac node in hash table
class node:
    def __init__(self, word):
        self.word = word
        self.next = None #used for chaining


class hashTable:
    def __init__(self, x, maxLength, p, buckets):
        self.table = [None for i in range(buckets)] 
        self.__h = hasher(x, maxLength,p, buckets) #used to create hash codes
    
    def add(self, word):
        hashValue = self.__h.getHash(word)
        newNode = node(word)
        if self.table[hashValue] != None: #if already value in that bucket inset new node at the head of the linked list
            cur = self.table[hashValue]
            while cur != None:#check if word already in hash table
                if cur.word == word:
                    return 
                cur = cur.next
            newNode.next = self.table[hashValue]

        self.table[hashValue] = newNode
        
    def delete(self, word):
        hashValue = self.__h.getHash(word)
        cur = self.table[hashValue]
        #if head is the word
        if cur!=None and cur.word == word:
            self.table[hashValue] = self.table[hashValue].next
            return
    
        while cur != None:#check if word already in hash table
            if cur.word == word:
                break
                
            prev = cur
            cur = cur.next
        
        if cur == None: #key not present 
            return

        prev.next = cur.next #delete current word

    def find(self, word):
        hashValue = self.__h.getHash(word)
        cur = self.table[hashValue]

        while cur != None:#check if word already in hash table
            if cur.word == word:
                return 'yes'
            prev = cur
            cur = cur.next

        return 'no'
    
    def check(self, index):
        cur = self.table[index]
        fullList =  ''
        while cur != None:#check if word already in hash table
            fullList = fullList + ' ' + cur.word
            cur = cur.next
        
        return fullList[1:]

#read inputs
def read_queries():
    m = int(input())
    n = int(input())
    return m, [Query(input().split()) for i in range(n)]

def main(): 
    m, queries = read_queries()

    wordDict = hashTable(263, 15, 1000000007, m)

    for query in queries:
        if query.type == 'add':
            wordDict.add(query.data)
        elif query.type == 'del':
            wordDict.delete(query.data)
        elif query.type == 'find':
            print(wordDict.find(query.data))
        elif query.type == 'check':
            print(wordDict.check(query.data))


if __name__ == "__main__":
    main()