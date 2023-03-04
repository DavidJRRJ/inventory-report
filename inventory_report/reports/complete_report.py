from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    def products_in_stock(list):
        product_per_company = Counter(
            item["nome_da_empresa"] for item in list
        ).most_common(10)
        return product_per_company

    def generate(list):
        stock_list = CompleteReport.products_in_stock(list)
        generated_report = (
            f"{SimpleReport.generate(list)}\n"
            f"Produtos estocados por empresa:\n"
        )
        generated_stock_list = [
            f"- {key}: {value}\n" for key, value in stock_list
        ]
        generated_report += "".join(generated_stock_list)
        return generated_report
