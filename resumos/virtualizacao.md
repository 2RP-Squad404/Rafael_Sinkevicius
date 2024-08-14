### Virtualização:

#### Tópicos:
- VMs
    - Introdução
    - Características
    - Componentes
    - Casos de Uso
    - Benefícios
    - Desafios
    - Artigo
- Docker
    - Introdução
    - Características
    - Casos de Uso
    - Benefícios
    - Desafios
- Kubernetes
    - Introdução
    - Características
    - Componentes
    - Casos de Uso
    - Benefícios
    - Desafios
    - Vídeo

#### VMs:
#### Introdução
São emulações de computadores físicos dentro de um ambiente de software, permitindo a execução de vários sistemas simultaneamente em um único hardwere físico.

#### Características
- Isolamento(permite executar deiferentes sistemas sem interferir entre si)

- Recursos Compartilhados(compartilham recursos como CPU, memória e armazenamento com o respectivo hardware, de forma independente)

- Portabilidade(podem ser movidas entre diferentes servidores físicos, permitindo flexibilidade)

- Escalabilidade(facilita a criação e gerenciamento de isntâncias conforme a demanda)

- Gerenciamento simplificado(gerenciamento centralizado e automatizado)

#### Componentes
- Hypervisor: cria e gerencia VMs, com o tipo Bare-metal(executa diretamente no hardware d servidor, como VMware ESXi) e o tipo Hosted(Executa sobre um sistema operacional host, como VMware Workstation)

- Imagens de Máquina Virtual: Arquivos nacessários para iniciar e operar uma máquina virtual

- Virtualização de hardware: emula os recursos de hardware para as máquinas virtuais, funcionando como um hardwere físico dedicado.

- Recursos virtuais: recursos são alocados conforme a necessidade.

#### Casos de Uso
- Consolidação de Servidores(execução de várias VMs em um único servidor físico)

- Ambientes de Desenvolvimento e Teste

- Execução de Sistemas Legados(execução de sistemas antigos através da virtualização)

- Recuperação de Desastres(backups)

- Escalabilidade em nuvem(escalar aplicações facilmente sob demanda).

#### Benefícios
Eficiência de recursos, flexibilidade e portabilidade e isolamento e segurança.

#### Desafios
Overhead de desempenho, gerenciamento de recursos e complexidade(exige ferramentas adequadas para lidar com a complexidade da gestão de múltiplas máquinas)

#### Artigo
#### O que é uma Máquina virtual e como ela funciona | Microsoft Azure:
O artigo sobre VMs explica que são computadores virtuais dentro de computadores físicos, tendo sua própria CPU, memória, armazenamento e sistema operacional, sendo usadas para diversos propósitos, como o desenvolvimento e teste de software, execução de aplicações antigas e criaçao de ambientes em nuvem híbrida, oferecendo diversos benefícios, como economia de custos, agilidade, escalabilidade e segurança, com o Azure(Microsoft) oferecendo diversos tipos de VMs para diferentes necessidades.

Pontos importantes:
- Uma VM é um computador virtual que funciona em um físico

- VMs são usados para inumeros propósitos, como desenvolvimento e teste de software

- VMs oferecem vários benefícios como economia de custos

- O Azure oferece diferentes tipos para diversas necessidades.

#### Docker
#### Introdução
É uma plataforma de software que facilita a criação, distribuição e execução de aplicativos dentro de containers, que são ambientes isolados contendo tudo que um aplicativo precisa para funcionar, como código, bibliotecas e dependências, garantindo o funionamento consistente em ambientes diversos.

#### Características
- Containers

- Imagens Docker(modelos para criar containers)

- Dockerfile(script com instruções para construir uma imagem docker)

- Docker Hub(registro público de imagens Docker)

- Docker Compose(ferramenta para definir e gerenciar aplicações multi-container)

#### Casos de Uso
Desenvolviemento e teste, implantação de aplicações, microserviços, isolamento e segurança e automação e CI/CD(se integra bem com pipelines de integração e entrega contínua)

#### Benefícios
Portabilidade(funcionam da mesma forma em qualquer ambiente), consistência(o app tem o mesmo comportamento em todos os ambientes), eficiência(containers são mais leves) e isolamento(ambiente isolado para cada container)

#### Desafios
Gerenciamento de containers(ebora simplificado pode ser complexo e exigir ferramentas como Kubernetes), persistência de dados(são efêmeros, complicando a gestão de dados persistentes) e segurança(embora isolados, compartilham o mesmo kernel)

#### Kubernetes
#### Introdução
É uma plataforma de código aberto para gerenciamento de clusters de containers, com alta disponibilidade, escalabilidade e flexibilidade, automatizando a implantação de aplicativos em containers.

#### Características 
- Orquestração de containers(automatiza o gerenciamento de containers em um cluster)

- Escalabilidade(permite o dimensionamento automático de aplicações)

- Desdobramento e Atualização(Facilita a atualização constante de aplicativos)

- Auto-recuperação(monitora a saúde dos containers e dos nós do cluster, substituindo automaticamente containers com falhas)

- Gerenciamento de Configuração e Segredos(separa dados de config. do código)

- Serviços e Networking(facilita a comunicação entre containers e aplicações)

#### Componentes 
- Pod(menor unidade de implantação no Kubernetes)

- Node(máquina física opu virtual que executa os Pods)

- Cluster(conjunto de Nodes para executar aplicações em containers)

- Master Node(nó central que coordena o cluster, gerenciando a comunicação entre os Nodes e controlando a execução dos Pods)

- Deployment(Um objeto que define como um conjunto de Pods deve ser executado e gerenciado)

- Service(expõe Pods como um serviço de rede)

- ConfigMap e Secret(separa configurações e informações sensíveis do código dos containers)

- Ingress(Gerencia o acesso externo aos serviços dentro do cluster baseado em regras de URL e host)

#### Casos de Uso
Implantação de aplicações em microserviços, escalabilidade e alta disponibilidade, desdobramento contínuo, ambientes multi-cloud e hibridos e gerenciamento de recursos e configurações.

#### Benefícios
Automatização, Flexibilidade, Resiliência e Portabilidade.

#### Desafios
Complexidade, Sobrecarga de Recursos e Curva de Aprendizado.

#### Vídeo
#### Docker Containers and Kubernetes Fundamentals – Full Hands-On Course