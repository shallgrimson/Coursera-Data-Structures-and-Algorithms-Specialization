'''
Phone book
Should be able to handle:
-adding a phone number
-deleting a number
-find a person based on number

Do this using direect addressing
'''
class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]

class phoneDic:
    dic = [-1]*9999999 #could set this to the string 'not found' as well

    def addNumber(self, phoneNumber, name):
        self.dic[phoneNumber] = name
    
    def delNumber(self, phoneNumber):
        self.dic[phoneNumber] = -1
    
    def findNumber(self, phoneNumber):
        if self.dic[phoneNumber] != -1:
            return self.dic[phoneNumber]
        
        return 'not found'
    


def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]

def phone_book():
    book = phoneDic()
    for query in read_queries():
        if query.type == 'add':
            book.addNumber(query.number, query.name)
        elif query.type == 'del':
            book.delNumber(query.number)
        elif query.type == 'find':
            print(book.findNumber(query.number))


if __name__ == "__main__":
    phone_book()
    