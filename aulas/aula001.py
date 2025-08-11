import pandas as pd

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

# Obter dimensões do DataFrame
linhas, colunas = df.shape


# Função para imprimir separadores de forma elegante
def print_sep():
    print('-' * 50)

# Impressão das informações
print_sep()
print(f'DataFrame com {linhas} linhas e {colunas} colunas.')
print('Colunas:', ', '.join(df.columns))
print_sep()

print('Resumo do DataFrame:')
print(df.info())
print_sep()

print('Estatísticas descritivas para colunas numéricas:')
print(df.describe())
print_sep()

print('Exemplo das primeiras linhas:')
print(df.head())
print_sep()

# Contagem de valores únicos para colunas categóricas importantes
print('Contagem de senioridade:')
print(df['senioridade'].value_counts(), end='\n\n')

print('Contagem de contrato:')
print(df['contrato'].value_counts(), end='\n\n')

print('Contagem de regime de trabalho remoto:')
print(df['remoto'].value_counts(), end='\n\n')

print('Contagem do tamanho da empresa:')
print(df['tamanho_empresa'].value_counts(), end='\n\n')
print_sep()

# Estatísticas descritivas para colunas categóricas
print(df.describe(include='object'))
print_sep()