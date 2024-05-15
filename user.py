from bookMgmt import BookMgmt

def userMenuMgmt(uname):
    bookMgmt = BookMgmt()
    ch = 0 
    while(ch != 10):
        print('''
            1. Show All Books
            2. Search Book by Id
            3. Search Book by Name
            4. Search Book by Author
            5. Issue Book by Id
            6. Submit Book
            10. Exit
        ''')

        ch = int(input("Enter your choice: "))
        if(ch == 1):
            bookMgmt.showAllBook()

        elif(ch == 2):
            id = int(input("Enter Book Id to search: ")) 
            bookMgmt.searchBookById(id)

        elif(ch == 3):
               nm = input("Enter Book Name to search: ")
               bookMgmt.searchBookByName(nm)
        
        elif(ch == 4):
            nm = input("Enter Book Author to search: ")
            bookMgmt.searchBookByAuthor(nm)  

        elif(ch == 5):
             id = int(input("Enter Book Id to Issue that book:")) 
             bookMgmt.issueBookById(id,uname)

        elif(ch == 6):
             id = int(input("Enter Book Id to Submit that book:")) 
             bookMgmt.submitBookById(id,uname)     
        
        elif(ch == 10):
            print("Thank you...")
            
        else:
            print("Invalid Choice..")

if(__name__ == "__main__"):
    userMenuMgmt() 