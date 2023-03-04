from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
import os


class Inventory:
    def import_data(file_path, report_type):
        _, ext = os.path.splitext(file_path)
        if ext == ".csv":
            data = CsvImporter.import_data(file_path)
        elif ext == ".json":
            data = JsonImporter.import_data(file_path)
        elif ext == ".xml":
            data = XmlImporter.import_data(file_path)
        else:
            raise ValueError("Arquivo Inválido")

        if report_type == 'simples':
            report = SimpleReport.generate(data)
        elif report_type == 'completo':
            report = CompleteReport.generate(data)        
        else:
            raise ValueError('Tipo de relatório inválido')
        
        return report
