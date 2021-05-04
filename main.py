#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 16:17:48 2021

@author: leandro
"""
# Imports
import pandas as pd
import geopandas as gpds
import plotly.express as px
from helper_functions import to_sneake_case
from helper_functions import tratamento_dados
from helper_functions import geocode
from helper_functions import mapa
import plotly.express as px

# Loading Data
df = pd.read_excel('previa.xls')
df1 = df.copy()

# Descrição dos Dados
# Nome das Colunas
colunas = df1.columns

# Chamando a Função para Alterar o Nome das Colunas
novas_colunas = []
to_sneake_case(colunas, novas_colunas)
df1.columns = novas_colunas

# Verificando as Dimensões do Data Frame
print("Este Data Frame possui {} linhas" .format(df1.shape[0]))
print("Este Data Frame possui {} colunas\n" .format(df1.shape[1]))

# Fazendo o tratamento dos dados
tratamento_dados(df1)

# Fazendo geocode
geocode(df1, df1['Cidade'])

# Transformando um Dataframe em um Geodataframe
df2 = df1
gdf = gpds.GeoDataFrame(df2,geometry=gpds.points_from_xy(df2.LONGITUDE,
                                                         df2.LATITUDE))

# Criar mapa
mapa(gdf)


