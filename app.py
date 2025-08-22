# -*- coding: utf-8 -*-
"""
Created on Fri Aug 22 14:05:13 2025

@author: jahop
"""

import streamlit as st
import pandas as pd
import numpy as np
import datetime
from datetime import time
import plotly.express as px

# Configuración de la página
st.set_page_config(
    page_title="Sistema Gerente de Operaciones - Transporte de Personal",
    page_icon="🚌",
    layout="wide"
)

# Título principal
st.title("🚌 Sistema de Gestión para Gerente de Operaciones")
st.subheader("Transporte de Personal - Apodaca, N.L.")

# Barra lateral con información de la vacante
with st.sidebar:
    st.header("Creado por: Javier Horacio Pérez Ricárdez")
    st.subheader("Información de la Vacante")
    st.write("**Posición:** Gerente de Operaciones")
    st.write("**Modalidad:** Tiempo completo, presencial")
    st.write("**Ubicación:** Apodaca, Nuevo León")
    
    st.divider()
    
    st.subheader("Requisitos")
    st.write("• Experiencia en transporte de personal (Indispensable)")
    st.write("• Capacidad analítica sólida")
    st.write("• Gestión de operaciones y liderazgo")
    st.write("• Administración de proyectos")
    st.write("• Buenas habilidades de comunicación")
    
    st.divider()
    
    st.info("Esta herramienta apoya las funciones clave del Gerente de Operaciones")

# Pestañas para las diferentes funciones
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📊 Dashboard Principal", 
    "🛣️ Planificación de Rutas", 
    "🚗 Gestión de Flotas", 
    "👥 Supervisión de Personal", 
    "⚙️ Resolución de Problemas"
])

with tab1:
    st.header("Dashboard de Operaciones")
    
    # Métricas clave
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Vehículos Operando", "42", "3")
    with col2:
        st.metric("Rutas Activas", "28", "2")
    with col3:
        st.metric("Personal Transportado", "1,250", "45")
    with col4:
        st.metric("Puntualidad", "92%", "-2%")
    
    # Gráficos de ejemplo
    col_chart1, col_chart2 = st.columns(2)
    
    with col_chart1:
        # Datos de ejemplo para gráfico de rutas
        data_rutas = pd.DataFrame({
            'Ruta': ['Ruta A', 'Ruta B', 'Ruta C', 'Ruta D', 'Ruta E'],
            'Tiempo promedio (min)': [45, 52, 38, 60, 42],
            'Pasajeros': [50, 45, 60, 35, 55]
        })
        fig = px.bar(data_rutas, x='Ruta', y='Tiempo promedio (min)', 
                     title='Tiempo Promedio por Ruta')
        st.plotly_chart(fig, use_container_width=True)
    
    with col_chart2:
        # Datos de ejemplo para gráfico de estado de flota
        data_flota = pd.DataFrame({
            'Estado': ['Operativo', 'Mantenimiento', 'Reserva', 'Inactivo'],
            'Cantidad': [32, 5, 3, 2]
        })
        fig = px.pie(data_flota, values='Cantidad', names='Estado', 
                     title='Estado de la Flota')
        st.plotly_chart(fig, use_container_width=True)
    
    # Alertas y notificaciones
    st.subheader("Alertas y Acciones Prioritarias")
    st.warning("⚠️ 2 vehículos requieren mantenimiento urgente")
    st.info("ℹ️ 3 conductores necesitan renovación de documentación")
    st.success("✅ Reunión programada con equipo de logística a las 11:00 AM")

with tab2:
    st.header("Planificación de Rutas")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Mapa de ejemplo (simulado con texto)
        st.subheader("Mapa de Rutas")
        st.image("https://via.placeholder.com/600x400/4F46E5/FFFFFF?text=Mapa+de+Rutas+de+Transporte", 
                 use_column_width=True)
        
        # Lista de rutas
        st.subheader("Rutas Programadas")
        rutas_data = pd.DataFrame({
            'Ruta': ['Corporativo', 'Industrial', 'Residencial', 'Mixta'],
            'Horario Salida': ['06:30', '07:15', '06:45', '07:00'],
            'Horario Regreso': ['17:30', '18:15', '18:45', '19:00'],
            'Pasajeros': [45, 52, 38, 42]
        })
        st.dataframe(rutas_data, use_container_width=True)
    
    with col2:
        st.subheader("Nueva Ruta")
        with st.form("nueva_ruta"):
            nombre_ruta = st.text_input("Nombre de la ruta")
            origen = st.text_input("Origen")
            destino = st.text_input("Destino")
            horario_salida = st.time_input("Horario de salida", time(7, 0))
            horario_regreso = st.time_input("Horario de regreso", time(17, 0))
            capacidad = st.slider("Capacidad estimada", 10, 60, 30)
            
            submitted = st.form_submit_button("Programar Ruta")
            if submitted:
                st.success(f"Ruta '{nombre_ruta}' programada correctamente")

