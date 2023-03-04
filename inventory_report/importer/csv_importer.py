from inventory_report.importer.importer import Importer
import csv
import os


class CsvImporter(Importer):
    def import_data(file_path):
        _, ext = os.path.splitext(file_path)
        if ext != ".csv":
            raise ValueError("Arquivo csv inválido")

        with open(file_path) as file:
            reader = csv.DictReader(file)
            return list(reader)
