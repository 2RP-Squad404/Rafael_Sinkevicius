### Computação em Nuvem:

#### Tópicos:
- Introdução ao Google Cloud Dataflow
    - Características
    - Componentes
    - Casos de Uso
    - Benefícios
    - Desafios
    - Documentação
- Introdução ao Google Cloud Dataproc
    - Características
    - Componentes
    - Casos de Uso
    - Benefícios
    - Desafios
    - Documentação
- Introdução ao Google Cloud Composer
    - Características
    - Componentes
    - Casos de Uso
    - Benefícios
    - Desafios
- Introdução ao Google Cloud Functions
    - Características
    - Componentes
    - Casos de Uso
    - Benefícios
    - Desafios
    - Documentação

---

#### Dataflow
#### Introdução
É um serviço para processamento e análise de dados em larga escala. Permite a criação e execução de pipelines em tempo real e em batch, utilizando o Apache Beam, que oferece flexibilidade para diferentes processamentos.

#### Características
- Modelo de programação: unifica o processamento em batch e streaming baseado no Apache Beam

- Gerenciamento automático de recursos: escalabilidade de acordo com a carga de trabalho, alocando recursos automaticamente.

- Escalabilidade: escala automaticamente os recursos conforme a demanda.

- Flexibilidade de processamento: suporta processamento em tempo real e em batch.

- Integração com o Ecossistema Google Cloud: BigQuery, Cloud Storage e Pub/Sub.

- Vizualização e monitoramento: interface para monitoramento de execução dos pipelines e diagnosticar problemas.

#### Componentes
- Pipeline: define o fluxo e transformação dos dados.

- Transformações: operações aplicadas aos dados, como filtragem e agregação.

- PCollections: coleções de dados intermediários ou finais dentro de um pipeline.

- Data Sources e Sinks: Fontes de dados e destinos onde os dados processados são armazenados.

- Workers: instâncias que executam as tarefas de processamento.

#### Casos de Uso
- Processamento de Dados em Tempo Real: Análise de streams de eventos, como logs de aplicações.

- ETL(Extract, Transform, Load): ETL de dados para armazenamento ou análise.

- Análise de dados em Batch: Processamento de grandes volumes de dados para análises complexas.

- Integração de dados: Unificação de dados de diversas fontes de forma consistente.

- Gerenciamento de Dados: Automação de dados entre sistemas, garantindo consistência.

#### Benefícios
- Automação e gerenciamento: solução que reduz complexidade de escalabilidade.

- Flexibilidade de Processamento: Suporta diferentes necessidades de processamento.

- Integração: Facilita a integração com serviços do Cloud.

- Escalabilidade: Escala de forma automatica conforme necessaidade de dados.

#### Desafios
- Complexidade de configuração: otimização pode ser complexa.

- Custo: aumenta conforme a quantidade de dados processados.

- Curva de aprendizado: requer familiaridade com Apache Beam e Google Cloud.

#### Documentação
#### Visão geral do Dataflow:
Serviço gerenciado para processamento de dados em stream e em batch em grande escala. Permite a criação de pipelines de dados que leem, transformam e gravam dados em diferentes destinos. Útil para ingestão de dados, fluxos de trabalho ETL, BI, aplicação de ML em tempo real e processamento de dados de sensores.

#### Vantagens
- Gerenciado: O Google gerencia os recursos e a execução do Dataflow.

- Escalonável: Processa dados em grande escala com escalonamento automático.

- Portátil: Permite mover pipelines entre diferentes plataformas, baseado no Apache Beam.

- Flexível: Suporta pipelines simples e avançados, com opções de codificação ou uso de modelos predefinidos.

- Observável: Oferece monitoramento e visualização de pipelines no Console do Google Cloud.

#### Funcionamento
Usa um modelo de dados que incluem leitura, transformação e gravação de dados. É compatível com executores com o Apache Beam, que permite a execução de pipelines em diferentes plataformas. Um uso comum é a integração com Pub/Sub, BigQuery e Looker para soluções de ETL e BI.

---

#### Dataproc
#### Introdução
Serviço que facilita o processamento de dados em larga escala usando Apache Hadoop e Apache Spark. Ele simplifica o gerenciamento de clusters com uma solução eficiente e econômica para executar cargas de trabalho de processamento de dados, análise e machine learning.

#### Características
- Gerenciamento de Clusters: Automação do ciclo de vida dos clusters, incluindo criação, escalabilidade e terminação.

- Integração com Google Cloud: Fácil integração com serviços como BigQuery e Cloud Storage.

- Escalabilidade: Ajuste automático e manual dos clusters conforme a demanda.

- Eficiência de Custo: Criação de clusters sob demanda, pagando apenas pelos recursos utilizados.

- Suporte a Múltiplos Frameworks: Compatível com Hadoop, Spark, Hive, entre outros.

- Monitoramento e Logs: Ferramentas para monitorar desempenho e acessar logs.

#### Componentes
- Cluster: Conjunto de VMs que processam dados, gerenciado automaticamente pelo Dataproc.

- Jobs: Tarefas enviadas ao cluster, como Spark ou Hadoop.

- Nodes: VMs dentro do cluster que executam o processamento.

- Inicializadores de Cluster: Scripts para configurar clusters na criação.

- Templates de Trabalho: Configurações reutilizáveis para jobs.

#### Casos de Uso
- Processamento de dados em larga escala.

- Análise de dados complexos.

- Treinamento de modelos de machine learning.

- Integração de dados de diversas fontes.

- Geração de relatórios e dashboards.

#### Benefícios
- Gerenciamento Simplificado: Facilita a configuração e o gerenciamento de clusters.

- Escalabilidade Flexível: Ajuste de capacidade conforme a demanda.

