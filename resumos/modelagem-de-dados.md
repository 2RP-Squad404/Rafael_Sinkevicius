# Relatório Semanal: Semana 1

## Nome:
Rafael Sinkevicius

## Trilha de Conhecimento:
Data Science

## Período:
05.08.2024-09.08.2024

---

## Conteúdos Estudados:

### Modelagem de Dados:

#### Tópicos:
- Conceito
- Tipos
- Processo
- Benefícios
- Ferramentas
- Exemplos
- Curso


#### Conceito:
É o processo de criação de um modelo lógico para relações entre diferentes tipos de dados. A modelagem de dados garante a organização, acesso e manipulação precisa.

#### Tipos:
Dentre os tipos, existem o Modelo Conceitual (Foca na organização e definição dos principais conceitos, como Diagrama de Entida-Relacionamento (ERD)), Modelo Lógico (Detalha o modelo conceitual, de forma mais técnica, sem implementações fisícas) e Modelo Físico (Define a implementação do modelo lógico no banco de dados, incluindo aspectos técnicos de armazenamento)

#### Processo:
O processo inclui coleta de requisitos, criação do modelo conceitual, lógico e físico, validação e refinamento e por último a implementação.

#### Benefícios:
Permite claridade e consistência na compreensão dos dados e relações, eficiência e armazenamento de acesso rápido, qualidade dos dados evitando redundância e inconsistencia e facilidade de manutenção permitindo o controle de ajustes e expanções.

#### Ferramentas:
- ER/Studio
- IBM InfoSphere Data Architect
- Microsoft Visio
- Oracle SQL Developer Data Modeler
- PowerDesigner
- MySQL Workbench

#### Exemplos:
As aplicações são Sistemas de Gerenciamento de Relacionamentos com o Cliente (CRM), Sistemas de Planejamento de Recursos Empresariais (ERP) e Data Warehousing (Integra e estrutura dados para análise e relatórios).

#### Curso:
### Introdução a Modelagem de Dados
**Nome do Curso:** Curso Modelagem de Dados e SQL | Guia Para Iniciantes
**Platafoma:** Youtube

### Objetivo do Curso
explicar os fundamentos mais importantes de banco de dados e apresentar uma metodologia passo a passo para estruturar os dados e transformar em aplicativo.

1. **Tópicos do Vídeo:**
   - Fundamentos Banco de Dados SQL e NoSQL
   - Modelagem de Banco de Dados 
   - Modelo Conceitual 
   - Modelo Lógico 
   - Modelo Físico
   - Modelagem dentro de um Plataforma Nocode
   - Banco de Dados Bubble 

**Resumo:**
O curso é direcionado para o entendimento dos fundamentos de banco de dados relacionais, como as conexões entre tabelas por meio de PKs e FKs. O curso também aborda sobre os modelos conceitual, lógico e físico. Além disso, fornece uma base para aplicações web e análise de dados, abordando as principais plataformas do mercado, como  o PostgreSQL. Também há uma parte onde utilizamos a ferramenta no-code, Bubble, que permite a criação de aplicações web com integração entre backend e frontend sem a necessidade de código, mostrando ser uma ótima ferramenta para iniciantes que desejam desenvolver aplicativos de forma simples e rápida. 

**Atividade feita em vídeo:**
```mermaid
erDiagram
    ALUNOS {
        int aluno_id PK
        varchar aluno_nome
        varchar aluno_CPF
        varchar aluno_email
        varchar aluno_telefone
        varchar end_rua
        varchar end_bairro
        date aluno_nasc
    }

    ALUNOS_CURSO {
        int aluno_id PK
        int curso_id PK
    }

    CURSOS {
        int curso_id PK
        int professor_id FK
        varchar curso_nome
        int curso_duracao
        int curso_valor
    }

    VENDA {
        int venda_id PK
        int aluno_id FK
        int curso_id FK
        timestamp venda_data
        int venda_valor
    }

    PROFESSORES {
        int professor_id PK
        varchar professor_nome
        varchar professor_ferramenta
        date professor_nasc
        varchar professor_telefone
    }

    ALUNOS ||--o{ ALUNOS_CURSO : Possui
    CURSOS ||--o{ ALUNOS_CURSO : Possui
    ALUNOS ||--o{ VENDA : Possui
    CURSOS ||--o{ VENDA : Possui
    PROFESSORES ||--|| CURSOS : Possui

Além do desenvolvimento de um diagrama ER como prática e exemplo, foi ensinado o básico dentro da plataforma Bubble, mostrando como inserir dados manualmente, afim de exemplificar como os dados funcionam e são processados dentro da plataforma, além de uma breve explicação de como desenvolver uma interface visual do aplicativo. 