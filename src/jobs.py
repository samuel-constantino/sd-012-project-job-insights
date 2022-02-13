import csv
from functools import lru_cache


@lru_cache
def read(path):
    # script baseado na resolução de Roberval Filho:
    # https://github.com/tryber/sd-012-project-job-insights/pull/28/files
    with open(path) as file:
        file_reader = csv.DictReader(file, delimiter=",", quotechar='"')

        file_content = []
        for row in file_reader:
            file_content.append(row)

    return file_content
