import os
import pandas as pd
import plotly.express as px

# objectives:
# calculate the most sold product
# calculate the product that earned the most
# calculate the store/city that earned the most (create a dashboard)

archive_list = os.listdir(r"C:\Users\Maycon\Vendas-20240415T220542Z-001\Vendas")
total_chart = pd.DataFrame()

for archive in archive_list:
    if 'vendas' in archive.lower():
        chart = pd.read_csv(fr"C:\Users\Maycon\Vendas-20240415T220542Z-001\Vendas\{archive}")
        total_chart = pd.concat([total_chart, chart])

total_chart['Faturamento'] = total_chart['Quantidade Vendida'] * total_chart['Preco Unitario']

prod_chart = total_chart.groupby('Produto').sum()
prod_chart = prod_chart[['Quantidade Vendida']].sort_values(by='Quantidade Vendida', ascending=False)
# print(prod_chart)

invoicing_chart = total_chart.groupby('Produto').sum()
invoicing_chart = invoicing_chart[['Faturamento']].sort_values(by='Faturamento', ascending=False)
# print(invoicing_chart)

store_chart = total_chart.groupby('Loja').sum()
store_chart = store_chart[['Faturamento']].sort_values(by='Faturamento', ascending=False)
# print(store_chart)

prod_grf = px.bar(prod_chart, x=prod_chart.index, y='Quantidade Vendida')
prod_grf.show()

store_grf = px.bar(store_chart, x=store_chart.index, y='Faturamento')
store_grf.show()