with tab3:
    st.header("Gestión de Flotas")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Vehículos en Operación")
        # Datos de ejemplo para vehículos
        vehiculos_data = pd.DataFrame({
            'Vehículo': ['VAN-001', 'VAN-002', 'BUS-001', 'BUS-002', 'VAN-003'],
            'Modelo': [2022, 2021, 2020, 2022, 2021],
            'Capacidad': [15, 15, 40, 40, 15],
            'Kilometraje': [45230, 58760, 82340, 25670, 43210],
            'Estado': ['Operativo', 'Mantenimiento', 'Operativo', 'Operativo', 'Reserva']
        })
        st.dataframe(vehiculos_data, use_container_width=True)
    
    with col2:
        st.subheader("Registro de Mantenimiento")
        with st.form("registro_mantenimiento"):
            vehiculo = st.selectbox("Vehículo", ['VAN-001', 'VAN-002', 'BUS-001', 'BUS-002', 'VAN-003'])
            tipo_mantenimiento = st.selectbox("Tipo de mantenimiento", 
                                            ["Preventivo", "Correctivo", "Revision"])
            fecha = st.date_input("Fecha programada")
            observaciones = st.text_area("Observaciones")
            
            submitted = st.form_submit_button("Programar Mantenimiento")
            if submitted:
                st.success(f"Mantenimiento para {vehiculo} programado correctamente")
    
    st.subheader("Control de Combustible")
    col_comb1, col_comb2, col_comb3 = st.columns(3)
    with col_comb1:
        st.metric("Consumo Mensual (Lts)", "2,850")
    with col_comb2:
        st.metric("Costo Mensual", "$85,500 MXN")
    with col_comb3:
        st.metric("Rendimiento Promedio", "7.2 km/lt")

with tab4:
    st.header("Supervisión de Personal")
    
    st.subheader("Equipo de Conductores")
    # Datos de ejemplo para conductores
    conductores_data = pd.DataFrame({
        'Nombre': ['Juan Pérez', 'María García', 'Carlos López', 'Ana Martínez'],
        'Ruta Asignada': ['Corporativo', 'Industrial', 'Residencial', 'Mixta'],
        'Horario': ['06:30-17:30', '07:15-18:15', '06:45-18:45', '07:00-19:00'],
        'Antigüedad': ['2 años', '3 años', '1 año', '4 años'],
        'Evaluación': [4.8, 4.5, 4.2, 4.9]
    })
    st.dataframe(conductores_data, use_container_width=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Registro de Incidencias")
        with st.form("registro_incidencia"):
            conductor = st.selectbox("Conductor", conductores_data['Nombre'].tolist())
            tipo_incidencia = st.selectbox("Tipo de incidencia", 
                                         ["Retraso", "Falta", "Vehicular", "Otro"])
            fecha_incidencia = st.date_input("Fecha de incidencia")
            descripcion = st.text_area("Descripción")
            
            submitted = st.form_submit_button("Registrar Incidencia")
            if submitted:
                st.success("Incidencia registrada correctamente")
    
    with col2:
        st.subheader("Desempeño del Equipo")
        # Gráfico de ejemplo para evaluaciones
        fig = px.bar(conductores_data, x='Nombre', y='Evaluación', 
                     title='Evaluación de Conductores (0-5)')
        st.plotly_chart(fig, use_container_width=True)

with tab5:
    st.header("Resolución de Problemas Operativos")
    
    st.subheader("Problemas Reportados")
    # Datos de ejemplo para problemas
    problemas_data = pd.DataFrame({
        'Fecha': ['2023-05-10', '2023-05-09', '2023-05-08', '2023-05-07'],
        'Problema': ['Retraso en ruta corporativa', 'Vehículo con falla mecánica', 
                    'Falta de conductor', 'Aumento de pasajeros en ruta industrial'],
        'Prioridad': ['Alta', 'Alta', 'Media', 'Baja'],
        'Estado': ['Resuelto', 'En proceso', 'Pendiente', 'Pendiente']
    })
    st.dataframe(problemas_data, use_container_width=True)
    
    st.subheader("Reportar Nuevo Problema")
    with st.form("nuevo_problema"):
        col1, col2 = st.columns(2)
        with col1:
            problema = st.text_input("Problema")
            fecha_reporte = st.date_input("Fecha de reporte")
        with col2:
            prioridad = st.selectbox("Prioridad", ["Alta", "Media", "Baja"])
            tipo_problema = st.selectbox("Tipo de problema", 
                                       ["Rutas", "Vehículos", "Personal", "Pasajeros", "Otro"])
        
        descripcion = st.text_area("Descripción detallada")
        
        submitted = st.form_submit_button("Reportar Problema")
        if submitted:
            st.success("Problema reportado correctamente")
    
    st.subheader("Seguimiento de Soluciones")
    with st.expander("Ver soluciones implementadas"):
        st.write("""
        - **Retrasos en rutas**: Implementado sistema de monitoreo en tiempo real
        - **Fallas mecánicas**: Establecido programa de mantenimiento preventivo
        - **Falta de personal**: Creación de banco de conductores de reserva
        """)

# Pie de página
st.divider()
st.caption("Sistema de gestión para Gerente de Operaciones - Transporte de Personal | Apodaca, N.L.")