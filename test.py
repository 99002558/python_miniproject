import unittest
from Dataset import Book

class Calculate(Book)(unittest.TestCase):
     def sort_titles_in_asc(self):
         self.assertEqual() #to check for an expected result
     def sort_titles_in_desc(self): 
         self.assertEqual()  
     def sort_publisher_in_asc(self):
         self.assertEqual() 
     def sort_publisher_in_desc(self):
         self.assertEqual()  
     def sort_global_sales_in_asc(self):
         self.assertEqual()  
     def sort_global_sales_in_desc(self):
         self.assertEqual()      
     def max_critic_score(self):
         self.assertEqual()
     def min_critic_score(self):
         self.assertEqual()   
     def max_user_score(self):
         self.assertEqual()
     def min_user_score(self):
         self.assertEqual()   
     def count_games_by_year(self,year):
         self.assertEqual()  
if __name__ == '__main__':
    unittest.main() #command line interface to test the script         