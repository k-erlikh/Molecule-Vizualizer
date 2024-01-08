import csv
from element import Element, init_element_from_data

class Data:
    def __init__(self):
        self.data = [None] * 10
        self.size = 10

    def load_data(self, path):
        with open(path, newline='') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                elem = Element()
                init_element_from_data(elem, row[0], row[1])
                self.data[elem.name % self.size] = elem
