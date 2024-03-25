from database import Database
from dataset.store_dataset import store_dataset
from product_analyzer import ProductAnalyzer


store_database = Database(database="mercado", collection="compras", dataset=store_dataset)

analyzer = ProductAnalyzer(database=store_database)

print("\nTotal de vendas por dia: ")
sales_per_day = analyzer.total_sales_per_day()
for sale in sales_per_day:
    print(f"{sale['_id']}: {sale['total_sales']} vendas")

print(f"\nProduto mais vendido: ")
most_sold = analyzer.most_sold_product()
if most_sold:
    print(f"{most_sold['_id']} ({most_sold['total_sold']} unidades vendidas)")

print("\nCliente que mais gastou em uma única compra: ")
highest_spender = analyzer.highest_spending_customer()
if highest_spender:
    print(f"Cliente {highest_spender['_id']} (R$ {highest_spender['total_spent']:.2f})")

print("\nProdutos com quantidade vendida acima de 1 unidade: ")
products_above_1 = analyzer.products_above_quantity_1()
for product in products_above_1:
    print(product)
