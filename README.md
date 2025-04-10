# A3 - Ferramentas Computacionais e Programação para Ciência de Dados 🏫
![Python](https://img.shields.io/badge/Python-3.12.3-blue?logo=python) 
![Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow) 

## Análise de Gargalos Operacionais na Cadeia de Suprimentos: Uma Solução Analítica para a DataLog 💻

Este projeto foi desenvolvido como parte da avaliação da Unidade Curricular Digital (UCD) de Ferramentas Computacionais e Programação para Ciência de Dados. O objetivo principal é aplicar os conhecimentos adquiridos em Ciência de Dados, Big Data e Inteligência Analítica para resolver um problema real na área de Logística e Cadeia de Suprimentos.

A solução analítica apresentada neste projeto foca na identificação e análise de gargalos na cadeia de suprimentos da DataLog, um hub logístico que atende grandes varejistas, indústrias e empresas de e-commerce no Brasil. A solução utiliza técnicas de mineração de dados e visualização para avaliar o desempenho dos centros de distribuição, processos de picking, embalagem e expedição, com o objetivo de recomendar melhorias operacionais.

### Problema Abordado 📝

A DataLog, empresa fictícia, assim como muitas empresas do setor, enfrenta desafios em otimizar suas operações logísticas devido ao crescimento do e-commerce e mudanças no comportamento do consumidor. Gargalos operacionais podem levar a ineficiências, aumento de custos e atrasos nas entregas, impactando a competitividade da empresa.

### Solução Proposta 🎯

Este projeto propõe uma metodologia de análise de dados, seguindo as etapas do pipeline de análise de dados, para identificar esses gargalos. A solução utiliza Python e bibliotecas como Pandas, NumPy, Scikit-learn e Matplotlib para:

* **Coleta e preparação de dados:** Identificação e tratamento dos dados relevantes para a análise. 
* **Análise exploratória dos dados:** Investigação de padrões, tendências e outliers nos dados operacionais da DataLog. 
* **Desenvolvimento dos modelos:** Implementação de modelos analíticos para identificar áreas de ineficiência e gargalos.
* **Geração de visualizações:** Criação de visualizações claras e informativas para facilitar a interpretação dos resultados.
* **Recomendações práticas:** Fornecimento de sugestões acionáveis para otimizar os processos e eliminar os gargalos identificados.

### Potenciais Benefícios 🥅

A implementação desta solução pode proporcionar à DataLog:

* Redução de custos operacionais. 
* Melhoria na eficiência dos processos. 
* Otimização da alocação de recursos. 
* Aumento da satisfação do cliente através da redução de prazos de entrega e maior confiabilidade no serviço.

### Visão Geral 🔍 

Abaixo, a distribuição de pedidos por centro de distribuição no dataset analisado:

Centro de Distribuição   | Número de Pedidos
------------------------ | -----------------
São Paulo (SP)           | ████████████████ 240
Brasília (DF)            | ██████████        150
Recife (PE)              | ████████          120
Belém (PA)               | ██████             90
Florianópolis (SC)       | ████               60


### Estrutura do projeto 🏠:

```bash
├── requirements.txt 📦 Dependências do projeto
├── README.md 📝 Este arquivo
├── scripts 🧠 Scripts principais
│   ├── data_generation.py 🔄 Geração de dados sintéticos
│   ├── data_analysis.py 📊 Análise e visualização de dados
├── resources 📁 Recursos do projeto
│   ├── images 🖼️ Imagens e gráficos gerados
│   ├── data 📊 Dataset utilizado
├── docs 📚 Documentação e insights
│   ├── insights.md 💡 Descobertas e conclusões
│   ├── graficos_gerados_infos.md 🧾 Detalhes dos gráficos
│   ├── dados_gerados_infos.md 📄 Informações sobre os dados
```

### Instalação das dependências 📖:

```sh
pip install -r requirements.txt
```

### Geração de massa de dados 🎲:

```sh
python3 scripts/data_generation.py
```

### Análise dos dados 📊:

```sh
python3 scripts/data_analysis.py
```
---
### Próximos Passos 📌 

- [ ] Implementar modelo preditivo com machine learning
- [ ] Automatizar pipeline de análise
- [ ] Criar dashboard interativo com Streamlit

---
### Desenvolvido por 👨‍💻 

[Marcus Borges](https://github.com/Marcus-Borges) • Discente do curso de ciência da computação

[Thiago Alves](https://github.com/TPAlves) • Discente do curso de

### 📄 Licença

![License](https://img.shields.io/badge/license-MIT-green) 

### 🐍 Python version: 3.12.3
Este README fornece uma visão geral do projeto, sua motivação acadêmica e os principais resultados esperados. Para detalhes completos sobre a metodologia, implementação e resultados, consulte o artigo e o código-fonte disponíveis neste repositório.
