import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.io as pio

# Carregar os dados
url = "https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv"
df = pd.read_csv(url)
pio.renderers.default = "browser"  # força abrir no navegador padrão

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

# Filtrar só data scientists
df_ds = df_limpo[df_limpo['cargo'] == 'Data Scientist']

# Calcular salário médio por país
salario_pais = df_ds.groupby('empresa')['usd'].mean().reset_index()

# Ordenar pela média
salario_pais = salario_pais.sort_values(by='usd', ascending=True)

# Gráfico sobre o salário médio anual de Data Scientists por país
fig = px.bar(
    salario_pais,
    x='empresa',
    y='usd',
    title='Salário médio anual de Data Scientists por país',
    labels={'usd': 'Salário médio (USD)', 'empresa': 'País'},
    text=salario_pais['usd'].round(0),
    color='usd',  # cor por intensidade do salário
    color_continuous_scale='Viridis'
)

# Formatação do texto
fig.update_traces(textposition='outside')  # texto fora da barra

# Ajustes de layout
fig.update_layout(
    xaxis_tickangle=-45,
    xaxis_title='País',
    yaxis_title='Salário médio (USD)',
    uniformtext_minsize=8,
    uniformtext_mode='hide',
    height=600,
    margin=dict(t=50, b=150)
)

fig.write_html("salario_med_cientistas.html", auto_open=True)