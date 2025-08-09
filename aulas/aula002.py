import pandas as pd
import numpy as np

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

# Aplicar renomeação das colunas
df.rename(columns=renomeacoes, inplace=True)

# Substituir códigos pelos valores descritivos nas colunas categóricas
df['senioridade'] = df['senioridade'].map(map_senioridade)
df['contrato'] = df['contrato'].map(map_contrato)
df['remoto'] = df['remoto'].map(map_remoto)
df['tamanho_empresa'] = df['tamanho_empresa'].map(map_tamanho_empresa)


# Função para imprimir separadores de forma elegante
def print_sep():
    print('-' * 50)

# Impressão das informações
print_sep()
print(df.info())  # Exibe informações do DataFrame
print_sep()
print(df.isnull().sum())  # Verifica valores ausentes
print_sep()
print(df['ano'].unique())  # Exibe anos únicos no DataFrame
print_sep()
print(df[df.isnull().any(axis=1)])  # Exibe linhas com valores ausentes
print_sep()

# Remove linhas com valores ausentes
df_limpo = df.dropna()

#Muda um dado float para inteiro
df_limpo = df_limpo.assign(ano=df_limpo['ano'].astype(int))

print('DataFrame após remoção de linhas com valores ausentes:')
print(df_limpo.isnull().sum())
print_sep()
print(df_limpo.head())  # Exibe as primeiras linhas do DataFrame limpo
print_sep()
print(df_limpo.info())  # Exibe informações do DataFrame limpo


'''
# Criacão de um DataFrame de exemplo para demonstrar o preenchimento de valores ausentes
# Prencher valores ausentes com a média e mediana da coluna 'salario'

df_salario = pd.DataFrame({
    'nome' : ['João', 'Maria', 'Pedro', 'Ana', 'Lucas'],
    'salario' : [4000, np.nan, 5000, np.nan, 100000]
    })
df_salario['salario_media'] = df_salario['salario'].fillna(df_salario['salario'].mean().round(2))
df_salario['salario_mediana'] = df_salario['salario'].fillna(df_salario['salario'].median())
print(df_salario)

# Criacão de um DataFrame de exemplo para demonstrar o preenchimento de valores ausentes
# Prencher valores ausentes com o valor anterior (forward fill) ou próximo (backward fill)

df_temperatura = pd.DataFrame({
    'dias' : ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta'],
    'temperatura' : [30, np.nan, np.nan, 28, 27]
})
df_temperatura['preenchido_ffill'] = df_temperatura['temperatura'].ffill()
df_temperatura['preenchido_bfill'] = df_temperatura['temperatura'].bfill()
print(df_temperatura)

# Criacão de um DataFrame de exemplo para demonstrar o preenchimento de valores ausentes
# Prencher valores ausentes com nao informado

df_cidade = pd.DataFrame({
    'nome' : ['João', 'Maria', 'Pedro', 'Ana', 'Lucas'],
    'cidade' : ['São Paulo', np.nan, 'Curitiba', np.nan, 'Rio de Janeiro']
})
df_cidade['cidade_preenchida'] = df_cidade['cidade'].fillna('Não informado')
print(df_cidade)
'''