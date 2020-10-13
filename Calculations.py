from Dataset import Book
import pandas as pd
class Calculate(Book):
    def __init__(self,my_list):
        super().__init__(my_list)
    def sort_titles_in_asc(self):
        data=self.import_data()
        if data:
            new_list=[]
            for row in data:
                new_list.append(row[0])
            return sorted(new_list)
    def sort_titles_in_desc(self):
        data=self.import_data()
        if data:
            new_list=[]
            for row in data:
                new_list.append(row[0])
            return sorted(new_list,reverse=True)
    def sort_pages_in_asc(self):
        data=self.import_data()
        if data:
            new_list=[]
            for row in data:
                new_list.append(row[2])
            return sorted(new_list)
    def sort_pages_in_desc(self):
        data=self.import_data()
        if data:
            new_list=[]
            for row in data:
                new_list.append(row[2])
            return sorted(new_list,reverse=True)
    def sort_price_in_asc(self):
        data=self.import_data()
        if data:
            new_list=[]
            for row in data:
                new_list.append(row[5])
            return sorted(new_list)
    def sort_price_in_desc(self):
        data=self.import_data()
        if data:
            new_list=[]
            for row in data:
                new_list.append(row[5])
            return sorted(new_list,reverse=True)
    def max_price(self):
        data=self.import_data()
        if data:
            new_list=[]
            for row in data:
                new_list.append(row[5])
            return max(new_list)
    def min_price(self):
        data=self.import_data()
        if data:
            new_list=[]
            for row in data:
                new_list.append(row[5])
            return min(new_list)

data_set=Calculate('libraryManagement.csv')
#print(data_set.sort_titles_in_asc())
#print(data_set.sort_titles_in_desc())
#print(data_set.sort_pages_in_asc())
#print(data_set.sort_pages_in_desc())
#print(data_set.sort_price_in_asc())
#print(data_set.sort_price_in_desc())
#print(data_set.max_price())
print(data_set.min_price())
#print(data_set.max_price())
