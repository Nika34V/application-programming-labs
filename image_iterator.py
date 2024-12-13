import csv

class ImageIterator:
    def __init__(self, annotation_file):
        self.paths = []
        self.index = 0

        with open(annotation_file, 'r') as file:
            reader = csv.reader(file)
            next(reader)  
            for row in reader:
                self.paths.append(row[0])

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.paths):
            raise StopIteration
        path = self.paths[self.index]
        self.index += 1
        return path

    def reset(self):
        self.index = 0

