#### Linux/Shell

#### Tópicos:
- Shell Script
    - Introdução
    - Conceitos
    - Importância
    - Exemplos
    - Conclusão
    - Documentação

#### Introdução
Shell Script é um arquivo de texto com comandos que o shell Unix ou Linux pode executar. É usado para automatizar tarefas repetitivas e simplificar comandos complexos.

#### Conceitos
- Shell: Programa que fornece uma interface de linha de comando, como Bash, Zsh e Sh.

- Script: Arquivo contendo comandos para o shell executar, podendo incluir variáveis, loops, condicionais e funções.

- Comandos: Instruções executáveis pelo shell, como ls (listar arquivos) e cp (copiar arquivos).

- Variáveis: Armazenam dados para uso em comandos e operações.

- Loops e Condicionais: Estruturas de controle para repetir comandos ou tomar decisões (ex.: for, while, if, else).

- Funções: Blocos reutilizáveis de comandos que facilitam a modularização e manutenção.

#### Importância
- Automatização de Tarefas: Reduz erros e economiza tempo ao automatizar tarefas como backups e monitoramento.

- Eficiência e Produtividade: Executa operações complexas com um único comando, aumentando a produtividade.

- Administração de Sistemas: Essencial para configuração e gestão de sistemas Unix e Linux.

- Desenvolvimento e Testes: Facilita a compilação, execução de testes e gerenciamento de ambientes.

- Flexibilidade e Controle: Permite personalizar e adaptar soluções para necessidades específicas.

- Facilidade de Aprendizado: Relativamente fácil para quem já usa a linha de comando.

#### Exemplos
1. Script de Backup:
```
bashCopiar código
#!/bin/bash
tar -czf /backup/meuarquivo_backup_$(date +%F).tar.gz /meuarquivo
```

2. Script de Verificação de Espaço em Disco:
```
bashCopiar código
#!/bin/bash
echo "Espaço disponível em disco:"
df -h
```

3. Script de Monitoramento de Processos:
```
bashCopiar código
#!/bin/bash
if pgrep "processo_exemplo" > /dev/null
then
    echo "O processo está em execução."
else
    echo "O processo não está em execução."
fi
```

#### Conclusão
Aprender shell scripting é fundamental para automação, aumento de eficiência e controle sobre sistemas Unix/Linux, sendo uma habilidade prática e valiosa para administradores, desenvolvedores e outros profissionais.

#### Documentação
#### Bash Commands Cheat Sheet
Bash é um interpretador de comandos com muitos aprimoramentos que é uma versão contemporânea do shell Unix clássico. É o shell padrão da GNU/Linux e de vários sistemas Unix, como o macOS. Muitos desenvolvedores sabem como usar Bash de forma interativa, mas poucos sabem como ele funciona para scripts.

#### Exemplos
Loop while:
Executa continuamente até que uma condição seja atendida.
```
x=1;
while [ $x -le 5 ]; do
  echo "Hello World"
  ((x=x+1))
done
```

Trabalhando com Códigos de Status:
Relata sucesso e erro com códigos de status. Sucesso é indicado por 0; qualquer número maior indica erro.

Código de exemplo para verificar parâmetros:
```
if [ -z "$1" ]; then
  echo "No parameter";
  exit 22;
fi
```