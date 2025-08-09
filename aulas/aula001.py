import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv")
# arquivo .csv = dados tabulares, onde cada linha representa uma linha da tabela e os valores são separados por vírgulas

linhas, colunas = df.shape

# Dicionário de renomeação
novos_nomes = {
    'work_year': 'ano',
    'experience_level': 'nivel_experiencia',
    'employment_type': 'tipo_emprego',
    'job_title': 'cargo',
    'salary': 'salario',
    'salary_currency': 'moeda',
    'salary_in_usd': 'salario_usd',
    'employee_residence': 'residencia',
    'remote_ratio': 'taxa_remoto',
    'company_location': 'localizacao_empresa',
    'company_size': 'tamanho_empresa'
}
# Aplicando renomeação
df.rename(columns=novos_nomes, inplace=True)

print()
print('Será impresso o DataFrame abaixo:')
print(f'{linhas} linhas e {colunas} colunas.')# Exibe quantas linhas e colunas existem no DataFrame
print()
print(f'As colunas são: {df.columns}')  # Exibe os nomes das colunas do DataFrame
print()
print(df.info())  # Exibe informações sobre o DataFrame, como tipos de dados e contagem de valores não nulos
print(df.describe())  # Exibe estatísticas descritivas do DataFrame
print('\n Primeiras linhas do DataFrame:')
print(df.head())  # Exibe as primeiras linhas do DataFrame
