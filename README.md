# Aplicación Web de Análisis de Vehículos en Venta (USA)

Esta aplicación web fue construida con Streamlit, permite visualizar de manera interactiva datos sobre vehículos en venta en EE.UU. Utiliza gráficas interactivas generadas con Plotly.

## Funcionalidades:

- Visualización de un histograma según la preferencia del usuario. Las opciones pueden ser: odometer, price, model_year y days_listed.
- Visualización de un gráfico de dispersión según sus preferencias a comparar. Puede comparar entre cualquier variable como odometer, price, model_year y days_listed. Solo tiene que específicar que dato quiere visualizar en cada eje. 

## Requisitos

- Python
- streamlit
- pandas
- plotly

## Cómo ejecutarlo

streamlit run app.py