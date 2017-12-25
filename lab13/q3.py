import random

class Patron:
    def __init__(self, name, accountnum=None):
        self.name=name
        self.accountnum=accountnum
        self.booklist=[]

    def __repr__(self):
        list=''
        for book in self.booklist:
            list=list+book+"\n"
        return "Library Patron Information: \n"+"Name: "+self.name+'\n' +"Library Account Number: "+ str(self.accountnum)+'\n' +"Borrowed Books: "+'\n'+ list

class Library:
    def __init__(self,name,location):
        self.name=name
        self.location=location
        self.patronlist=[]
        self.availbooks=[]

    def add_patron(self,name):
        num = random.randint(10000, 99999)
        for object in self.patronlist:
            if num == object.accountnum:
                num = random.randint(10000, 99999)
        name.accountnum=num
        self.patronlist.append(name)

    def lend_book(self, name, book):
        inlist = False
        bookinlist=False
        for object in self.patronlist:
            while object == name:
                inlist = True
                for name in self.availbooks:
                    if book == name:
                        booklinlist=True
                        object.booklist.append(book)
                        self.availbooks.remove(book)
                if bookinlist==False:
                    print(book, " is not available")
        if inlist == False:
            print(name.name, " is not in the system")

    def add_book(self,name):
        self.availbooks.append(name)

    def __repr__(self):
        booklist=''
        for book in self.availbooks:
            booklist = booklist + book + "\n"
        return "Name: "+self.name+'\n'+"Location: "+self.location+'\n'+"Available Books: "+booklist+"Patron List: \n"+str(self.patronlist)

def main():
    bk_library=Library("Brooklyn Public Library","6 Metrotech Center")
    bk_library.add_book("Ender's Game")
    bk_library.add_book("Ender's Shadow")
    bk_library.add_book("Shadow of the Hegemon")
    bk_library.add_book("Ready Player One")
    bk_library.add_book("The Outsiders")
    bk_library.add_book("Flowers for Algernon")
    print(bk_library)
    bob=Patron('Bob')
    print(bob.accountnum)
    bk_library.add_patron(bob)
    print(bob.accountnum)
    print(bk_library)
    shuyu=Patron('shuyu')
    bk_library.lend_book(shuyu, "Old Man's War")
    bk_library.add_patron(shuyu)
    bk_library.lend_book(shuyu, "Ender's Game")
    bk_library.lend_book(bob,"Ender's Game")
    print(bk_library)


main()