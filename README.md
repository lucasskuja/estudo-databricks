# Estudo Databricks - Portfólio de Engenharia de Dados

Este repositório contém meus estudos e projetos práticos com Databricks, focados em engenharia de dados, processamento de dados e arquitetura de dados. Tudo versionado no GitHub para facilitar compartilhamento e colaboração, em vez de usar o workspace nativo do Databricks.

## Tópicos Abordados
- Delta Lake
- ETL com Spark SQL
- Processamento Incremental
- Delta Live Tables (DLT)
- Orquestração de Jobs
- Dashboards e Consultas DBSQL

## Como Executar
1. Clone o repositório: `git clone https://github.com/lucasskuja/estudo-databricks.git`
2. Importe os notebooks no seu workspace Databricks (conectado ao GitHub).
3. Execute os scripts em Python ou SQL.

## Estrutura do Repositório
- [notebooks/](notebooks/): Notebooks Jupyter com exemplos práticos.
  - [01-bronze-etl.ipynb](notebooks/01-bronze-etl.ipynb): ETL na camada Bronze (ingestão de dados brutos).
  - [02-silver-etl.ipynb](notebooks/02-silver-etl.ipynb): ETL na camada Silver (limpeza e transformação).
  - [03-gold-etl.ipynb](notebooks/03-gold-etl.ipynb): ETL na camada Gold (agregação e métricas).
  - [primeiro_notebook.ipynb](notebooks/primeiro_notebook.ipynb): Notebook inicial de estudos.
- [scripts/](scripts/): Scripts Python para automação e utilitários.
- [data/](data/): Dados de exemplo para testes.
- [docs/](docs/): Documentação e tutoriais.

## Tecnologias Utilizadas
- Databricks Runtime
- Python
- SQL
- Delta Lake
- Spark SQL

## Contato
- GitHub: [lucasskuja](https://github.com/lucasskuja)
