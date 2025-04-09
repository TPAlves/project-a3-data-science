# 📦 project-a3-data-science

Análise e geração de dados sintéticos para simulação de processos logísticos e extração de insights relevantes com Python. 🚛📈

![Python](https://img.shields.io/badge/Python-3.12.3-blue?logo=python) 

![License](https://img.shields.io/badge/license-MIT-green) 

![Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow) 

### 🔍 Visão Geral

Abaixo, a distribuição de pedidos por centro de distribuição no dataset analisado:

Centro de Distribuição   | Número de Pedidos
------------------------ | -----------------
São Paulo (SP)           | ████████████████ 240
Brasília (DF)            | ██████████        150
Recife (PE)              | ████████          120
Belém (PA)               | ██████             90
Florianópolis (SC)       | ████               60


### 🏠 Estrutura do projeto:

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
### 🎯 Objetivo

Este projeto tem como objetivo aplicar técnicas de ciência de dados utilizando dados logísticos sintéticos, com foco em:

- Geração de dados realistas para simulação de gargalos operacionais de uma empresa ficticia.
- Análise exploratória e visualização.
- Extração de insights aplicáveis a logística e cadeia de suprimentos.

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
### 📌 Próximos Passos

- [ ] Implementar modelo preditivo com machine learning
- [ ] Automatizar pipeline de análise
- [ ] Criar dashboard interativo com Streamlit

---
### 👨‍💻 Desenvolvido por

[Seu Nome](https://github.com/seuusuario) • MBA em IA para Negócios

### 📄 Licença

Este projeto está licenciado sob a licença MIT.

### 🐍 Python version: 3.12.3
