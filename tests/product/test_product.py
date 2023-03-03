from inventory_report.inventory.product import Product
from datetime import datetime


def test_cria_produto():
    product = Product(
        1,
        "Produto Teste",
        "Empresa Teste",
        datetime(2022, 1, 1),
        datetime(2022, 12, 31),
        "123456",
        "em local seco e arejado",
    )

    assert product.id == 1
    assert product.nome_do_produto == "Produto Teste"
    assert product.nome_da_empresa == "Empresa Teste"
    assert product.data_de_fabricacao == "2022-01-01 00:00:00"
    assert product.data_de_validade == "2022-12-31 00:00:00"
    assert product.numero_de_serie == "123456"
    assert product.instrucoes_de_armazenamento == "em local seco e arejado"
