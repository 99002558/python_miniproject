import csv
class Book:
    def __init__(self,my_list):
        self.my_list=my_list    
    def get_data(self):
        return self.my_list       
data_list=[]
with open('libraryManagement.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    next(spamreader, None)
    for row in spamreader:
        data_list.append(row)    
v=Book(data_list)
