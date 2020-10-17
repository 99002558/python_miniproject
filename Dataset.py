import csv
class Book:
    def __init__(self, my_list):
        self.my_list = my_list    
    def import_data(self):
        self.data_list = []
        try:
            with open(self.my_list, newline='') as csvfile:
                spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
                next(spamreader, None)
                for row in spamreader:
                    self.data_list.append(row)
        except IOError:
            print("file doesn't exist")
        else:
            return self.data_list
    def display(self):
        for row in self.data_list:
            print("Name:", row[0])
            print("Platform:", row[1])
            print("Year:", row[2])
            print("Genre:", row[3])
            print("Publisher:", row[4])
            print("NASales:", row[5])
            print("EUSales:", row[6])
            print("JPSales:", row[7])
            print("OtherSales:", row[8])
            print("GlobalSales:", row[9])
            print("CriticScores:", row[10])
            print("CriticCount:", row[11])
            print("UserScore:", row[12])
            print("UserCount:", row[13])
            
