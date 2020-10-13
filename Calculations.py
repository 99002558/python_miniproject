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
    def sort_publisher_in_asc(self):
        data=self.import_data()
        if data:
            new_list=[]
            for row in data:
                new_list.append(row[4])
            return sorted(new_list)
    def sort_publisher_in_desc(self):
        data=self.import_data()
        if data:
            new_list=[]
            for row in data:
                new_list.append(row[4])
            return sorted(new_list,reverse=True)
    def sort_global_sales_in_asc(self):
        data=self.import_data()
        if data:
            new_list=[]
            for row in data:
                new_list.append(row[9])
            return sorted(new_list)
    def sort_global_sales_in_desc(self):
        data=self.import_data()
        if data:
            new_list=[]
            for row in data:
                new_list.append(row[9])
            return sorted(new_list,reverse=True)
    def max_critic_score(self):
        data=self.import_data()
        if data:
            new_list=[]
            for row in data:
                new_list.append(row[10])
            return max(new_list)
    def min_critic_score(self):
        data=self.import_data()
        if data:
            new_list=[]
            for row in data:
                new_list.append(row[10])
            return min(new_list)

data_set=Calculate('Video_Games_Sales.csv')
print(data_set.sort_titles_in_asc())
print("**************************************************************************************************************************")
print(data_set.sort_titles_in_desc())
print("**************************************************************************************************************************")
print(data_set.sort_publisher_in_asc())
print("**************************************************************************************************************************")
print(data_set.sort_publisher_in_desc())
print("**************************************************************************************************************************")
print(data_set.sort_global_sales_in_asc())
print("**************************************************************************************************************************")
print(data_set.sort_global_sales_in_desc())
print("**************************************************************************************************************************")
print(data_set.max_critic_score())
print("**************************************************************************************************************************")
print(data_set.min_critic_score())
print("**************************************************************************************************************************")

