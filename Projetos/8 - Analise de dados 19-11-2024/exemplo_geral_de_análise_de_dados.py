# -*- coding: utf-8 -*-
"""Exemplo Geral de Análise de Dados.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1boaunM8dGI6--2Ov6BINBzN4VKFTN1Gt

# Análise de Dados de vendas de uma empresa fictícia nos Estados Unidos


*   Responda às questões de negócio.
*   Utilize os conhecimentos adquiridos ao longo do curso e também as bibliotecas: numpy, pandas, matplotlib e seaborn.

## Pergundas de negócio


1. Análise exploratória (medidas estatísticas)
2. Qual cidade com maior valor de venda de produtos na Categoria "Suprimentos de Escritório"?
3. Qual o total de vendas por data do pedido? Demonstre o resultado por meio de um gráfico de linhas.
4. Qual o valor total de vendas por estado? Utilize um gráfico de barras.
5. Quais são as 10 cidades com maior total de vendas? Utilize um gráfico de barras.
6. Quais as 20 cidades com menor total de vendas? Utilzie um gráfico de barras.
7. Qual o segmento teve o maior total de vendas? Utilize um gráfico de pizza.
8. Qual o total de vendas por segmento e por ano?

###Preparação das bibliotecas e carregamento dos dados
"""

import numpy as np, pandas as pd, matplotlib as plt

dataset = pd.read_excel("dataset.xlsx")

"""###1. Análise exploratória (medidas estatísticas)

"""

dataset.info()

"""- Descrito:"""

dataset.describe()

"""- Metodo Head:

"""

dataset.head()

"""- Metodo Tail:"""

dataset.tail()

"""###2. Qual cidade com maior valor de venda de produtos na Categoria "Suprimentos de Escritório"?

- Filtrando:
"""

dataset2 = dataset[dataset["Categoria"] == "Material de Escritório"]
dataset2 = dataset2.groupby('Cidade').sum()
dataset2 = dataset2.sort_values('Valor_Venda', ascending=False)
dataset2 = dataset2.head()
dataset2.info()

"""###3. Qual o total de vendas por data do pedido? Demonstre o resultado por meio de um gráfico de linhas."""

dataset3 = dataset.groupby('Data_Pedido').sum().reset_index()
dataset3.head()
dataset3.plot(x='Data_Pedido', y='Valor_Venda', kind='line').figure.set_size_inches(15,5)

"""###4. Qual o valor total de vendas por estado? Utilize um gráfico de barras."""

dataset4 = dataset.groupby('Estado').sum().reset_index()
dataset4.plot(x='Estado', y='Valor_Venda', kind='bar').figure.set_size_inches(15,5)

"""###5. Quais são as 10 cidades com maior total de vendas? Utilize um gráfico de barras."""

dataset5 = dataset.groupby('Cidade').sum().reset_index()
dataset5 = dataset5.sort_values('Valor_Venda', ascending=False)
dataset5 = dataset5.head(10)
dataset5.plot(x='Cidade', y='Valor_Venda', kind='bar').figure.set_size_inches(15,5)

"""###6. Quais as 20 cidades com menor total de vendas? Utilzie um gráfico de barras.

"""

dataset6 = dataset.groupby('Cidade').sum().reset_index()
dataset6 = dataset6.sort_values('Valor_Venda', ascending=True)
dataset6 = dataset6.head(20)
dataset6.plot(x='Cidade', y='Valor_Venda', kind='bar').figure.set_size_inches(15,5)

"""###7. Qual o segmento teve o maior total de vendas? Utilize um gráfico de pizza.

"""

from enum import auto
dataset7 = dataset.groupby('Segmento').sum().reset_index()
dataset7.plot(x='Segmento', y='Valor_Venda', kind='pie', labels=dataset7['Segmento'], autopct='%1.1f%%').figure.set_size_inches(15,5)

"""###8. Qual o total de vendas por segmento e por ano?"""

dataset8 = dataset.copy()
dataset8['Data_Pedido'] = pd.to_datetime(dataset8['Data_Pedido'], format='%d/%m/%Y')
dataset8['Ano'] = dataset8['Data_Pedido'].dt.year
dataset8 = dataset8.groupby(['Segmento', 'Ano'])['Valor_Venda'].sum().reset_index()
dataset8.info()