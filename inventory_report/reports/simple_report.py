from collections import Counter
from datetime import datetime


class SimpleReport:
    def old_manufacturing_data(list):
        old_data = [product["data_de_fabricacao"] for product in list]
        return min(old_data)

    def close_expiration_date(list):
        data = datetime.now().strftime("%Y-%m-%d")
        close_data = [
            product["data_de_validade"]
            for product in list
            if product["data_de_validade"] > data
        ]
        return min(close_data)

    def company_with_more_products(list):
        company_name = Counter(
            [product["nome_da_empresa"] for product in list]
        ).most_common(1)[0][0]
        return company_name

    def generate(list):
        old_data = SimpleReport.old_manufacturing_data(list)
        close_data = SimpleReport.close_expiration_date(list)
        company_name = SimpleReport.company_with_more_products(list)
        return (
            f"Data de fabricação mais antiga: {old_data}\n"
            f"Data de validade mais próxima: {close_data}\n"
            f"Empresa com mais produtos: {company_name}"
        )
