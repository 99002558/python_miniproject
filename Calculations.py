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
    def max_user_score(self):
        data=self.import_data()
        if data:
            new_list=[]
            for row in data:
                new_list.append(row[12])
            return max(new_list)
    def min_user_score(self):
        data=self.import_data()
        if data:
            new_list=[]
            for row in data:
                new_list.append(row[12])
            return min(new_list)
    def count_games_by_year(self,year):
        data=self.import_data()
        if data:
            new_list=[]
            for row in data:
                new_list.append(row[2])
            count=0
            for x in new_list:
                if year==x:
                    count+=1
            return count
    def games_by_publisher(self,publisher):
        data=self.import_data()
        if data:
            name_list=[]
            publisher_list=[]
            game_list=[]
            for row in data:
                name_list.append(row[0])
                publisher_list.append((row[4]))
            for x in publisher_list:
                if x==publisher:
                    index_of_pub=x.index(publisher)
                    val=name_list[index_of_pub]
                    game_list.append(val)
            return game_list



data_set=Calculate('Video_Games_Sales.csv')
#print(data_set.sort_titles_in_asc())
#print(data_set.sort_titles_in_desc())
#print(data_set.sort_publisher_in_asc())
#print(data_set.sort_publisher_in_desc())
#print(data_set.sort_global_sales_in_asc())
#print(data_set.sort_global_sales_in_desc())
#print(data_set.max_critic_score())
#print(data_set.min_critic_score())
#print(data_set.count_games_by_year("2004"))
print(data_set.games_by_publisher("Nintendo"))
