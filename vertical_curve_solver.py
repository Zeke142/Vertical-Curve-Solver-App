import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(page_title="Vertical Curve Solver", layout="centered")
st.title("Vertical Curve Solver")

with st.form("curve_form"):
    st.subheader("Input Vertical Curve Parameters")

    x_pvi = st.number_input("Station of PVI (ft or m)", value=1000.0)
    y_pvi = st.number_input("Elevation at PVI", value=500.0)
    g1 = st.number_input("Initial Grade (in decimal, e.g., 0.03 for 3%)", value=0.03)
    g2 = st.number_input("Final Grade (in decimal)", value=-0.02)
    L = st.number_input("Length of Vertical Curve", value=200.0)
    x = st.number_input("Station to Evaluate", value=1025.0)
    show_plot = st.checkbox("Show Elevation Plot")

    submitted = st.form_submit_button("Calculate")

if submitted:
    A = g2 - g1
    dx = x - x_pvi
    y = y_pvi + g1 * dx + (A * dx**2) / (2 * L)

    st.success(f"Elevation at station {x} is **{y:.3f}**")

    if show_plot:
        st.subheader("Curve Profile")
        x_vals = np.linspace(x_pvi - L/2, x_pvi + L/2, 100)
        y_vals = y_pvi + g1*(x_vals - x_pvi) + (A/2)*((x_vals - x_pvi)**2) / L

        fig, ax = plt.subplots()
        ax.plot(x_vals, y_vals, label="Vertical Curve")
        ax.axvline(x, color='red', linestyle='--', label=f"Station {x}")
        ax.plot(x, y, 'ro')
        ax.set_xlabel("Station")
        ax.set_ylabel("Elevation")
        ax.legend()
        ax.grid(True)
        st.pyplot(fig)
