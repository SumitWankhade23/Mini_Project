from os import path
from datetime import datetime

class BookMgmt:

    def addBook(self, b1):
        fp = open("BookInfo.txt","a")
        fp.write(str(b1))
        fp.write("\n")
        fp.close()
    
    def showAllBook(self):
        try:
            fp = open("BookInfo.txt", "r")
        except:
            print("File Not Found..")
        else:
            data = fp.read()
            print(data)
    
    def searchBookById(self, id):
        if(path.exists("BookInfo.txt")):
            with open("BookInfo.txt", "r") as fp:
                flag = False
                for line in fp:
                    data = line.split(",")
                    if(data[0] == str(id)):
                        print("Record found...\n",line)
                        flag = True
                        break     
            
                else: 
            #if(flag ==  False): 
                    print("Record Not Found...")       
        else:
            print("File not found..")  

    def searchBookByName(self, nm):
        if(path.exists("BookInfo.txt")):
            with open("BookInfo.txt", "r") as fp:
                flag = False
                for line in fp:
                    if(nm.lower() in line.lower()):
                        print("Record found...\n",line)
                        flag = True
                        break     
            
                else: 
            #if(flag ==  False): 
                    print("Record Not Found...")       
        else:
            print("File not found..")
    
    def searchBookByAuthor(self,au):
        if(path.exists("BookInfo.txt")):
            with open("BookInfo.txt", "r") as fp:
                flag = False
                for line in fp:
                    if(au.lower() in line.lower()):
                        print("Record found...\n",line)
                        flag = True
                        break     
            
                else: 
            #if(flag ==  False): 
                    print("Record Not Found...")       
        else:
            print("File not found..")
    
    def deleteBookById(self, id):
        booklist=[]
        flag = False

        if(path.exists("BookInfo.txt")):
            with open("BookInfo.txt", "r") as fp:
                for line in fp:
                    data = line.split(",")
                    if(data[0] == str(id)):
                        print("Record found...\n",line)
                        flag = True  
                    else:
                        booklist.append(line)

            fp.close()
            if(flag ==  False): 
                    print("Record Not Found...")      
            else:
                with open("BookInfo.txt", "w") as fp:    
                    for book in booklist:
                        fp.write(book)
                fp.close()
        else:
            print("File not found..")
        
    def editBookById(self, id):
        booklist=[]
        flag = False

        if(path.exists("BookInfo.txt")):
            with open("BookInfo.txt", "r") as fp:
                for line in fp: 
                    data = line.split(",")
                    if(data[0] == str(id)):
                        print("Record found...\n",line)
                        flag = True  
                        ans=input("Do you wish to change Book Name?(Y/N):")
                        if(ans.lower()=='y'):
                            data[1]=input("Enter new Book Name:")

                        ans=input("Do you wish to change Book Author?(Y/N):")
                        if(ans.lower()=='y'):
                            au=input("Enter new Book Author:")
                            data[2]=au

                        line=",".join(data)  
                        line += '\n'
                             
                    booklist.append(line)

            fp.close()
            if(flag ==  False): 
                    print("Record Not Found...")      
            else:
                with open("BookInfo.txt", "w") as fp:    
                    for book in booklist:
                        fp.write(book)
                fp.close()
        else:
            print("File not found..")

    def issueBookById(self,id,nm):
        booklist=[]
        flag = False
        issue= False
        if(path.exists("BookInfo.txt")):
            with open("BookInfo.txt", "r") as fp:
                for line in fp: 
                    data = line.split(",")
                    if(data[0] == str(id)):
                        print("Record found...\n",line)
                        flag=True
                        if(int(data[3])== 1):
                            date_of_issue=input("Enter date of Issue(dd.mm.yy):")
                            Book=str(id) +","+ nm +","+date_of_issue
                            with open("IssueInfo.txt", "a") as fp1:
                               fp1.write(Book)
                               fp1.write('\n')
                            fp1.close()   
                            issue=True
                            data[3]='0\n'
                        else:
                            print("Book not available..")

                    line=",".join(data)  
                    #line += '\n'
                    booklist.append(line)
            fp.close()
            if(flag ==  False): 
                    print("Record Not Found...")      
            if(issue):
                with open("BookInfo.txt", "w") as fp:    
                    for book in booklist:
                        fp.write(book)
                fp.close()
        else:
            print("File not found..") 
    
    def submitBookById(self,id,nm):
        issuelist=[]
        flag = False
        submit= False
        rent_per_day=50
        fine_per_day=10
        limit=7
        if(path.exists("IssueInfo.txt")):
            with open("IssueInfo.txt", "r") as fp:
                for line in fp: 
                    data = line.split(",")
                    if(data[0] == str(id) and data[1].lower() == nm.lower()):
                        print("Record found...\n",line)
                        flag=True
                        date_of_issue=data[2]
                        date_of_submit=input("Enter the date of submit(dd.mm.yy):")
                        date_of_issue=date_of_issue.split('.')
                        yy=int(date_of_issue[2])
                        mm=int(date_of_issue[1])
                        dd=int(date_of_issue[0])
                        date_of_issue=datetime(yy,mm,dd)
                        
                        date_of_submit=date_of_submit.split('.')
                        yy=int(date_of_submit[2])
                        mm=int(date_of_submit[1])
                        dd=int(date_of_submit[0])
                        date_of_submit=datetime(yy,mm,dd)
                        diff=(date_of_submit-date_of_issue)
                        
                        day=diff.days+1
                        print("Total days:",day)
                        if(diff.days > limit): 
                            print("Extra fine for",day-limit,'days')
                            total=(day*rent_per_day) + ((day-limit)*fine_per_day)
                        elif(diff.days > 0 and diff.days < limit): 
                            total=day*rent_per_day
                        else:
                            total=rent_per_day
                       
                        print("You have to pay: ",total,' InR')             
                        submit=True
                    else:
                        issuelist.append(line)   
                    
            fp.close()
            if(flag ==  False): 
                    print("Record Not Found...")      
            if(submit):
                with open("IssueInfo.txt", "w") as fp1:    
                    for user in issuelist:
                        fp1.write(user)
                        #fp1.write('\n')
                fp1.close()
                booklist=[]
                with open("BookInfo.txt", "r") as fp2:
                    for line in fp2: 
                        data = line.split(",")
                        if(data[0] == str(id)):
                            data[3]='1\n'
                            line=','.join(data)
                        booklist.append(line) 
                fp2.close()        
                with open("BookInfo.txt", "w") as fp3:    
                    for book in booklist:
                        fp3.write(book)  
                        #fp3.write('\n')
                fp3.close()
        else: 
            print("File not found..") 
