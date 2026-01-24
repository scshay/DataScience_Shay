import pandas as pd
import matplotlib.pyplot as plt
import os

# --- CONFIGURAÇÕES ---
# Fonte dos dados: MIT-BIH Arrhythmia Database (Simple CSVs) - https://www.kaggle.com/datasets/protobioengineering/mit-bih-arrhythmia-database-modern-2023?resource=download
# O arquivo 100_annotations_1.csv deve estar na mesma pasta do script
FILENAME = r'C:\DataScience_Shay\Santander2025_Ciencia-de-Dados-com-Python\Explorando-IA-Generativa-em-um-Pipeline-de-ETL-com-Python\100_annotations_1.csv'
SAMPLING_RATE = 360  # Hz (Frequência de amostragem do dataset MIT-BIH)

def run_etl_process():
    print("Iniciando Processo ETL de Monitoramento Cardíaco...")

    # --- 1. EXTRACT ---
    try:
        df = pd.read_csv(FILENAME)
        print(f"Extração concluída: {len(df)} registros carregados.")
    except FileNotFoundError:
        print(f"Erro: O arquivo {FILENAME} não foi encontrado.")
        return

    # --- 2. TRANSFORM: Calcula a Variabilidade da Frequência Cardíaca (HRV) ---
    # Diferença entre amostras consecutivas (Intervalo R-R)
    df['rr_interval_samples'] = df['index'].diff()

    # Converte amostras para segundos (Tempo = Amostras / Frequência)
    df['rr_interval_seconds'] = df['rr_interval_samples'] / SAMPLING_RATE

    # Calcula Batimentos por Minuto (BPM) -> 60s / intervalo_em_segundos
    df['bpm'] = 60 / df['rr_interval_seconds']

    # --- Data Cleaning ---
    # Removemos o primeiro valor (NaN) e filtramos ruídos técnicos (batimentos irreais)
    df_clean = df.dropna(subset=['bpm']).copy()
    df_clean = df_clean[(df_clean['bpm'] >= 30) & (df_clean['bpm'] <= 200)]

    # Identificação de Anomalias (Onde o símbolo é 'A' de Arritmia Atrial)
    df_clean['is_anomaly'] = df_clean['annotation_symbol'] == 'A'

    print("Transformação concluída: Métricas de saúde calculadas com sucesso.")

    # --- 3. LOAD (Carregamento / Visualização) ---
    # Exportando o Data Warehouse processado
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_csv = os.path.join(script_dir, 'paciente_100_metricas_saude.csv')
    df_clean.to_csv(output_csv, index=False)

    # Gerando Dashboard Visual
    plt.figure(figsize=(15, 6))

    # Eixo X: Convertendo o índice de amostras para Minutos
    time_minutes = df_clean['index'] / (SAMPLING_RATE * 60)
    
    # Plot do Ritmo Cardíaco
    plt.plot(time_minutes, df_clean['bpm'], label='Frequência Cardíaca (BPM)', color='#2c3e50', alpha=0.7)

    # Destaque das Anomalias (Arritmias)
    anomalies = df_clean[df_clean['is_anomaly']]
    plt.scatter(anomalies['index'] / (SAMPLING_RATE * 60), anomalies['bpm'],
                color='red', label='Arritmia Atrial Detectada', s=60, zorder=5)

    plt.title('Dashboard de Monitoramento Cardíaco: Paciente 100', fontsize=14)
    plt.xlabel('Tempo (Minutos)', fontsize=12)
    plt.ylabel('Batimentos por Minuto (BPM)', fontsize=12)
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.5)

    # Salvando o resultado visual
    plt.tight_layout()
    output_png = os.path.join(script_dir, 'monitoramento_cardiaco_final.png')
    plt.savefig(output_png)
    plt.show()

    print(f"Processo finalizado!")
    print(f"📄 CSV: {output_csv}")
    print(f"📊 Gráfico: {output_png}")

if __name__ == "__main__":
    run_etl_process()