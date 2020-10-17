"""
This class is responsible for various calculations on the game dataset.
"""
from dataset import Game
class Calculate(Game):
    """
    This is a constructor which initialized the base class constructor i.e Game
    """
    def __init__(self, my_list):
        super().__init__(my_list)

    def sort_titles_in_asc(self):
        """
        Function to sort game titles in ascending order.
        """
        data = self.import_data()
        if data:
            new_list = []
            for row in data:
                new_list.append(row[0])
        return sorted(new_list)

    def sort_titles_in_desc(self):
        """
        Function to sort game titles in descending order.
        """
        data = self.import_data()
        if data:
            new_list = []
            for row in data:
                new_list.append(row[0])
        return sorted(new_list, reverse=True)

    def sort_publisher_in_asc(self):
        """
        Function to sort publishers in ascending order.
        """
        data = self.import_data()
        if data:
            new_list = []
            for row in data:
                new_list.append(row[4])
        return sorted(new_list)

    def sort_publisher_in_desc(self):
        """
        Function to sort publishers in descending order.
        """
        data = self.import_data()
        if data:
            new_list = []
            for row in data:
                new_list.append(row[4])
        return sorted(new_list, reverse=True)

    def sort_global_sales_in_asc(self):
        """
        Function to sort global sales in ascending order.
        """
        data = self.import_data()
        if data:
            new_list = []
            for row in data:
                new_list.append(row[9])
        return sorted(new_list)

    def sort_global_sales_in_desc(self):
        """
        Function to sort global sales in descending order.
        """
        data = self.import_data()
        if data:
            new_list = []
            for row in data:
                new_list.append(row[9])
        return sorted(new_list, reverse=True)

    def max_critic_score(self):
        """
        Function to return the maximum critic score.
        """
        data = self.import_data()
        if data:
            new_list = []
            for row in data:
                new_list.append(row[10])
        return max(new_list)

    def min_critic_score(self):
        """
        Function to return the minimum critic score.
        """
        data = self.import_data()
        if data:
            new_list = []
            for row in data:
                new_list.append(row[10])
        return min(new_list)

    def max_user_score(self):
        """
        Function to return the maximum user score.
        """
        data = self.import_data()
        if data:
            new_list = []
            for row in data:
                new_list.append(row[12])
        return max(new_list)

    def min_user_score(self):
        """
        Function to return the minimum user score.
        """
        data = self.import_data()
        if data:
            new_list = []
            for row in data:
                new_list.append(row[12])
        return min(new_list)

    def count_games_by_year(self, year):
        """
        Function to count the games by year by passing year as a parameter.
        """
        data = self.import_data()
        if data:
            new_list = []
            for row in data:
                new_list.append(row[2])
            count = 0
            for x_in_row in new_list:
                if year == x_in_row:
                    count += 1
        return count

    def games_by_publisher(self, publisher):
        """
        Function to return a list of all the games by a certain publisher,
        by passing a publisher as a parameter.
        """
        data = self.import_data()
        if data:
            name_list = []
            publisher_list = []
            game_list = []
            for row in data:
                name_list.append(row[0])
                publisher_list.append((row[4]))
            for index, game in enumerate(publisher_list):
                if game == publisher:
                    game_list.append(name_list[index])
        return game_list

    def games_by_genre(self, genre):
        """
        Function to return a list of all the games by genre by passing a genre as a parameter.
        """
        data = self.import_data()
        if data:
            name_list = []
            genre_list = []
            game_list = []
            for row in data:
                name_list.append(row[0])
                genre_list.append(row[3])
            for index, game in enumerate(genre_list):
                if game == genre:
                    game_list.append(name_list[index])
        return game_list

    def games_by_year(self, year):
        """
        Function to return a list of all games by a specific year,
         by passing a specific year as a parameter.
        """
        data = self.import_data()
        if data:
            name_list = []
            publisher_list = []
            result_list = []
            for row in data:
                name_list.append(row[0])
                publisher_list.append((row[2]))

            for index, y_in_row in enumerate(publisher_list):
                if y_in_row == year:
                    result_list.append(name_list[index])

        return result_list

    def games_by_platform(self, platform):
        """
        Function to return a list of all games on a specific platform,
        by passing a specific platform as a parameter.
        """
        data = self.import_data()
        if data:
            name_list = []
            publisher_list = []
            result_list = []
            for row in data:
                name_list.append(row[0])
                publisher_list.append((row[1]))

            for index, y_in_row in enumerate(publisher_list):
                if y_in_row == platform:
                    result_list.append(name_list[index])

        return result_list

DATASET = Calculate('Video_Games_Sales.csv')
print(DATASET.import_data())
print(DATASET.display())
print(DATASET.sort_titles_in_asc())
print(DATASET.sort_titles_in_desc())
print(DATASET.sort_publisher_in_asc())
print(DATASET.sort_publisher_in_desc())
print(DATASET.sort_global_sales_in_asc())
print(DATASET.sort_global_sales_in_desc())
print(DATASET.max_critic_score())
print(DATASET.min_critic_score())
print(DATASET.count_games_by_year("2004"))
print(DATASET.games_by_publisher("Nintendo"))
print(DATASET.games_by_year("2004"))
print(DATASET.games_by_genre("Sports"))
print(DATASET.games_by_platform("Wii"))
