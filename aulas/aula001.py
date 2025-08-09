import pandas as pd

# Carregar os dados
url = "https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv"
df = pd.read_csv(url)

linhas, colunas = df.shape

# Dicionário de renomeação
novos_nomes = {
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
senioridade = {
    'SE': 'senior',
    'MI': 'pleno',
    'EN': 'junior',
    'EX': 'executivo'
}
contrato = {
    'FT': 'integral',
    'PT': 'parcial',
    'CT': 'contrato',
    'FL': 'freelancer'
}
remoto = {
    0: 'presencial',
    100: 'remoto',
    50: 'hibrido'
}
tamanho_empresa = {
    'L': 'grande',
    'S': 'pequena',
    'M':	'media'

}
# Aplicando renomeação
df.rename(columns=novos_nomes, inplace=True)
df['senioridade'] = df['senioridade'].replace(senioridade)
df['contrato'] = df['contrato'].replace(contrato)
df['remoto'] = df['remoto'].replace(remoto)
df['tamanho_empresa'] = df['tamanho_empresa'].replace(tamanho_empresa)

print()
print('Será impresso o DataFrame abaixo:')
print(f'{linhas} linhas e {colunas} colunas.')# Exibe quantas linhas e colunas existem no DataFrame
print(f'\nAs colunas são: {df.columns}')  # Exibe os nomes das colunas do DataFrame
print()
print(df.info())  # Exibe informações sobre o DataFrame, como tipos de dados e contagem de valores não nulos
print(df.describe())  # Exibe estatísticas descritivas do DataFrame
print('\n Primeiras linhas do DataFrame:')
print(df.head())  # Exibe as primeiras linhas do DataFrame
print()

print(df['senioridade'].value_counts())  # Exibe a contagem de valores únicos na coluna 'senioridade'
# SE = Senior, MI = Mid-level, EN = Entry-level, EX = Executive
print()
print(df['contrato'].value_counts())  # Exibe a contagem de valores únicos na coluna 'contrato'
# FT = Full-time, PT = Part-time, CT = Contract, FL = Freelance
print()
print(df['remoto'].value_counts())  # Exibe a contagem de valores únicos na coluna 'remoto'
print()
print(df['tamanho_empresa'].value_counts())  # Exibe a contagem de valores únicos na coluna 'tamanho_empresa'
