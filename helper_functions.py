# imports
import folium
from folium.plugins import FastMarkerCluster

# Função para Alterar o nome das colunas para camel_case
#novas_colunas = []
def to_sneake_case(colunas, novas_colunas):
    """Transforma os nomes das colunas par snake case"""
    #novas_colunas = []
    for i in colunas:
        i = i.replace(" ", '_')
        novas_colunas.append(i)
    return

def tratamento_dados(df1):
    """Faz todo o trabalho de tratamento dos dados"""
    # Verificando a Existência de NA 
    print(df1.isna().sum())
    # Tratar as Linhas NA
    # Não preciso tratar as colunas Logradouro e Bairro, pois utilizarei.
    # apenas a coluna CEP e Programa
    # Removendo Dados 'na'
    df1 = df1.dropna(axis=0)
    print(df1)
    # Verificar as distribuições das variáveis Cidade, Programa e
    # Fonte_de_Pagamento
    distribuicao = df1.apply(lambda x: x.unique().shape[0])
    print(distribuicao)
    return    

def geocode(df1, cidade):
    """Criando colunas com geometria de ponto"""
    import geopandas as gpds
    a = 0
    latitude = []
    longitude = []
    endereco = []
    
    while a != len(df1['Cidade']):
        
        for i in df1["Cidade"]:
            end = gpds.tools.geocode(i, provider = "nominatim",
                             user_agent = "Leandro_Custódio")
            endereco.append(end['geometry'])
            longitude.append(end['geometry'][0].y)
            latitude.append(end['geometry'][0].x)
            a = a + 1
            print("Item {} foi processado.".format(a))
        print(" ")
        print("Processamento dos dados realizado com sucesso.")
    df1["ENDEREÇO"] = endereco 
    df1["LONGITUDE"] = longitude
    df1["LATITUDE"] = latitude
    return

def mapa(gdf):
    """Cria o mapa base, insere marcadores e exporta uma arquivo html."""
    # Criando mapa base com o folium
    media_longitude = gdf['LONGITUDE'].mean()
    media_latitude = gdf['LATITUDE'].mean()
    
    ceara = folium.Map(location=[media_longitude,media_latitude],zoom_start=7.5,
                       tiles='stamentoner', width='100%', height='100%')
    mc = FastMarkerCluster(gdf[['LONGITUDE','LATITUDE',]],
                           popup=list(gdf['Programa']))
    ceara.add_child(mc)
    
    ceara.save('promac.html')
      