import pandas as pd 

def renombra_id(x):
    x = f"Frase {x}"
    return x


def carga_data():
    data = pd.read_pickle("data/clean.pkl")
    return data

def grafico_barras_st():
    data = carga_data()
    data = data.groupby("character_name").agg({"character_name":'count'}).rename(columns={"character_name":"character_name", "character_name":"número de frases"}).reset_index().set_index("character_name", drop=True)
    return data



def lista_personajes():
    data = carga_data()
    return list(data.character_name.unique())

def grafico(personaje):
    data = carga_data()
    data = data[(data["character_name"] == f"{personaje}")]
    data = data[["frase","polarity"]].reset_index(drop=True)
    data["frase"] = data.index+1
    data["frase"] = data.frase.apply(renombra_id)
    return data

def bar_2():
    data= carga_data()
    data = data.groupby("character_name").agg({"polarity":"mean"}).reset_index().set_index("character_name", drop=True)
    return data