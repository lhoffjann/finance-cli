from dataclasses import dataclass, field
import csv
from csv import DictReader
from transaction import Transaction
csv_file = '/home/lennart/Documents/.finances/export.csv' #TODO: This should be moved into a config file

def import_transaction_from_csv(csv_file):
    with open(csv_file) as read_obj:
        csv_dict_reader = DictReader(read_obj) 
        csv_reader = csv.reader(read_obj, delimiter = ",")

        for i in csv_reader:
            print(i[0])

import_transaction_from_csv(csv_file)
