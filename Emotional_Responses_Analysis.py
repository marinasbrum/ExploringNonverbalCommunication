pip install pandas
pip install matplotlib

import pandas as pd 
import matplotlib.pyplot as plt

# Read file
ENC = pd.read_csv('')

def plot_season(dataframe):
    # Agrupa por temporada e episódio e conta o número de olhadas em cada grupo
    looks_per_season = dataframe.groupby(['Season', 'Episode']).size().reset_index(name='looks')

    # Plota um gráfico de linhas para cada temporada
    for season, data_season in looks_per_season.groupby('Season'):
        plt.plot(data_season['Episode'], data_season['looks'], marker='o', label=f'Temporada {season}')

    plt.xlabel('Episódio')
    plt.ylabel('Número de Olhadas por Jim Halpert')
    plt.title('Número de Olhadas de Jim Halpert para a Câmera por Temporada')
    plt.legend()
    plt.grid(True)
    plt.show()

plot_season(ENC)

def plot_ranking(dataframe):
    # Agrupa por influenciador e conta o número de ocorrências
    influencers_counts = dataframe['Influencer'].value_counts()

    # Plota um gráfico de barras
    influencers_counts.plot(kind='bar')
    plt.xlabel('Influenciador')
    plt.ylabel('Número de Ocorrências nas Reações de Jim')
    plt.title('Ranking de Influenciadores nas Reações de Jim')
    plt.grid(axis='y')
    plt.show()

plot_ranking(ENC)

def plot_emotional_responses(dataframe):
    # Obtém uma lista de todos os influenciadores presentes nos dados
    influencers = dataframe['Influencer'].unique()

    # Itera sobre cada influenciador e cria um gráfico de pizza para cada um
    for influencer in influencers:
        # Filtra o DataFrame apenas para as olhadas influenciadas por um determinado influenciador
        influencer_df = dataframe[dataframe['Influencer'] == influencer]

        # Conta o número total de olhadas influenciadas por esse influenciador
        total_looks = len(influencer_df)

        # Conta o número de cada tipo de resposta emocional
        emotional_responses_counts = influencer_df['Emotional_Responses'].value_counts()

        # Calcula a porcentagem de cada tipo de resposta emocional
        percentage = (emotional_responses_counts / total_looks) * 100

        # Plota um gráfico de pizza
        percentage.plot(kind='pie', autopct='%1.1f%%')
        plt.title(f'Distribuição das Respostas Emocionais de Jim para Olhadas Influenciadas por {influencer}')
        plt.ylabel('')
        plt.show()

plot_emotional_responses(ENC)

def plot_prank(dataframe):
    # Filtrar o DataFrame para incluir apenas as olhadas que envolveram uma pegadinha
    pranks_df = dataframe[dataframe['Prank'] == 'Sim']

    # Contar o número de olhadas envolvendo pegadinhas para cada personagem
    prank_counts = pranks_df['Influencer'].value_counts()

    # Filtrar o DataFrame original para incluir apenas as olhadas para cada personagem
    all_looks_counts = dataframe['Influencer'].value_counts()

    # Calcular a porcentagem de olhadas para cada personagem que envolveu uma pegadinha
    prank_percentage = (prank_counts / all_looks_counts) * 100

    # Plotar um gráfico de barras para a porcentagem de pegadinhas por personagem
    prank_percentage.plot(kind='bar')
    plt.xlabel('Personagem')
    plt.ylabel('Porcentagem de Olhadas com Pegadinha')
    plt.title('Porcentagem de Olhadas com Pegadinha por Personagem')
    plt.grid(axis='y')
    plt.show()

plot_prank(ENC)

def plot_looks_with_events(dataframe):
    # Filtrar o DataFrame para incluir apenas os episódios com eventos
    events_df = dataframe[dataframe['Event'] != 'Nenhum']

    # Filtrar o DataFrame para incluir apenas os episódios sem eventos
    no_events_df = dataframe[dataframe['Event'] == 'Nenhum']

    # Contar o número de olhadas em episódios com eventos e sem eventos
    looks_with_events = len(events_df)
    looks_without_events = len(no_events_df)

    # Plotar um gráfico de pizza mostrando a proporção de olhadas com eventos e sem eventos
    plt.pie([looks_with_events, looks_without_events], labels=['Com Eventos', 'Sem Eventos'], autopct='%1.1f%%')
    plt.title('Proporção de Olhadas com e sem Eventos')
    plt.show()

plot_looks_with_events(ENC)
