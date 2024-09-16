import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from models.voltage_to_capacity.predict_capacity import vol_to_cap
from models.capacity_to_rul.predict_rul import cap_to_rul
from utils.convert import month_year_converter



# SIDEBAR
icon =  'assets/icon.png'
st.sidebar.image(icon, width=300)

# Adding space between the image and the select_slider
st.sidebar.markdown("<div style='margin-top: 100px;'></div>", unsafe_allow_html=True)

# Load data
df_cap = pd.read_csv('dataset/voltage_to_capacity.csv')
df_cap['Voltage'] = df_cap['Voltage'] * 16
voltage_options = sorted(round(v, 2) for v in df_cap['Voltage'].unique().tolist())

# Input Voltage
voltage = st.sidebar.select_slider('Tegangan BMS (Volt)', options=voltage_options, value=voltage_options[-1])

# MAIN
st.subheader('PREDIKSI RUL BMS')

capacity = vol_to_cap(voltage)
rul = cap_to_rul(capacity)
    
st.write(f"Capacity = {capacity:.2f}")
st.write(f"RUL = {rul:.2f}")
st.write(f"Usia = {month_year_converter(rul / 365)}")

# Visualization
plt.figure(figsize=(10, 6))
plt.scatter(df_cap['Voltage'], df_cap['Capacity'], label='Data', alpha=0.5)
plt.scatter([voltage], [capacity], color='red', label='Input Voltage', zorder=5)
plt.title('Scatter Plot of Voltage vs Capacity')
plt.xlabel('Voltage')
plt.ylabel('Capacity')
plt.legend()
    
plt.axvline(voltage, color='red', linestyle='--', linewidth=0.5)
plt.axhline(capacity, color='red', linestyle='--', linewidth=0.5)
st.pyplot(plt)

df_rul = pd.read_csv('dataset/capacity_to_rul.csv')

plt.figure(figsize=(10, 6))
plt.scatter(df_rul['Capacity'], df_rul['RUL'], label='Data', alpha=0.5)
plt.scatter([capacity], [rul], color='red', label='Capacity', zorder=5)
plt.title('Scatter Plot of Capacity vs RUL')
plt.xlabel('Capacity')
plt.ylabel('RUL')
plt.legend()
    
plt.axvline(capacity, color='red', linestyle='--', linewidth=0.5)
plt.axhline(rul, color='red', linestyle='--', linewidth=0.5)
st.pyplot(plt)



