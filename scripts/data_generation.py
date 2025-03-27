import pandas as pd
import numpy as np
import os

PATH_RESOURCES = os.path.join(
    os.path.dirname(os.path.dirname(__file__)), "resources/data/"
)

# Definição do número de registros
n = 50000  # Ajustável conforme necessidade

# Gerar datas entre 01/01/2024 e 31/12/2024
dates = pd.date_range(start="2024-01-01", end="2024-12-31", freq="h")
dates = np.random.choice(dates, n, replace=True)

# Simular sazonalidade: mais pedidos em novembro e dezembro, menos em janeiro e fevereiro
for i in range(n):
    mes = pd.Timestamp(dates[i]).month
    if mes in [11, 12]:  # Black Friday e Natal
        if np.random.rand() < 0.5:  # 50% de chance de criar um pedido extra
            dates[i] = np.random.choice(
                pd.date_range("2024-11-01", "2024-12-31", freq="h")
            )
    elif mes in [1, 2]:  # Período de baixa demanda
        if np.random.rand() < 0.3:  # 30% de chance de remover um pedido
            dates[i] = np.random.choice(
                pd.date_range("2024-01-01", "2024-02-28", freq="h")
            )

# Centros de distribuição
centros = [
    "São Paulo (SP)",
    "Recife (PE)",
    "Brasília (DF)",
    "Florianópolis (SC)",
    "Belém (PA)",
]
centros_cd = np.random.choice(centros, n)

# Percentual de ocupação do CD no momento do pedido (%)
percentual_ocupacao_CD = np.random.normal(loc=75, scale=15, size=n)
percentual_ocupacao_CD = np.clip(percentual_ocupacao_CD, 40, 100)

# Tempo de separação aumenta se a ocupação do CD for alta
tempo_separacao = (
    np.random.normal(loc=20, scale=5, size=n) + (percentual_ocupacao_CD - 75) * 0.2
)
tempo_separacao = np.clip(tempo_separacao, 5, 60)

# Tempo de embalagem varia conforme o tamanho do pedido
quantidade_itens = np.random.randint(1, 10, n)
tempo_embalagem = np.random.normal(loc=10, scale=3, size=n) + quantidade_itens * 0.5
tempo_embalagem = np.clip(tempo_embalagem, 2, 30)

# Tempo total de processamento
tempo_total = tempo_separacao + tempo_embalagem + np.random.randint(5, 20, n)

# Status do pedido: 15% de chance de atraso, mas maior quando o CD está superlotado
prob_atraso = np.where(
    percentual_ocupacao_CD > 85, 0.25, 0.15
)  # Maior atraso se ocupação > 85%
status_pedido = np.where(np.random.rand(n) < prob_atraso, "Atrasado", "Entregue")

# Tempo de atraso no transporte (apenas para pedidos atrasados)
atraso_transporte_min = np.where(
    status_pedido == "Atrasado", np.random.randint(10, 120, n), 0
)

# Erro na separação do pedido (1 = sim, 0 = não) - Mais comum em picos de demanda
erro_picking = np.random.choice([0, 1], n, p=[0.95, 0.05])

# Categorias de produto
categorias = ["Eletrodoméstico", "Vestuário", "Alimentos", "Eletrônicos", "Brinquedos"]
categoria_produto = np.random.choice(categorias, n)

# Peso total do pedido (kg) - Produtos maiores exigem mais tempo
peso_total_kg = np.random.uniform(0.5, 30.0, n)

# Criar DataFrame
df = pd.DataFrame(
    {
        "id_pedido": np.arange(1, n + 1),
        "data_hora_pedido": dates,
        "centro_distribuicao": centros_cd,
        "percentual_ocupacao_CD": np.round(percentual_ocupacao_CD, 2),
        "tempo_separacao_min": np.round(tempo_separacao, 2),
        "tempo_embalagem_min": np.round(tempo_embalagem, 2),
        "tempo_total_processamento_min": np.round(tempo_total, 2),
        "status_pedido": status_pedido,
        "atraso_transporte_min": atraso_transporte_min,
        "erro_picking": erro_picking,
        "categoria_produto": categoria_produto,
        "quantidade_itens": quantidade_itens,
        "peso_total_kg": np.round(peso_total_kg, 2),
    }
)


# Exibir as primeiras linhas
print(df.head())


#  Remover valores duplicados
df = df.drop_duplicates()

# Verificar e tratar valores nulos
df = df.dropna()

# Converter tipos de dados
df["data_hora_pedido"] = pd.to_datetime(df["data_hora_pedido"])
df["centro_distribuicao"] = df["centro_distribuicao"].astype("category")
df["status_pedido"] = df["status_pedido"].astype("category")
df["categoria_produto"] = df["categoria_produto"].astype("category")

# Salvar dataset processado
df.to_csv(os.path.join(PATH_RESOURCES, "dados_logisticos_sinteticos.csv"), index=False)

# Exibir informações sobre o dataset processado
print("\nInformações do Dataset Processado:")
print(df.info())
print("\nEstatísticas Descritivas:")
print(df.describe())
