import pandas as pd

import matplotlib.pyplot as plt

data = {
    'data_venda': ['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04', '2024-01-05', '2024-01-06', '2024-01-07'],
    'produto': ['Produto A', 'Produto B', 'Produto A', 'Produto C', 'Produto B', 'Produto C', 'Produto A'],
    'quantidade': [10, 5, 7, 3, 10, 6, 15],
    'preco_unitario': [15.5, 22.0, 15.5, 40.0, 22.0, 40.0, 15.5]
}

df = pd.DataFrame(data)

df['valor_total'] = df['quantidade'] * df['preco_unitario']

df['data_venda'] = pd.to_datetime(df['data_venda'])

print("Primeiras linhas do DataFrame:")
print(df.head())

print("\nEstatísticas descritivas:")
print(df.describe())

vendas_por_produto = df.groupby('produto')['valor_total'].sum()
print("\nTotal de vendas por produto:")
print(vendas_por_produto)

receita_total = df['valor_total'].sum()
print(f"\nReceita total: R${receita_total:.2f}")

media_vendas = df['valor_total'].mean()
print(f"Média de vendas por transação: R${media_vendas:.2f}")

vendas_por_produto.plot(kind='bar', color='skyblue', title='Total de Vendas por Produto')
plt.xlabel('Produto')
plt.ylabel('Valor Total de Vendas')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()