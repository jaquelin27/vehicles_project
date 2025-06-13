import pandas as pd
import streamlit as st
import plotly.express as px

car_data = pd.read_csv('vehicles_us.csv')  # leer los datos

st.header('Análisis de vehículos en venta (USA)')

# Histograma:
st.subheader('Histograma interactivo')
# Selección de la columna a graficar en histograma
column_option = st.selectbox(
    'Selecciona una opción para crear el histograma:',
    options=['odometer', 'price', 'model_year', 'days_listed']
)

hist_button = st.button('Construir histograma')  # crear un botón

if hist_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(f'Histograma para la opción: **{column_option}**')

    # crear un histograma para la opción elegida
    fig = px.histogram(car_data, x=column_option)

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

# Gráfico de dispersión:
st.subheader('Gráfico de dispersión interactivo')

# Opciones de ejes para el gráfico:
x_axis = st.selectbox('Selecciona el eje X:', options=[
                      'odometer', 'price', 'model_year', 'days_listed'], key='x')
y_axis = st.selectbox('Selecciona el eje Y:', options=[
                      'odometer', 'price', 'model_year', 'days_listed'], key='y')

scatter_button = st.button('Construir gráfico de dispersión')  # crear botón

if scatter_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(f'Gráfico de dispersión entre **{x_axis}** vs. **{y_axis}**')

    # crear gráfico de dispersión
    fig2 = px.scatter(car_data, x=x_axis, y=y_axis)

    # mostrar el gráfico de dispersión
    st.plotly_chart(fig2, use_container_width=True)
