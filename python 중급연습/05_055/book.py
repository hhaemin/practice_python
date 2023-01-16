class Book:
    def __init__(self, name, price, isbn):
        self.bName = name
        self.bPrice = price
        self.bIsbn = isbn

class BookRepository:
    def __init__(self):
        self.bDic = {}
        
    def registBook(self, b):
        self.bDic[b.bIsbn] = b
    
    def removeBook(self, isbn):
        del self.bDic[isbn]
        
    def printBooksInfo(self):
        for isbn in self.bDic.keys():
            b = self.bDic[isbn]
            print(f'{b.bName}, {b.bPrice}, {b.bIsbn}')
        
    def printBookInfo(self, isbn):
        if isbn in self.bDic:
            b = self.bDic[isbn]
            print(f'{b.bName}, {b.bPrice}, {b.bIsbn}')
        else:
            print('Lookup result does not exist.')    
        