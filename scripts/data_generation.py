import pandas as pd
import numpy as np
import os

PATH_RESOURCES = os.path.join(os.path.dirname(os.path.dirname(__file__)), "resources/")
CITIES = ["São Paulo", "Manaus", "Porto Alegre", "Salvador", "Natal"]
TYPES_PRODUCTS = ["Eletrônico", "Vestuário", "Alimento", "Móvel", "Brinquedo"]


def convert_datetime(df: pd.DataFrame, columns: list):
    """
    Realiza a conversão de colunas para o tipo datetime americano
    """
    for col in columns:
        df[col] = pd.to_datetime(df[col], format="%Y-%m-%d %H:%M:%S", errors="coerce")
    return df


def clean_data(df: pd.DataFrame):
    """
    Realiza a limpeza dos dados

    - Remove valores duplicados
    - Remove valores nulos
    - Remove valores com caracteres especiais
    """
    df.drop_duplicates(inplace=True)
    df.dropna(inplace=True)
    return df


def create_data_distribution_centers():
    """
    Realiza a criação de dados de Centros de Distribuição (CDs)

    - ID_CD: Identificador único do centro de distribuição
    - Localizacao: Cidade onde o CD está localizado
    - Capacidade_Maxima_m3: Capacidade máxima de armazenamento em m³
    - Tempo_Processamento_horas: Tempo médio de processamento de pedidos em horas
    - Funcionarios_por_turno: Número de funcionários por turno
    - Custo_Operacional_R: Custo operacional mensal em R$
    """
    distribution_centers = pd.DataFrame(
        {
            "ID_CD": range(1, 6),
            "Localizacao": CITIES,
            "Capacidade_Maxima_m3": np.random.randint(1000, 5000, size=5),
            "Tempo_Processamento_horas": np.random.uniform(2, 10, size=5).round(2),
            "Funcionarios_por_turno": np.random.randint(20, 100, size=5),
            "Custo_Operacional_R": np.random.randint(100000, 500000, size=5),
        }
    )
    distribution_centers = clean_data(distribution_centers)
    distribution_centers.to_csv(
        f"{PATH_RESOURCES}centros_distribuicao.csv", index=False
    )
    return distribution_centers


def create_data_products():
    """
    Realiza a criação de dados de Pedidos e Expedição

    - ID_Pedido: Identificador único do pedido
    - Data_Pedido: Data e hora do pedido
    - Tempo_Separacao: Tempo médio de separação do pedido em minutos
    - Tempo_Expedicao: Tempo médio de expedição do pedido em minutos
    - Tipo_Produto: Tipo do produto
    - Quantidade: Quantidade de produtos no pedido
    - Tempo_Total_Processamento: Tempo total de processamento do pedido (Tempo_Separacao + Tempo_Expedicao) em minutos
    """
    num_orders = 1000
    orders = pd.DataFrame(
        {
            "ID_Pedido": range(1, num_orders + 1),
            "Data_Pedido": pd.date_range(
                start="2025-01-01", periods=num_orders, freq="h"
            ),
            "Tempo_Separacao": np.random.randint(10, 120, size=num_orders),  # minutos
            "Tempo_Expedicao": np.random.randint(10, 180, size=num_orders),  # minutos
            "Tipo_Produto": np.random.choice(
                TYPES_PRODUCTS,
                size=num_orders,
            ),
            "Quantidade": np.random.randint(1, 10, size=num_orders),
        }
    )
    orders["Tempo_Total_Processamento"] = (
        orders["Tempo_Separacao"] + orders["Tempo_Expedicao"]
    )
    orders = clean_data(orders)
    orders = convert_datetime(orders, ["Data_Pedido"])
    orders.to_csv(f"{PATH_RESOURCES}pedidos_expedicao.csv", index=False)


