import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt



with st.echo(code_location='below'):

    """
    ## Spotify top 100
    """

    st.write(
        'Данная работа основана на данных о ежегодном плейлисте 100 лучших песен в Spotify за 2010-2019. В таблице, помимо автора, названия '
        'композиции, длительности, года выхода присутствуют еще несколько параметров, которые определяет алгоритм Spotify. Это такие параметры, как'
        ' bpm, энергичность трека, танцевальность, настроение, акустичность и популярность.'
        'Все эти параметры были определены в момент создания датафрейма')



    @st.cache
    def get_data():
        return (
            pd.read_csv("Spotify 2010 - 2019 Top 100.csv").dropna(how='all')
        )


    df = get_data()
    df = df.astype({'top year': 'int'})
    df = df.astype({'year released': 'int'})
    df = df.rename(columns={'nrgy': 'energy', 'dnce': 'dance', 'val': 'mood', 'dur': 'duration', 'acous': 'acoustic',
                            'spch': 'speech','pop': 'popularity'})
    df = df.astype({'bpm': 'int'})
    df = df.astype({'energy': 'int'})
    df = df.astype({'dance': 'int'})
    df = df.astype({'mood': 'int'})
    df = df.astype({'duration': 'int'})
    df = df.astype({'acoustic': 'int'})
    df = df.astype({'speech': 'int'})
    df = df.astype({'popularity': 'int'})

    del df['added']
    del df['dB']
    del df['live']
    del df['speech']

    st.write(df)

    st.write(
        'В следующем виджете в списке есть все артисты, попавшие в изначальный датафрейм. '
        'Можно найти интересующего исполнителя, набрав его псевдоним, или выбрав из списка, который упорядочен по убыванию общего количества треков исполнителя в датафрейме')

    artist = st.selectbox(
        "artist", df["artist"].value_counts().iloc[:500].index
    )

    df_selection = df[lambda x: x["artist"] == artist]
    df_selection


    st.write('Параметр Popularity для песни считается в настоящий момент времени. На следующем графике изображен средний рейтинг топ-100 по годам. '
             'Заметно, что средний рейтинг по годам растет. Это отражает "смену поколений" среди музукальных предпочтений: хиты 3-х летней давности более популярны сейчас'
             ', чем хиты 10-летней давности')

    Ypop=df.groupby(['top year'])['popularity'].mean()

    st.write(Ypop)

    fig, ax = plt.subplots()
    df1 = pd.DataFrame({'Year': np.array([2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]), 'Popularity': np.array([70.1800, 73.0500, 72.8500, 73.8100, 74.3200, 75.2800, 75.0900, 77.8100, 77.5800, 78.4300])})
    sns.lineplot(x='Year', y='Popularity', data=df1)
    st.pyplot(fig)

    st.write(
        'Самые устаревшие жанры (сортировка по рейтингу)')

    Typepop = df.groupby(['top genre'])['popularity'].mean().sort_values().iloc[:10]

    st.write(Typepop)

    st.write(
        'Следующий график показывает связь между энергичностью композиции (x) и ее настроением (y). '
        'Ожидаемо, можно увидеть небольшую положительную корреляцию ')

    fig = plt.figure()
    (plt.scatter(df['energy'], df['mood'], s=0.4))
    st.write(fig)

    st.write(
        'Этот график показыает связь уже между bpm и настроением композиции. '
        'Кажется, что bpm и энергичность показывают почти одно и тоже, но на этом графике мы уже не видим положительной связи ')

    fig = plt.figure()
    (plt.scatter(df['bpm'],df['mood'], s=0.4))
    st.write(fig)






