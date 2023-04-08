import csv
import numpy as np
import math


filename = "C:/Users/Shrrrr/OneDrive/Desktop/Coderush-Challangeproject/Task-2/file.csv"

with open(filename, "r") as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader) # Skip header row
    for row in csv_reader:
        # Do something with each row
        benford_test(row[0])

