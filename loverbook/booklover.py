import pandas as pd

class BookLover: 
    ''' class that manages the evolving booklist for a reader '''
    
    def __init__(self, name, email, fav_genre, num_books=0, book_list=None):
        self.name = name #string type 
        self.email = email #string type - unique identifier
        self.fav_genre = fav_genre #string type 
        self.num_books = num_books #int type 
        self.book_list = pd.DataFrame({
            'book_name':[], 
            'book_rating':[] 
        }) if book_list is None else book_list #dataframe with columns ['book_name', 'book_rating']
    
    def add_book(self, book_name, book_rating): 
        ''' takes in book_name and book_rating and adds an observation to the book_list dataframe '''
        if book_name in self.book_list.book_name.values:
            print("You've already read that one!")
        else:
            if (book_rating > 5) | (book_rating < 0): 
                print("Your rating must be between 0 and 5")
            else: 
                new_book = pd.DataFrame({
                'book_name': [book_name], 
                'book_rating': [book_rating]
                })
                self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
    
    def has_read(self, book_name):
        ''' checks if book is already in book list '''
        return book_name in self.book_list.book_name.values
    
    def num_books_read(self):
        ''' outputs integer value for number of books read '''
        self.num_books = len(self.book_list.book_name)
        return self.num_books
        
    def fav_books(self): 
        ''' returns dataframe of only books rated over 3 '''
        return self.book_list[self.book_list.book_rating > 3]
    
if __name__ == '__main__':

    test_object = BookLover("Hallie Parten", "hallieparten@gmail.com", "nonfiction")
    test_object.add_book("Harry Potter", 5)

