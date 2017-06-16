import os
import os.path
import csv
def read_csv_file(file_path):
    # read a file and parse the data as a json object or dictionary to the template
    """                      The File Template Look
    date | time | home_team | vs | Away_team | prediction | odds |
    """
    # so like first check that the file is existent and that ii is a csv file format
    # then we can create a like generator function that yields each row in the csv at a time

    csv_handler = csv.reader(open('Book1.csv', newline=''))
    for row in csv_handler:
        yield(row)