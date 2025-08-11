import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Carregar os dados
url = "https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv"
df = pd.read_csv(url)

# Renomear colunas para português
renomeacoes = {
    'work_year': 'ano',
    'experience_level': 'senioridade',
    'employment_type': 'contrato',
    'job_title': 'cargo',
    'salary': 'salario',
    'salary_currency': 'moeda',
    'salary_in_usd': 'usd',
    'employee_residence': 'residencia',
    'remote_ratio': 'remoto',
    'company_location': 'empresa',
    'company_size': 'tamanho_empresa'
}


# Dicionários para mapear valores categóricos para português
map_senioridade = {'SE': 'senior', 'MI': 'pleno', 'EN': 'junior', 'EX': 'executivo'}
map_contrato = {'FT': 'integral', 'PT': 'parcial', 'CT': 'contrato', 'FL': 'freelancer'}
map_remoto = {0: 'presencial', 50: 'hibrido', 100: 'remoto'}
map_tamanho_empresa = {'L': 'grande', 'M': 'media', 'S': 'pequena'}


# Função para imprimir separadores de forma elegante
def print_sep():
    print('-' * 50)

# Aplicar renomeação das colunas
df.rename(columns=renomeacoes, inplace=True)

# Substituir códigos pelos valores descritivos nas colunas categóricas
df['senioridade'] = df['senioridade'].map(map_senioridade)
df['contrato'] = df['contrato'].map(map_contrato)
df['remoto'] = df['remoto'].map(map_remoto)
df['tamanho_empresa'] = df['tamanho_empresa'].map(map_tamanho_empresa)

# Remove linhas com valores ausentes
df_limpo = df.dropna()

#Muda um dado float para inteiro
df_limpo = df_limpo.assign(ano=df_limpo['ano'].astype(int))

'''
# Ordena o DataFrame por ordem crescente de senioridade
df_limpo.groupby('senioridade')['usd'].mean().sort_values(ascending=False)
ordem = df_limpo.groupby('senioridade')['usd'].mean().sort_values(ascending=True).index


# Gráfico de barras do salário anual em USD por nível de senioridade
# Define o tamanho do gráfico
plt.figure(figsize=(8, 5))
# Cria o gráfico de barras
sns.barplot(data=df_limpo, x='senioridade', y='usd', order=ordem)
# Título e ajustes
plt.title('Salario anual com base no nivel de senioridade', fontsize=14)
plt.xlabel('Nível de Senioridade', fontsize=12)
plt.ylabel('Salário medio em (USD)', fontsize=12)

plt.show()

# Gráfico de distribuição do salário anual em USD
plt.figure(figsize=(10, 5))
sns.histplot(df_limpo['usd'], bins=50, kde=True)
plt.title('Distribuição do Salário Anual (USD)', fontsize=14)
plt.xlabel('Salario em USD', fontsize=12)
plt.ylabel('Frequencia', fontsize=12)

plt.show()

# Gráfico de caixa do salário anual em USD
plt.figure(figsize=(8, 5))
sns.boxenplot(x=df_limpo['usd'])
plt.title('Boxplot do salário', fontsize=14)
plt.xlabel('Salario em USD', fontsize=12)

plt.show()
'''
#
ordem_senioridade = ['junior', 'pleno', 'senior', 'executivo']
plt.figure(figsize=(8, 5))
sns.boxenplot(data=df_limpo, x='senioridade', y='usd', order=ordem_senioridade, palette='Set2', hue='senioridade')
plt.title('Boxplot do Salário Anual por Nível de Senioridade', fontsize=14)
plt.xlabel('Nível de Senioridade', fontsize=12)
plt.ylabel('Salário Anual (USD)', fontsize=12)

plt.show()