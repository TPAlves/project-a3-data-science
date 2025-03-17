# Relação de Dados Gerados

## Dados de Centros de Distribuição (CDs)

- ID do CD: código único do centro de distribuição
- Localização: cidade, estado
- Capacidade máxima de armazenagem: metros cubicos (m³)
- Tempo médio de processamento de pedidos: horas
- Número de funcionários por turno
- Custo operacional mensal: R$

## Dados de Pedidos e Expedição

- ID do pedido: código único do pedido
- Data e hora da solicitação
- Tempo de separação e embalagem do pedido: minutos
- Tempo de expedição do pedido: minutos
- Tipo de produto: SKU, categoria
- Quantidade de itens no pedido

## Dados de Transporte

- ID do veículo: código único do veículo
- Capacidade máxima de carga: kg
- Centro de distribuição de origem
- Data e hora de saída
- Distância percorrida: km
- Tempo total de entrega: horas
- Status de pontualidade: Atrasado / No Prazo

## Dados de Estoque

- ID do produto (SKU): código único do produto
- Centro de distribuição de armazenamento
- Quantidade disponível
- Lead time de reposição: dias
- Índice de ruptura: ocorrências de falta de estoque

## Dados de Gargalos Operacionais

- Data do gargalo
- Tipo de gargalo: Excesso de pedidos, Atraso na expedição, Falta de estoque, etc.
- CD afetado
- Tempo médio de atraso registrado: horas
