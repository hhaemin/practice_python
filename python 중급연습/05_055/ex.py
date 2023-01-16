'''
다음 명세서를 참고해서 도서 관리 프로그램을 만들어보자
-도서 정보(도서명, 가격,isbn)
Book
    속성:name, price, isbn
    
-도서 저장소(도서 컨테이너, 도서 등록, 도서 삭제, 전체 도서 정보 출력, 도서 정보 출력
BookRepository
    속성:bDic
    기능:registBook(), removeBook(), printBookInfo(), printBookInfo()
'''

import book as bk

myBRepository = bk.BookRepository()

myBRepository.registBook(bk.Book('python', 20000, '1234567'))
myBRepository.registBook(bk.Book('c++', 26000, '1230067'))
myBRepository.registBook(bk.Book('java', 21000, '889765'))

myBRepository.printBooksInfo()