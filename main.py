import os # Importa a biblioteca OS, que permite iteragir com o sistema operacional como manipular arquivos e diretórios.
import pandas as pd # Importa a biblioteca panda, amplamente usada para manipulação e analise de dados, com o apelido "pd".
import plotly.express as px # Importa a biblioteca plotly express para a criação de gráficos interativos com o apelido "px".

# Lista todos os arquivos no diretório especificado, que contém as bases de vendas.
lista_arquivos = os.listdir(r"C:\Users\guilhermedelaporta\Downloads\drive-download-20241122T152310Z-001\Vendas") # e lista um diretorio com o listdir() que tem o caminho para a pasta de vendas
# print (lista_arquivos) # teste para verificar se estava funcionando 

tabela_total = pd.DataFrame() # Cria um DataFrame vazio que será usado para consolidar todas as tabelas de vendas.

for arquivo in lista_arquivos: # Itera sobre cada arquivo listado no diretório.
     if "vendas" in arquivo.lower(): # Verifica se o nome do arquivo contém a palavra "vendas" (ignorando maiúsculas e minúsculas).
         tabela = pd.read_csv(fr"C:\Users\guilhermedelaporta\Downloads\drive-download-20241122T152310Z-001\Vendas/{arquivo}") # Importa o arquivo como um DataFrame Pandas. Aqui assume-se que os arquivos estão no formato CSV.
         tabela_total = pd.concat([tabela_total, tabela], ignore_index=True) # Concatena a nova tabela importada ao DataFrame "tabela_total".
         
# A tabela está consolidada e pode ser visualizada, se necessário.
# print(tabela_total) # teste para verificar os dados compilados.

tabela_produtos = tabela_total.groupby("Produto").sum() # Agrupa os dados por produto e calcula a soma de todas as colunas numéricas, como "Quantidade Vendida" e "Preco Unitario"
tabela_produtos = tabela_produtos[["Quantidade Vendida", "Preco Unitario"]].sort_values(by="Quantidade Vendida", ascending=False ) # Seleciona as colunas relevantes e ordena os produtos pela quantidade vendida em ordem decrescente. 
# print(tabela_produtos) # (descomentar para ver o ranking dos produtos mais vendidos).


tabela_total['Faturamento'] = tabela_total['Quantidade Vendida'] * tabela_total['Preco Unitario'] # Adiciona uma nova coluna "Faturamento" ao DataFrame, calculando o faturamento como "Quantidade Vendida" * "Preco Unitario".
# print(tabela_total) # (Descomentar para verificar os dados com a nova coluna "Faturamento")


tabela_faturamento = tabela_total.groupby("Produto").sum() # Agrupa novamente os dados por produto, agora somando o faturamento.
# print(tabela_faturamento) (teste)


tabela_faturamento = tabela_faturamento[['Faturamento']].sort_values(by='Faturamento', ascending=False) # Seleciona apenas a coluna "Faturamento" e ordena os produtos em ordem decrescente pelo valor faturado.
# print(tabela_faturamento) # (Descomentar para ver o ranking dos produtos mais lucrativos.)

 
tabela_lojas = tabela_total.groupby('Loja').sum() # Agrupa os dados por loja/cidade, somando o faturamento de cada uma.
# print(tabela_lojas) # (Descomentar para visualizar a cidade da loja e o faturamento dela)


tabela_lojas = tabela_lojas[['Faturamento']].sort_values(by="Faturamento", ascending=False) # Seleciona apenas a coluna "Faturamento" e ordena as lojas em ordem decrescente pelo valor faturado.
# print(tabela_lojas) # (Descomentar para verificar o ranking das lojas que mais faturaram).
 
grafico = px.bar(tabela_lojas, x=tabela_lojas.index, y='Faturamento') # Cria um gráfico de barras interativo usando Plotly Express(O eixo X será o nome das lojas(índice do DataFrame) e o eixo y será o faturamento.)
grafico.show() # Exibe no navegador o gráfico configurado.
