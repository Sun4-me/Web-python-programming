class Book:

    def __init__(self, title, authors, publisher, isbn, price):
        self.title = title
        self.authors = authors[:]
        self.publisher = publisher
        self.ISBN = isbn
        self.price = price
    
    def __str__(self):
        rep = " Title: {0}\n Authors: {1}\n Publisher: {2}\n ISBN: {3}\n Price: {4}".format(self.title, self.authors, self.publisher, self.ISBN, self.price)
        return rep

    def __eq__(self, other):
        return self.ISBN == other.ISBN

    def num_authors(self):
        return len(self.authors)

python_book = Book("Practical Programing",["A","B","C"],"SUN","12-1",300)
print(python_book)