def create_data_transport(distribution_centers: pd.DataFrame):
    """
    Realiza a criação de dados de Transporte

    - ID_Veiculo: Identificador único do veículo
    - Capacidade_kg: Capacidade máxima de carga em kg
    - CD_Origem: Centro de distribuição de origem
    - Data_Saida: Data e hora de saída do veículo
    - Distancia_km: Distância em km
    - Tempo_Entrega_horas: Tempo de entrega em horas
    - Status_Pontualidade: Status da pontualidade da entrega
    """
    num_vehicles = 200
    transport = pd.DataFrame(
        {
            "ID_Veiculo": range(1, num_vehicles + 1),
            "Capacidade_kg": np.random.randint(1000, 15000, size=num_vehicles),
            "CD_Origem": np.random.choice(
                distribution_centers["Localizacao"], size=num_vehicles
            ),
            "Data_Saida": pd.date_range(
                start="2025-01-01", periods=num_vehicles, freq="3h"
            ),
            "Distancia_km": np.random.randint(10, 500, size=num_vehicles),
            "Tempo_Entrega_horas": np.random.randint(1, 48, size=num_vehicles),
            "Status_Pontualidade": np.random.choice(
                ["Atrasado", "No Prazo"], size=num_vehicles, p=[0.3, 0.7]
            ),
        }
    )
    transport = clean_data(transport)
    transport = convert_datetime(transport, ["Data_Saida"])
    transport.to_csv(f"{PATH_RESOURCES}transporte.csv", index=False)


def create_data_stock(distribution_centers: pd.DataFrame):
    """
    Realiza a criação de dados de Estoque

    - ID_Produto: Identificador único do produto
    - CD_Armazenamento: Centro de distribuição de armazenamento
    - Quantidade_Disponivel: Quantidade disponível no estoque
    - Lead_Time_dias: Tempo médio de reposição do estoque em dias
    - Indice_Ruptura_Percentual: Índice de ruptura do produto
    """
    num_products = 500
    stock = pd.DataFrame(
        {
            "ID_Produto": range(1, num_products + 1),
            "CD_Armazenamento": np.random.choice(
                distribution_centers["Localizacao"], size=num_products
            ),
            "Quantidade_Disponivel": np.random.randint(0, 1000, size=num_products),
            "Lead_Time_dias": np.random.randint(1, 30, size=num_products),
            "Indice_Ruptura_Percentual": np.random.uniform(
                0, 1, size=num_products
            ).round(2),
        }
    )
    stock = clean_data(stock)
    stock.to_csv(f"{PATH_RESOURCES}estoque.csv", index=False)


def create_data_operation_locks():
    """
    Realiza a criação de dados de Gargalos Operacionais

    - Data_Gargalo: Data e hora do gargalo
    - Tipo_Gargalo: Tipo de gargalo
    - CD_Afetado: Centro de distribuição afetado
    - Tempo_Atraso_horas: Tempo de atraso em horas
    """
    num_bottlenecks = 200

    bottlenecks = pd.DataFrame(
        {
            "Data_Gargalo": pd.date_range(
                start="2025-01-01", periods=num_bottlenecks, freq="2D"
            ),
            "Tipo_Gargalo": np.random.choice(
                ["Excesso de Pedidos", "Atraso na Expedição", "Falta de Estoque"],
                size=num_bottlenecks,
            ),
            "CD_Afetado": np.random.choice(
                distribution_centers["Localizacao"], size=num_bottlenecks
            ),
            "Tempo_Atraso_horas": np.random.randint(1, 24, size=num_bottlenecks),
        }
    )
    bottlenecks = clean_data(bottlenecks)
    bottlenecks.to_csv(f"{PATH_RESOURCES}gargalos_operacionais.csv", index=False)


if __name__ == "__main__":
    if not os.path.exists(PATH_RESOURCES):
        os.makedirs(PATH_RESOURCES)
    distribution_centers = create_data_distribution_centers()
    create_data_products()
    create_data_transport(distribution_centers)
    create_data_stock(distribution_centers)
    create_data_operation_locks()
    print("Todos os arquivos CSV foram gerados com sucesso!")
