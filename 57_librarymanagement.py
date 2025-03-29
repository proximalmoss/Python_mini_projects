class library:
    def __init__(self): #simply creating an instance attribute for which we set the initial value
        self.nobooks=0
        self.books=[]
    def addbooks(self,book):
        self.books.append(book)
        self.nobooks=len(self.books)
    def showinfo(self):
        print(f"the library has {self.nobooks} and they are the following: {self.books}")

L1=library()
L1.addbooks("harry potter")
L1.showinfo()