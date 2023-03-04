from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
import os


class Inventory:
    def generate_report(file_path, ext):
        IMPORTERS = {
            ".csv": CsvImporter,
            ".json": JsonImporter,
            ".xml": XmlImporter,
        }
        importer_class = IMPORTERS.get(ext)
        if importer_class:
            return importer_class.import_data(file_path)
        else:
            raise ValueError("Arquivo Inválido")

    def import_data(file_path, report_type):
        _, ext = os.path.splitext(file_path)
        data = Inventory.generate_report(file_path, ext)

        switcher = {
            "simples": SimpleReport.generate(data),
            "completo": CompleteReport.generate(data),
        }
        report = switcher.get(report_type, None)
        if report is None:
            raise ValueError("Tipo de relatório inválido")

        return report
