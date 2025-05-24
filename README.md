# DataLog - Solução Analítica e Previsão de Demanda Logística com Machine Learning

![Python](https://img.shields.io/badge/Python-3.12.3-blue?logo=python)
![Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow)
![License](https://img.shields.io/badge/license-MIT-green)

## Visão Geral

## Este projeto implementa um pipeline completo para previsão de demanda logística e análise de gargalos operacionais, utilizando técnicas de ciência de dados e machine learning. O objetivo é identificar padrões, prever demandas futuras e recomendar melhorias para centros de distribuição (CDs) da DataLog.

## Como Executar o Projeto

1. **Pré-requisitos**

   - Python 3.12.3 ou superior
   - Instale as dependências:
     ```sh
     pip install -r requirements.txt
     ```

2. **Execução**

   - Para executar o pipeline, você pode usar o Jupyter Notebook incluído no projeto:
     ```sh
     jupyter notebook
     ```
   - Abra o arquivo `main.ipynb` no Jupyter Notebook.
   - Para rodar o pipeline completo:
     ```sh
     jupyter notebook main.ipynb
     ```
   - Siga as células do notebook para:
     - Gerar dados sintéticos de demanda
     - Preparar os dados para modelagem
     - Realizar análise exploratória e gerar gráficos
     - Treinar modelos de machine learning para previsão de demanda
     - Gerar previsões futuras
     - Analisar gargalos e recomendar ações
     - Salvar todos os resultados no diretório `output/`

---

## Estrutura do Projeto

```bash
├── requirements.txt           # Dependências do projeto
├── README.md                  # Este arquivo
├── main.ipynb                 # Notebook principal do pipeline
├── output/                    # Resultados gerados automaticamente contendo: images, relatórios e datasets utilizados.
```

---

## Pipeline de Análise

O pipeline executa as seguintes etapas:

1. **Geração de Dados Sintéticos**  
   Simula a demanda diária por categoria de produto em cada CD, considerando eventos especiais, sazonalidade, capacidade e características operacionais.

2. **Preparação dos Dados**

   - Engenharia de features (lags, médias móveis, variáveis cíclicas)
   - Codificação de variáveis categóricas
   - Normalização e tratamento de valores ausentes

3. **Análise Exploratória**

   - Geração de gráficos e estatísticas
   - Identificação de padrões sazonais, gargalos e fatores de influência

4. **Treinamento de Modelos de Machine Learning**

   - Modelos: Random Forest, Gradient Boosting, XGBoost, Regressão Linear
   - Previsão de demanda futura por CD e categoria
   - Seleção automática do melhor modelo para cada caso

5. **Geração de Previsões Futuras**

   - Previsão da demanda para os próximos 30 dias
   - Estimativa de capacidade utilizada e gargalos previstos

6. **Análise de Gargalos e Recomendações**
   - Identificação de CDs, datas e processos críticos
   - Geração de recomendações gerais e específicas para otimização operacional

---

## Principais Arquivos Gerados

| Arquivo                                    | Caminho Relativo                                 | Descrição                                                                  |
| ------------------------------------------ | ------------------------------------------------ | -------------------------------------------------------------------------- |
| Dados de Demanda Brutos                    | output/dados_demanda_brutos.csv                  | Dados sintéticos gerados para todas as combinações de CD, categoria e data |
| Dados de Demanda Preparados                | output/dados_demanda_preparados.csv              | Dados tratados e enriquecidos para uso nos modelos                         |
| Insights da Análise Exploratória           | output/insights_analise.txt                      | Resumo dos principais padrões e insights                                   |
| Previsões de Demanda                       | output/previsoes_demanda.csv                     | Previsões futuras para cada CD e categoria                                 |
| Relatório de Recomendações                 | output/recomendacoes/relatorio_recomendacoes.md  | Relatório detalhado com análise de gargalos e recomendações                |
| Gráficos de Análise e Modelos              | output/visualizacoes/_.png, output/modelos/_.png | Visualizações dos dados, previsões, importância de variáveis e gargalos    |
| Gráficos de Gargalos e Capacidade Prevista | output/recomendacoes/\*.png                      | Visualizações dos gargalos previstos e capacidade utilizada                |

---

## Principais Insights da Análise

- **Padrões sazonais:** Picos de demanda em eventos como Black Friday e Natal; menor demanda nos fins de semana.
- **Diferenças entre CDs:** São Paulo lidera em demanda e eficiência; Belém e Florianópolis têm maior risco de gargalos.
- **Categorias críticas:** Eletrônicos e Vestuário concentram maior variabilidade e risco de gargalo.
- **Gargalos operacionais:** Picking é o principal gargalo, seguido por expedição em períodos críticos.
- **Fatores de influência:** Eventos especiais, sazonalidade, dia da semana e características dos produtos/CDs.
- **Eficiência:** CDs com maior automação apresentam menores taxas de erro e maior eficiência.

---

## Modelos de Machine Learning Utilizados

| Modelo            | Objetivo Principal    | Rótulo (Target) | Tipo de Valor | O que faz?                                               | Principais Features Utilizadas                 |
| ----------------- | --------------------- | --------------- | ------------- | -------------------------------------------------------- | ---------------------------------------------- |
| Random Forest     | Prever demanda futura | demanda         | Numérico      | Usa várias árvores de decisão para estimar a demanda     | Datas, eventos, histórico, capacidade, produto |
| Gradient Boosting | Prever demanda futura | demanda         | Numérico      | Combina árvores pequenas para melhorar a previsão        | Datas, eventos, histórico, capacidade, produto |
| XGBoost           | Prever demanda futura | demanda         | Numérico      | Otimiza boosting para prever quantidade de itens         | Informações temporais, atrasos, capacidade     |
| Regressão Linear  | Prever demanda futura | demanda         | Numérico      | Calcula tendência linear baseada em variáveis históricas | Datas, histórico, eventos, características     |

O melhor modelo é selecionado automaticamente para cada CD e categoria.

---

## Recomendações Operacionais

- Implementar sistema de previsão de demanda em tempo real
- Estabelecer alertas automáticos para capacidade acima de 80%
- Desenvolver planos de contingência para períodos críticos
- Otimizar processos de picking e embalagem, investir em automação
- Balancear carga entre CDs durante picos de demanda

---

## Conclusão

A solução permite prever demandas, identificar gargalos e recomendar ações para otimizar a operação logística da DataLog, reduzindo custos, atrasos e aumentando a eficiência e satisfação do cliente.

---

## Autores

[Marcus Borges](https://github.com/Marcus-Borges) • Ciência da Computação  
[Thiago Alves](https://github.com/TPAlves) • Sistemas de Informação

---

**Obs.: Para detalhes completos, consulte o notebook `main.ipynb`, notebooks auxiliares, scripts e relatórios gerados no diretório `output/`.**
