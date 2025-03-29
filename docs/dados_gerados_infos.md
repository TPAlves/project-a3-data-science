## Relação de Dados Gerados

| Coluna                        | Descrição                                                             | Tipo       | Exemplo                        |
| ----------------------------- | --------------------------------------------------------------------- | ---------- | ------------------------------ |
| id_pedido                     | Identificador único do pedido                                         | Inteiro    | 102345                         |
| data_hora_pedido              | Data e hora da criação do pedido                                      | Datetime   | 2025-03-15 14:32               |
| centro_distribuicao           | CD onde o pedido foi processado                                       | Categórico | São Paulo (SP)                 |
| tempo_separacao_min           | Tempo (minutos) para separar o pedido                                 | Numérico   | 18.5                           |
| tempo_embalagem_min           | Tempo (minutos) para embalar                                          | Numérico   | 5.2                            |
| tempo_total_processamento_min | Tempo total para processar pedido (separação + embalagem + expedição) | Numérico   | 34.7                           |
| status_pedido                 | Status final do pedido                                                | Categórico | "Entregue" / "Atrasado"        |
| percentual_ocupacao_CD        | Ocupação do centro de distribuição no momento do pedido (%)           | Numérico   | 82.3                           |
| qtd_pedidos_dia_CD            | Quantidade total de pedidos processados no CD no dia                  | Numérico   | 12.453                         |
| erro_picking                  | Pedido teve erro na separação?                                        | Binário    | 0 (não) / 1 (sim)              |
| atraso_transporte_min         | Tempo de atraso no transporte (se houver)                             | Numérico   | 12.1                           |
| categoria_produto             | Tipo de produto enviado                                               | Categórico | "Eletrodoméstico", "Vestuário" |
| quantidade_itens              | Quantidade de itens no pedido                                         | Numérico   | 3                              |
| peso_total_kg                 | Peso total da carga do pedido                                         | Numérico   | 1.8                            |
