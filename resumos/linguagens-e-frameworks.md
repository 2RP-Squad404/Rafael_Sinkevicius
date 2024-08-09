# Relatório Semanal: Semana 2

## Nome:
Rafael Sinkevicius

## Trilha de Conhecimento:
Data Science

## Período:
05.08.2024-09.08.2024

---

## Conteúdos Estudados:

### Linguagens e Frameworks:

#### Tópicos:
- Python:
    - Introdução
    - Características
    - Usos
    - Video
- Apache Spark:
    - Introdução
    - Características
    - Usos
    - Exemplos
    - Benefícios
- Apache Beam:
    - Introdução
    - Características
    - Casos de Uso
    - Benefícios
    - Desafios
- Google Dataflow: 
    - Características
    - Casos de Uso
    - Benefícios
    - Desafios
- Apache Airflow:
    - Introdução
    - Características
    - Componentes
    - Casos de Uso
    - Benefícios
    - Desafios

#### Python:
#### Introdução
De sintaxe simples e fácil leitura de código, Python é uma linguagem de alto nível, com design limpo e escrita fácil.

#### Características
Sintaxe simples e legível, interpretação e portabilidade, bibliotecas e frameworks ricos e comunidade ativa.

#### Usos
Desenvolvimento Web, Data Science e Machine Learning, Desenvolvimento de Software, Inteligência Artificial e Deep Learning, Computação Científica e Pesquisa, Desenvolvimento de Jogos e Desenvolvimento de Aplicativos Desktop.

#### Video
[Introdução ao Python](introducao_python/app.py)

#### Apache Spark:
#### Introdução
Framework open-source para processamento rápido e em grande escala, superando outras tecnologias. PySpark é a interface do Apache Spark para o python. 

#### Características
Processamento em memória, API unificada para diferentes tipos de análise, escalabilidade e distribuição, suporte a várias linguagens e facilidade de integração.

#### Usos
Análise de dados em tempo real, Machine Learning, ETL (Extract, Transform, Load), análise de Big Data e processamento de grafos (redes sociais ou redes de transporte).

#### Exemplos
Processamento de Logs de servidores (monitoramento e anomalias), recomendação de produtos, análise de dados de sensores (manutenção preditiva e monitoramento de condições), análise de dados de redes sociais e análise financeira.

#### Benefícios
Desempenho, versatilidade, facilidade de uso e comunidade ativa.

#### Apache Beam:
#### Introdução
Modelo de programação unificado de código aberto e processamento de dados em tempo real. permite pipelines de dados com uma API.

#### Características
Modelo Unifcado (processamento em lotes e streaming), portabilidade, API flexível (suporta várias liguagens), transformações (manipulação de dados com map, filter, etc.) e Janelas e Watermarks (tempo real e marcações de água para dados fora de ordem).

#### Casos de Uso
ETL, processamento de dados em tempo real e agregações e análises em grandes conjuntos de dados.

#### Benefícios
Portabilidade, flexibilidade e comunidade ativa.

#### Desafios
Curva de aprendizado e desempenho dependente do executor.

#### Google Dataflow: 
Serviço gerenciado da Cloud de execução de pipelines criados com Apache Beam, fornecendo uma plataforma para dados em lote e streaming.

#### Características
Gerenciamento totalmente gerenciado, escalabilidade automática, integração com Google Cloud, vizualização e monitoramento e modelo de preços baseado em uso.

#### Casos de Uso
Processamento de Logs, análise de dados em tempo real e Data Integration (integrar e transformar dados de várias fontes antes da análise ou armazenamento).

#### Benefícios
Simplicidade de uso, integração com Google Cloud e escalabilidade e performance.

#### Desafios
Custo e dependência do Google Cloud

#### Apache Airflow:
#### Introdução
Plataforma de código aberto para automação de workflows de dados. Permite a definição, agendamento e monitoramento de dados complexos.

#### Características
Definição de Workflow como código (criação de DAGs (Directed Acyclic Graphs)), interface web, agendamemento flexível, execução paralela e escalabilidade, retry e resiliência (recuperação de erros, aumentando a robustez) e integração com diversas fontes.   

#### Componentes
DAG (define o fluxo de tarefas), operadores (BashOperator, PythonOperator, etc.), tasks (unidades de trabalho dentro de um DAG), scheduler (aciona as tarefas em cronogramas), executor (Celery, Kubernetes, etc.) e web interface (interface para gerenciar DAGs).  

#### Casos de Uso
ETL, Data Pipeline Management (coordenação de workflows), automação de processos e integração de sistemas.

#### Benefícios
Flexibilidade, escalabilidade, visibilidade e monitoramento e comunidade ativa.

#### Desafios
Complexidade de configuração, gerenciamento de recursos e curva de aprendizado.