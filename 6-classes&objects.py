#creating the class
class Book:
    def __init__(self, title, author, genre):        #init method to set info/initialize instance of class
        self.title = title
        self.author = author
        self.genre = genre
    def display(self):                               #method to display info about book
        print("Book Title: ", self.title)
        print("Author    : ", self.author)
        print("Genre     : ", self.genre)
        
#creating an instance/ method to set information
book1 = Book("The Tresure Island", "Robert Louis Stevenson", "Adventure")
#method to display information
book1.display()

book2 = Book("Murder on the Orient Express", "Agatha Cristie", "Crime")
book2.display()