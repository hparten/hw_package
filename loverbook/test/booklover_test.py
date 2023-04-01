from booklover import BookLover
import unittest

class BookLoverTestSuite(unittest.TestCase): 
    
    def test_1_add_book(self): 
        # add a book and test if it is in `book_list`
        reader1 = BookLover("Hallie", "hallieparten@gmail.com", "nonfiction")
        reader1.add_book("Harry Potter", 5)
        found = "Harry Potter" in reader1.book_list.book_name.values
        self.assertTrue(found)
        
    def test_2_add_book(self): 
        # add the same book twice. Test if it's in `book_list` only once.
        reader1 = BookLover("Hallie", "hallieparten@gmail.com", "nonfiction")
        reader1.add_book("Harry Potter", 5)
        reader1.add_book("Harry Potter", 5)
        Expected = 1
        Actual = reader1.book_list.shape[0]
        self.assertEqual(Expected, Actual)
        
    def test_3_has_read(self):
        # pass a book in the list and test if the answer is `True`.
        reader1 = BookLover("Hallie", "hallieparten@gmail.com", "nonfiction")
        reader1.add_book("Harry Potter", 5)
        yes = reader1.has_read("Harry Potter")
        self.assertTrue(yes)
        
    def test_4_has_read(self):
        # pass a book NOT in the list and use `assert False` to test the answer is `True
        reader1 = BookLover("Hallie", "hallieparten@gmail.com", "nonfiction")
        no = reader1.has_read("Lord of the Rings")
        self.assertFalse(no)
        
    def test_5_num_books_read(self):
        # add some books to the list, and test num_books matches expected.
        reader1 = BookLover("Hallie", "hallieparten@gmail.com", "nonfiction")
        reader1.add_book("Harry Potter 1", 5)
        reader1.add_book("Harry Potter 2", 3)
        reader1.add_book("Harry Potter 3", 5)
        Expected = 3 
        Actual = reader1.num_books_read()
        self.assertEqual(Expected, Actual)
        
    def test_6_fav_books(self): 
        # add some books with ratings to the list, making sure some of them have rating > 3. 
        # Your test should check that the returned books have rating  > 3
        reader1 = BookLover("Hallie", "hallieparten@gmail.com", "nonfiction")
        reader1.add_book("Harry Potter 1", 5)
        reader1.add_book("Harry Potter 2", 3)
        reader1.add_book("Harry Potter 3", 2)
        reader1.add_book("Harry Potter 4", 4)
        Expected = 2
        Actual = reader1.fav_books().shape[0]

if __name__ == '__main__':

    unittest.main(verbosity=3)