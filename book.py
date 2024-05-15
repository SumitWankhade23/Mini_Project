class Book:
    def __init__(self,id = 0, name ="newBook", au='Unknown',a=1):
        self.id = id
        self.name =  name
        self.author = au
        self.availability = a
        
    
    def __str__(self):
        data = str(self.id) +","+ self.name +","+ self.author +","+ str(self.availability)
        return data


if(__name__ == "__main__"):
    b = Book(111,"Wings of Fire" ,'Abdul Kalam',1)
    print(b)