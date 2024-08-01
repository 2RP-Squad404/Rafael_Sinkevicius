# Relatório Semanal: Semana 1

## Nome:
Rafael Sinkevicius

## Trilha de Conhecimento:
Data Science

## Período:
29.07.2024-02.08.2024

---

## Conteúdos Estudados:

### Git:

#### Tópicos:
- O que é
- Principais conceitos
- Benefícios
- GitFlow
- Componentes GitFlow
- Fluxo de Trabalho
- Benefícios Gitflow
- Cursos e Artigos

#### O que é:
Sistema de controle de versão para rastrear alterações em arquivos e coordenar o trabalho de vários em projetos de desenvolvimento de software.

#### Principais conceitos:
- **Repositório:** Diretório de armazenamento de histórico de mudanças, inclui pastas e arquivos.
- **Commit:** Snapshot do projeto de um ponto específico. Cada um tem seu identificador (hash).
- **Branch:** Ramificação que permite trabalhar em diferentes linhas ao mesmo tempo, sendo sua principal chamada "main" ou "master".
- **Merge:** Mudanças de diferentes branchs em uma branch.
- **Pull:** Atualiza a cópia local do repositório com o repositório remoto.
- **Push:** Envia mudanças do repo local para o remoto.
- **Clone:** Copia o repositório remoto para o local.
- **Fork:** Cópia de um repo, sem afetar o original.

#### Benefícios:
- **Controle de versão:** Mantém o histórico de mudanças, podendo reverter para versões anteriores.
- **Colaboração:** Facilita o trabalho em equipe, permitindo o trabalho simultâneo.
- **Distribuído:** Cada desenvolvedor tem sua cópia do repo, aumentando a flexibilidade.

#### Cursos e Artigos:
### Introdução ao GIT
**Nome do Curso:** Git e Github para iniciantes 
**Instituição:** Udemy

### Objetivo do Curso
Aprender o que é controle de versão, como lidar com o Git e seus comandos e como subir código no Github.

### Conteúdo Programático
1. **Módulo 1:** Entendendo o que é Git e Github
   - Introdução
   - Controle de versão
   - História do Git
   - O que é Github

2. **Módulo 2:** Configurando o Git
   - Configuração inicial do Git

3. **Módulo 3:** Essencial do Git
   - Inicializando um repositório
   - Usando o editor do terminal
   - O ciclo de vida dos status de seus arquivos
   - Visualizando logs
   - Visualizando o diff
   - Desfazendo coisas

4. **Módulo 4:** Repositórios Remotos
   - Introdução
   - Controle de versão
   - História do Git
   - O que é Github

#### Introdução GitFlow:
É um modelo de branching para o gerenciamento de branches de forma organizada em projetos de larga escala.

#### Componentes GitFlow:
1. **Branches Principais:**
    - **main:** Contém o código estável. Todo commit nesta branch é uma nova versão de lançamento
    - **develop:** Contém o código em desenvolvimento com as alterações aprovadas. É base para novas integrações e funcionalidades.
2. **Branches de Suporte:**
    - **feature:** Usada para novas funcionalidades. Deriva da develop e volta a develop quando concluida.
    - **realease:** Usada para o lançamento de uma nova versão. Deriva da develop e volta para a main e develop.

#### Fluxos de Trabalho
1. **Desenvolvimento de Funcionalidades:**
    - Cria a feature a partir da develop.
    - Nova funcionalidade.
    - Volta a feature para a develop.
2. **Preparação para Lançamento:**
    - Cria a release a partir da develop.
    - Ajustes e correções.
    - Volta a release em main e develop e commit com tag.
3. **Correções Urgentes:**
    - Cria a hotfix a partir da main.
    - Correção necessária.
    - Volta a hotfix em main e develop e commit com tag.

#### Benefícios GitFlow:
- **Organização:** Estrutura para gerenciamento de varios tipos de trabalho.
- **Paralelismo:** Facilita o trabalho simultâneo.
- **Estabilidade:** Garante o estado estável contínuo do código.

- #### Cursos e Artigos:
- **Gitflow conceito:**
- **Gitflow cheatsheet:**
- **Gitflow extention:**