import streamlit as st
import random
import pandas as pd
import numpy as np
from scipy import stats

# Título de la app
st.title("Simulación de lanzamiento de un dado")

# Simular los 20 lanzamientos
st.header("Lanzamientos")
rolls = [random.randint(1, 6) for _ in range(20)]
st.write("Resultados de los lanzamientos:")
st.write(rolls)

# Cálculo de estadísticas
mean = np.mean(rolls)
median = np.median(rolls)

# Calcular la moda con manejo de posibles errores
mode_result = stats.mode(rolls, keepdims=True)  # Usar keepdims para compatibilidad
if mode_result.count[0] > 1:  # Solo hay moda si ocurre más de una vez
    mode = mode_result.mode[0]
else:
    mode = "No hay moda única"

variance = np.var(rolls, ddof=1)
std_dev = np.std(rolls, ddof=1)

# Mostrar estadísticas
st.header("Análisis Estadístico")
st.write(f"Media: {mean:.2f}")
st.write(f"Mediana: {median}")
st.write(f"Moda: {mode}")
st.write(f"Varianza: {variance:.2f}")
st.write(f"Desviación estándar: {std_dev:.2f}")

# Análisis de frecuencias
freq_table = pd.DataFrame({
    "Número": range(1, 7),
    "Frecuencia": [rolls.count(i) for i in range(1, 7)]
})

st.header("Tabla de Frecuencias")
st.table(freq_table)
