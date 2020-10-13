from Dataset import Game
import pandas as pd
class Calculate(Game):
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
            for index,game in enumerate(publisher_list):
                if game==publisher:
                    game_list.append(name_list[index])       
            return game_list

    def games_by_genre(self,genre):
        data=self.import_data()
        if data:
            name_list=[]
            genre_list=[]
            game_list=[]
            for row in data:
                name_list.append(row[0])
                genre_list.append(row[3])
            for index,game in enumerate(genre_list):
                if game==genre:
                    game_list.append(name_list[index])
            return game_list

    def games_by_year(self,year):
        data=self.import_data()
        if data:
            name_list=[]
            publisher_list=[]
            result_list=[]
            for row in data:
                name_list.append(row[0])
                publisher_list.append((row[2]))
            
            for index,y in enumerate(publisher_list):
                if y==year:
                    result_list.append(name_list[index])
                    
            return result_list

    def games_by_Platform(self,Platform):
        data=self.import_data()
        if data:
            name_list=[]
            publisher_list=[]
            result_list=[]
            for row in data:
                name_list.append(row[0])
                publisher_list.append((row[1]))
            
            for index,y in enumerate(publisher_list):
                if y==Platform:
                    result_list.append(name_list[index])
                    
            return result_list






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
#print(data_set.games_by_publisher("Nintendo"))
#print(data_set.games_by_year("2004"))
#print(data_set.games_by_genre("Sports"))
#print(data_set.games_by_Platform("Wii"))

