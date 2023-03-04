from inventory_report.importer.importer import Importer
import xml.etree.ElementTree as ET
import os


class XmlImporter(Importer):
    def import_data(file_path):
        _, ext = os.path.splitext(file_path)
        if ext != ".xml":
            raise ValueError("Arquivo xml inválido")
        
        file = ET.parse(file_path)
        root = file.getroot()
        return [{e.tag: e.text for e in record} for record in root]
