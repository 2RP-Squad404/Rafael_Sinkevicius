#### CI/CD

#### Tópicos:
- Introdução
- Conceitos
- Benefícios
- Desafios
- Conclusão
- Vídeos/Documentação

#### Introdução
São práticas essenciais no desenvolvimento de software, automatizando o ciclo do desenvolvimento, melhorando a eficiência e a qualidade.

#### Conceitos
- Integração Contínua (CI - Continuous Integration):

- Definição: Integra alterações de código em um repositório compartilhado várias vezes ao dia. Cada integração é verificada através de builds e testes automatizados.

- Objetivo: Reduzir o risco de problemas de integração e garantir que o código esteja sempre compatível com o código existente.

- Processo:
    - Alterações são enviadas ao repositório.

    - O sistema de CI executa builds e testes automatizados.
    
    - Relatórios são gerados para indicar o sucesso ou falha dos testes.

---

- Entrega Contínua (CD - Continuous Delivery):

- Definição: Mantém o código em um estado que pode ser implantado a qualquer momento. O código é automaticamente implantado em um ambiente de staging ou pré-produção.

- Objetivo: Garantir que o código esteja pronto para produção com o mínimo esforço manual e menor risco.
- Processo:
    - O código é implantado automaticamente em staging.
    
    - Testes adicionais são executados em staging.
    
    - Se os testes forem bem-sucedidos, o código está pronto para produção.

---

- Deploy Contínuo (às vezes chamado de CD - Continuous Deployment):

- Definição: Extensão da entrega contínua onde as alterações são automaticamente implantadas em produção após testes e validações.

- Objetivo: Automatizar completamente a implantação para entregar atualizações rapidamente aos usuários finais.

- Processo:
    - Código é integrado e testado automaticamente.

    - Se todos os testes forem aprovados, a implantação para produção é realizada automaticamente.

#### Benefícios
- Redução de Erros: A automação identifica e corrige erros rapidamente.

- Entrega Mais Rápida: Acelera o processo de construção e implantação.

- Feedback Rápido: Fornece feedback quase em tempo real sobre a qualidade do código.

- Consistência e Reprodutibilidade: Garante que o processo seja consistente e reproduzível em diferentes ambientes.

#### Desafios
- Complexidade de Configuração: Configurar pipelines de CI/CD pode ser complexo, especialmente para projetos grandes.

- Gerenciamento de Dependências: Manter consistência de dependências e configurações pode ser desafiador.

- Segurança: Garantir a segurança durante o CI/CD é crucial para evitar vulnerabilidades e falhas.

#### Conclusão
São práticas fundamentais para o desenvolvimento ágil, promovendo a automação, qualidade e eficiência. Integração contínua e entrega contínua garantem que o código esteja sempre pronto para produção, respondendo rapidamente às demandas e mantendo alta qualidade do software.

#### Vídeo/Documentação
#### Pipeline (CD/CI) // Dicionário do Programador
Explica o que é Pipeline (CD/CI) e como ele funciona. É uma sequência de etapas automatizadas que colocam software em produção de forma rápida e confiável, composta por Integração Contínua (CI) e Entrega Contínua (CD).

#### Benefícios
- Agilidade na entrega de software.

- Redução de erros.

- Simplificação do processo de desenvolvimento.

- Maior visibilidade do progresso do desenvolvimento.

#### Como construir:
- Defina o processo de desenvolvimento.

- Escolha as ferramentas (Jenkins, GitLab CI/CD, CircleCI, AWS CodePipeline).

- Configure a pipeline.

- Monitore e ajuste.

#### O que é CI/CD?
Integração Contínua/Entrega Contínua (também conhecida como Implantação Contínua) é uma abordagem que visa automatizar e acelerar o ciclo de vida do desenvolvimento de software. A integração contínua (CI) inclui mudanças de código em um repositório compartilhado, seguida de testes automatizados. A Implantação Contínua automatiza completamente a distribuição de atualizações diretamente para a produção, enquanto a Entrega Contínua (CD) envia as alterações validadas para um ambiente de pré-produção. Essas práticas melhoram a eficiência, reduzem erros e tornam a entrega de software mais rápida.

#### Documentação do Cloud Build
Cloud Build, um serviço do Google Cloud,  permite a construção de software diretamente na nuvem. Ele pode importar código de fontes como GitLab, GitHub, Bitbucket e Google Cloud Storage e executar builds usando contêineres do Docker, criando artefatos como imagens de contêiner ou arquivos Java. O processo de construção consiste em várias etapas que são realizadas em um contêiner. Você pode usar etapas pré-definidas ou criar etapas de construção personalizadas.