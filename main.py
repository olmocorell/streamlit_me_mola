from re import T
import streamlit as st
from PIL import Image
from multipage import MultiPage
from pages import home
from pages import datos
from pages import graficos


app = MultiPage()


app.add_page("Index", home.app)
app.add_page("Datitos", datos.app)
app.add_page("Gráficos", graficos.app)


app.run()