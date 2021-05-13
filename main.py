import streamlit as st
import codecs
import src.manage_data as dat
import plotly.express as px
import pandas as pd
import folium
from streamlit_folium import folium_static
import streamlit.components.v1 as components
from PIL import Image

imagen = Image.open("images/portada2.jpg")
st.image(imagen)

st.write("""
# My awesome app
Con Jake el perro y Finn el humano lo pasaremos guaaaaaaaay
"""
)

st.dataframe(dat.carga_data())

st.write("""
### Grafiquito de Barras propio de streamlit
"""
)

datos_grafico = dat.grafico_barras_st()
st.dataframe(datos_grafico)

st.bar_chart(datos_grafico)


st.write("""
### Grafiquito de Plotly

""")

person = st.selectbox(
    "Selecciona un personaje", dat.lista_personajes()
)

datagraf = dat.grafico(person)

fig = px.line(datagraf, y="polarity", title = f"Evolución de la polaridad de {person}",
labels = {"index": "Frases"}
)

st.plotly_chart(fig)
st.write("""
### Formulario de texto

""")
texto = st.text_input('Indicamos lo que tiene que introducir', 'Texto por defecto')
st.write("Ha introducido: ", texto)
st.write("""
### Gestor de archivos

""")

uploaded_file = st.file_uploader("Sube un csv")
if uploaded_file: 
    dataframe = pd.read_csv(uploaded_file)
    st.write(dataframe)

foto = st.file_uploader("Sube uba foto")
if foto: 
    imagen = Image.open(foto)
    imagen.save('data/foto.png')
    st.write("tu foto se ha subido correctamente")


st.write("""
### Columnas

""")

datos = dat.bar_2()

col1,col2 = st.beta_columns([4,2])

col1.subheader("El gráfico")
col1.bar_chart(datos)

col2.subheader("Los datitos")
col2.write(datos)


st.write("""
### Mapita de Folium

""")

map_1 = folium.Map(location = [40.4143851,-3.6820241], zoom_start = 15)
folium_static (map_1)



st.write("""
### Mapita insertado con HTML

""")

archivo = codecs.open("data/mapa.html",'r')
mapa = archivo.read()

components.html(mapa, height = 550)