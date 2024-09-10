import streamlit as st
import pandas as pd
from streamlit_drawable_canvas import st_canvas
import matplotlib.pyplot as plt

# Lista para armazenar as coordenadas e cores
if 'points' not in st.session_state:
	st.session_state['points'] = []

# Definir a cor inicial
if 'color' not in st.session_state:
	st.session_state['color'] = 'blue'

# Exibir o rádio botão para escolher a cor
st.title("Toy Data")
st.write("Choose between red or blue. Click in the Canvas and generate your data!")
selected_color = st.radio("Color:", ('blue', 'red'))
st.session_state['color'] = selected_color

# Configuração do quadro de desenho
canvas_result = st_canvas(
	fill_color=selected_color,  # Cor do ponto
	stroke_width=10,
	background_color="#fff",
	update_streamlit=True,
	height=400,
	width=400,
	drawing_mode="circle",  # Permitir desenhar pontos
	key="canvas"
)

# Verificar se o ponto foi desenhado
if canvas_result.json_data is not None:
	# Limitar o processamento para novos pontos apenas
	if len(canvas_result.json_data["objects"]) > len(st.session_state['points']):
		# Adicionar apenas o ponto mais recente
		last_object = canvas_result.json_data["objects"][-1]
		x = last_object["left"]
		y = last_object["top"]
		color = selected_color
		st.session_state['points'].append([x, y, color])


# Botão para limpar o dataset
if st.button("Clean Data"):
	st.session_state['points'] = []  # Limpar os pontos armazenados

# Exibir o dataset criado
if st.session_state['points']:
	st.subheader("Your Toy Data")
	df = pd.DataFrame(st.session_state['points'], columns=["X", "Y", "Color"])
	st.dataframe(df)
else:
	st.write("You don't have points yet!")