- Custo-Efetivo: Pagamento apenas pelos recursos utilizados.

- Integração Nativa: Conexão fácil com outros serviços do Google Cloud.

#### Desafios
- Complexidade de Frameworks: Requer conhecimento especializado em Hadoop e Spark.

- Gerenciamento de Dados: Desafios relacionados à eficiência e desempenho.

- Custo: Pode ser alto para clusters de longa duração ou tarefas intensivas.

#### Documentação
#### Documentação do Dataproc sem servidor:
O Dataproc sem servidor permite executar cargas de trabalho do Apache Spark em lote sem a necessidade de provisionar ou gerenciar clusters. O serviço gerencia automaticamente a infraestrutura e escala os recursos conforme necessário, cobrando apenas pelo tempo de execução das cargas de trabalho.

---

#### Composer
#### Introdução
Serviço gerenciado de orquestração de workflows baseado em Apache Airflow, usado para criar, executar e monitorar pipelines de dados complexos.

#### Características
- Automação de Workflows: Simplifica o gerenciamento e a escalabilidade de workflows.

- Integração com Google Cloud: Conecta-se facilmente com serviços como BigQuery, Cloud Storage e Dataproc.

- Interface Gráfica: Oferece uma UI web para visualizar e gerenciar workflows.

- Segurança e Compliance: Integra-se com ferramentas do Google Cloud para proteger dados.

#### Componentes
- DAG (Directed Acyclic Graph): Estrutura que define a sequência e as dependências das tarefas.

- Tarefas e Operadores: Unidades de trabalho e blocos de construção para executar operações.

- Executores e Hooks: Componentes que executam tarefas e conectam com sistemas externos.

#### Casos de Uso
- Orquestração de Pipelines ETL: Automatiza a extração, transformação e carregamento de dados.

- Automação de Processos: Coordena tarefas e processos complexos.

- Integração de Dados: Facilita a sincronização e fluxo de informações entre sistemas.

#### Benefícios
- Gerenciamento Simplificado: Reduz a complexidade de gerenciar workflows.

- Integração Nativa: Melhor eficiência na construção de pipelines de dados com o Google Cloud.

- Escalabilidade: Ajusta recursos conforme a demanda.

#### Desafios
- Complexidade de Configuração: Requer conhecimento detalhado do Airflow.

- Curva de Aprendizado: Exige tempo para dominar a ferramenta.

- Custo: Pode aumentar com a complexidade dos workflows.

---

#### Functions
#### Introdução
É um serviço de computação serverless que permite executar código em resposta a eventos, sem a necessidade de gerenciar servidores.

#### Características
- Serverless: Gerenciamento automático de infraestrutura, focando apenas no código.

- Escalabilidade Automática: Ajusta automaticamente a capacidade conforme a demanda.

- Execução Baseada em Eventos: Responde a eventos como mudanças em Cloud Storage ou mensagens do Pub/Sub.

- Integração com Google Cloud: Funciona bem com outros serviços do Google Cloud.

- Preços Baseados em Uso: Custo calculado pelo número de execuções e tempo de computação.

#### Componentes
- Funções: Unidades de código que executam tarefas específicas.

- Gatilhos (Triggers): Eventos que disparam a execução da função.

- Eventos: Dados passados para a função durante sua execução.

- Ambiente de Execução: Configurado automaticamente, incluindo o tempo de execução e recursos necessários.

- Configuração de Funções: Inclui variáveis de ambiente e permissões.

#### Casos de Uso
- APIs e Webhooks: Criação de APIs RESTful e webhooks.
- Processamento de Arquivos: Automatização de tarefas como redimensionamento de imagens.
- Integração de Dados: Conexão e transformação de dados entre diferentes sistemas.
- Automação de Processos: Automatização de tarefas em tempo real.
- Reação a Eventos: Resposta a eventos em tempo real.

#### Benefícios
- Simplicidade: Menos complexidade operacional.

- Escalabilidade: Gerenciamento automático de tráfego.

- Custo-Efetividade: Pagamento conforme o uso real.

- Integração: Fácil integração com outros serviços do Google Cloud.

#### Desafios
- Limitações de Tempo de Execução: Não ideal para tarefas longas.
- Gerenciamento de Estado: Necessidade de serviços adicionais para persistência de dados.
- Gerenciamento de Dependências: Requer configuração adequada das dependências da função.

#### Documentação
#### Cloud Functions
permite executar código na nuvem sem gerenciar servidores ou contêineres, usando um modelo de funções como serviço (FaaS) com pagamento por utilização.

#### Recursos
- Experiência Simplificada: Executado sem necessidade de gerenciamento de infraestrutura.

- Pagamento por Uso: Cobrança baseada no tempo de execução da função.

- Tecnologia Aberta: Compatível com diversos ambientes sem servidor e frameworks FaaS.

#### Benefícios
- Desenvolvimento Ágil: Foco no desenvolvimento com menos preocupação sobre a infraestrutura.

- Escalabilidade Automática: Recursos ajustados automaticamente conforme a demanda.

- Custo-Efetivo: Pagamento somente pelo uso real da função.

#### Casos de Uso
- Integração com APIs e Serviços de Terceiros.

- Back-ends para Dispositivos Móveis e IoT.

- Processamento de Arquivos e Streams em Tempo Real.

- Assistentes Virtuais e Experiências de Conversa.

- Análise de Vídeo, Imagem e Sentimentos.

#### Preços
O custo é baseado no tempo de execução, número de invocações e recursos provisionados. Clientes novos recebem US$ 300 em créditos e dois milhões de invocações gratuitas por mês.

#### Novidades
Cloud Functions (2ª geração): Oferece opções de computação mais avançadas, controle granular e novos gatilhos.