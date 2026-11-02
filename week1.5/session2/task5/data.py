# Week 1.5, Session 2: Task 5

import math

class Dataset:
    """
    A numeric dataset, loaded from a file.
    """

    def __init__(self, filename=None):
        """
        Creates a Dataset containing data from the specified file.
        If no file is specified, an empty Dataset is created.
        """
        self.data = []
        if filename:
            self.filename = filename
            self.load_data(filename)

    def load_data(self, filename):
        """
        Loads data from the specified file into this Dataset.
        Any existing data will be deleted.
        """
        self.data.clear()

        with open(filename, "r") as f:

            try:
                for line in f:
                    current_line = line.strip()
                    split_into_list = current_line.split()
                    for i in range(0, len(split_into_list)):
                        self.data.append(int(split_into_list[i]))
                self.data.sort()
            except:
                raise TypeError("Only use integers and spaces between them")

    def __len__(self):
        """
        Returns the size of this Dataset.
        """

        return len(self.data)

    def __getitem__(self, index):
        """
        Returns the value at the specified position in this Dataset.
        """
        return self.data[index]

    def mean(self):
        """
        Returns the arithmetic mean of the values in this Dataset.
        """

        total = sum(each for each in self.data)
        return round(total / len(self.data), 1)

    def median(self):
        """
        Returns the median of the values in this Dataset.
        """

        length = len(self.data)
        median = length / 2
        if length % 2 != 0:
            return self.data[int(median)]
        else:  
            return (self.data[int(math.floor(median))] + self.data[int(math.floor(median) + 1)]) / 2

    def __str__(self,):

        response = (
            f"Filename: {self.filename}\n"
        )

        return response



