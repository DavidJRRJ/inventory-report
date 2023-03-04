from inventory_report.importer.importer import Importer
import json
import os


class JsonImporter(Importer):
    def import_data(file_path):
        _, ext = os.path.splitext(file_path)
        if ext != ".json":
            raise ValueError("Arquivo JSON inválido")
     
        with open(file_path) as file:
            return json.load(file)
