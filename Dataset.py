import csv
class Book:
    def __init__(self,my_list):
        self.my_list=my_list    
    def import_data(self):
        self.data_list=[]
        with open(self.my_list, newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            next(spamreader, None)
            for row in spamreader:
                self.data_list.append(row)
        return self.data_list
    def display(self):
        for row in self.data_list:
            print("Title:",row[0])
            print("Author:",row[1])
            print("Pages:",row[2])
            print("Publisher:",row[3])
            print("Id:",row[4])
            print("Price:",row[5])
