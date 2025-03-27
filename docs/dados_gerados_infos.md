# Relação de Dados Gerados

- id_pedido: Identificador único do pedido.
- data_hora_pedido: Data e hora em que o pedido foi realizado.
- centro_distribuicao: Nome ou código do centro de distribuição responsável pelo processamento do pedido.
- percentual_ocupacao_CD: Percentual de ocupação do centro de distribuição no momento do processamento do pedido.
- tempo_separacao_min: Tempo (em minutos) gasto para a separação dos itens do pedido dentro do CD.
- tempo_embalagem_min: Tempo (em minutos) gasto na embalagem dos itens do pedido.
- tempo_total_processamento_min: Tempo total (em minutos) desde a separação até a finalização da embalagem do pedido.
- status_pedido: Status atual do pedido (ex: Pendente, Em Processamento, Enviado, Entregue).
- atraso_transporte_min: Tempo de atraso (em minutos) no transporte do pedido até o destino final.
- erro_picking: Indica se houve erro no picking (separação do pedido) no CD (ex: Sim/Não).
- categoria_produto: Categoria do produto no pedido (ex: Eletrônicos, Vestuário, Alimentos, etc.).
- quantidade_itens: Quantidade total de itens no pedido.
- peso_total_kg: Peso total do pedido em quilogramas.
