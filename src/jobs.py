import csv
from functools import lru_cache


@lru_cache
def read(path):
    with open(path) as file:
        file_reader = csv.DictReader(file, delimiter=",", quotechar='"')

        file_content = []
        for row in file_reader:
            file_content.append(row)

    return file_content
