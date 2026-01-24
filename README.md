# 🫀 Pipeline ETL para Monitoramento Cardíaco

## 📋 Sobre o Projeto

Este projeto implementa um pipeline completo de **ETL (Extract, Transform, Load)** aplicado à área de **saúde cardiovascular**, utilizando dados reais do **MIT-BIH Arrhythmia Database**. O sistema processa sinais de eletrocardiograma (ECG), calcula métricas de saúde cardíaca e identifica anomalias como arritmias atriais.

## 🎯 Objetivo

Demonstrar a aplicação prática de Ciência de Dados na área da saúde, processando dados biomédicos para:
- Extrair informações de arquivos de anotações de ECG
- Transformar sinais brutos em métricas clínicas (BPM, HRV)
- Carregar e visualizar resultados em dashboards médicos

## 🗄️ Fonte dos Dados

**Dataset:** [MIT-BIH Arrhythmia Database (Modern 2023)](https://www.kaggle.com/datasets/protobioengineering/mit-bih-arrhythmia-database-modern-2023)

O MIT-BIH é um dos datasets mais utilizados mundialmente para pesquisa em arritmias cardíacas, contendo:
- 48 registros de ECG de 30 minutos
- Frequência de amostragem: 360 Hz
- Anotações de batimentos cardíacos por cardiologistas

## 🔄 Fluxo do Pipeline ETL

### 1️⃣ **EXTRACT** (Extração)
- Leitura do arquivo CSV com anotações de batimentos cardíacos
- Validação da existência e integridade dos dados

### 2️⃣ **TRANSFORM** (Transformação)
- **Cálculo de Intervalos R-R:** Diferença entre batimentos consecutivos
- **Conversão para BPM:** Cálculo da frequência cardíaca em batimentos por minuto
- **Data Cleaning:** Remoção de outliers e ruídos técnicos (30-200 BPM)
- **Detecção de Anomalias:** Identificação de arritmias atriais (símbolo 'A')

### 3️⃣ **LOAD** (Carregamento)
- **Exportação:** Geração de arquivo CSV com métricas processadas
- **Visualização:** Dashboard interativo mostrando:
  - Frequência cardíaca ao longo do tempo
  - Marcadores visuais de arritmias detectadas
  - Gráfico temporal em minutos

## 📊 Resultados

O pipeline gera automaticamente:

1. **`paciente_100_metricas_saude.csv`** - Data warehouse com métricas calculadas
2. **`monitoramento_cardiaco_final.png`** - Dashboard visual do monitoramento

### Exemplo de Visualização

O gráfico apresenta:
- **Linha cinza:** Frequência cardíaca (BPM) em tempo real
- **Pontos vermelhos:** Arritmias atriais detectadas automaticamente
- **Eixo temporal:** 30+ minutos de monitoramento contínuo

## 🛠️ Tecnologias Utilizadas

- **Python 3.13**
- **Pandas** - Manipulação e análise de dados
- **Matplotlib** - Visualização científica
- **NumPy** - Computação numérica (dependência do Pandas)

## 📦 Requisitos

```bash
pip install pandas matplotlib
```

Ou utilize o requirements.txt:
```bash
pip install -r requirements.txt
```

## 🚀 Como Executar

1. **Clone o repositório:**
```bash
git clone <seu-repositorio>
cd Explorando-IA-Generativa-em-um-Pipeline-de-ETL-com-Python
```

2. **Baixe o dataset:**
   - Acesse o [Kaggle Dataset](https://www.kaggle.com/datasets/protobioengineering/mit-bih-arrhythmia-database-modern-2023)
   - Faça download do arquivo `100_annotations_1.csv`
   - Coloque na mesma pasta do script

3. **Execute o pipeline:**
```bash
python projetoETL.py
```

4. **Verifique os resultados:**
   - Dashboard será exibido automaticamente
   - Arquivos CSV e PNG serão salvos no diretório

## 📁 Estrutura do Projeto

```
📂 Explorando-IA-Generativa-em-um-Pipeline-de-ETL-com-Python/
├── 📄 projetoETL.py                          # Script principal do pipeline
├── 📄 100_annotations_1.csv                  # Dados de entrada (não versionado)
├── 📄 paciente_100_metricas_saude.csv       # Saída: métricas processadas
├── 📊 monitoramento_cardiaco_final.png      # Saída: dashboard visual
├── 📄 README.md                              # Documentação do projeto
└── 📄 requirements.txt                       # Dependências Python
```

## 🧮 Métricas Calculadas

| Métrica | Descrição | Unidade |
|---------|-----------|---------|
| **rr_interval_samples** | Intervalo entre batimentos (amostras) | samples |
| **rr_interval_seconds** | Intervalo entre batimentos (tempo) | segundos |
| **bpm** | Frequência cardíaca | batimentos/min |
| **is_anomaly** | Indicador de arritmia atrial | booleano |

## 🏥 Aplicações Clínicas

Este tipo de análise é fundamental para:
- Monitoramento remoto de pacientes cardíacos
- Detecção precoce de arritmias
- Sistemas de alertas médicos em tempo real
- Pesquisa em cardiologia computacional

## 📚 Referências

- **MIT-BIH Database:** Moody GB, Mark RG. The impact of the MIT-BIH Arrhythmia Database. IEEE Eng in Med and Biol 20(3):45-50 (May-June 2001).
- **PhysioNet:** Goldberger, A., et al. PhysioBank, PhysioToolkit, and PhysioNet: Components of a new research resource for complex physiologic signals. Circulation 101(23):e215-e220.

## 👨‍💻 Autor

Desenvolvido como parte do **Bootcamp Santander 2025 - Ciência de Dados com Python**

## 📄 Licença

Este projeto é educacional e utiliza dados públicos do MIT-BIH Database.

---

⭐ **Se este projeto foi útil para você, considere deixar uma estrela no repositório!**
