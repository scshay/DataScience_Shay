# Guia Rápido de Comandos CMD (Windows)

Este guia prático contém os comandos mais utilizados no Prompt de Comando (CMD) do Windows para navegação, manipulação de arquivos, rede e sistema.

## 1. Navegação e Diretórios

| Comando | Descrição | Exemplo |
| :--- | :--- | :--- |
| **`cd`** | Exibe o diretório atual ou muda de pasta. | `cd Documents` |
| **`cd ..`** | Volta para a pasta anterior (diretório pai). | `cd ..` |
| **`cd \`** | Vai direto para a raiz do disco (ex: C:\). | `cd \` |
| **`dir`** | Lista todos os arquivos e pastas do diretório atual. | `dir` |
| **`mkdir`** ou **`md`** | Cria uma nova pasta. | `mkdir NovaPasta` |
| **`rmdir`** ou **`rd`** | Remove uma pasta (deve estar vazia). | `rmdir NovaPasta` |

## 2. Manipulação de Arquivos

| Comando | Descrição | Exemplo |
| :--- | :--- | :--- |
| **`echo`** | Exibe mensagens ou grava texto em um arquivo. | `echo Texto > arquivo.txt` |
| **`type`** | Exibe o conteúdo de um arquivo de texto no terminal. | `type arquivo.txt` |
| **`copy`** | Copia um ou mais arquivos para outro local. | `copy foto.jpg D:\Backup` |
| **`move`** | Move arquivos ou renomeia pastas. | `move arquivo.txt D:\Backup` |
| **`del`** | Exclui um ou mais arquivos. | `del arquivo.txt` |
| **`ren`** | Renomeia um arquivo ou pasta. | `ren antigo.txt novo.txt` |

## 3. Rede e Conectividade

| Comando | Descrição | Exemplo |
| :--- | :--- | :--- |
| **`ipconfig`** | Exibe as configurações de IP e rede do computador. | `ipconfig` |
| **`ping`** | Testa a conectividade com um site ou IP. | `ping google.com` |
| **`tracert`** | Traça a rota de pacotes até o destino. | `tracert google.com` |
| **`netstat`** | Mostra todas as conexões de rede ativas. | `netstat -a` |

## 4. Informações e Sistema

| Comando | Descrição | Exemplo |
| :--- | :--- | :--- |
| **`systeminfo`** | Exibe detalhes sobre o sistema operacional e hardware. | `systeminfo` |
| **`tasklist`** | Lista todos os processos e programas rodando no momento. | `tasklist` |
| **`taskkill`** | Encerra um processo ou programa em execução. | `taskkill /IM notepad.exe /F` |
| **`cls`** | Limpa a tela do terminal. | `cls` |
| **`exit`** | Fecha o prompt de comando. | `exit` |

## 5. Redirecionadores Úteis

* **`>`** : Cria ou substitui o conteúdo de um arquivo com a saída do comando. (Ex: `dir > lista.txt`)
* **`>>`** : Adiciona a saída do comando ao final de um arquivo existente. (Ex: `echo Novo texto >> lista.txt`)
* `echo Texto > arquivo.txt`  -> Cria o arquivo ou substitui todo o seu conteúdo pelo novo texto.
* `echo Texto >> arquivo.txt` -> Mantém o conteúdo existente e adiciona o novo texto na última linha.