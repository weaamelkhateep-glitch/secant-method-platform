import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Secant Method Platform", layout="centered")
st.title("🔹 Secant Method Platform")

func_str = st.text_input("f(x):", "x**3 - x - 2")
x0 = st.number_input("x0:", value=0.0)
x1 = st.number_input("x1:", value=2.0)
tol = st.number_input("Tolerance:", value=1e-6)

if st.button("Calculate"):
    try:
        def f(x):
            return eval(func_str)
        
        max_iter = 100
        for i in range(max_iter):
            if f(x1) - f(x0) == 0:
                st.error("⚠ Division by zero!")
                break
            x2 = x1 - f(x1)*(x1 - x0)/(f(x1) - f(x0))
            if abs(x2 - x1) < tol:
                root = x2
                iterations = i+1
                break
            x0, x1 = x1, x2
        else:
            root = x2
            iterations = max_iter

        st.success(f"Root ≈ {root}\nIterations = {iterations}")

        x_vals = np.linspace(root-5, root+5, 400)
        y_vals = [f(x) for x in x_vals]
        plt.figure(figsize=(7,4))
        plt.plot(x_vals, y_vals, label="f(x)")
        plt.axhline(0, color='black', linewidth=0.8)
        plt.axvline(root, color='red', linestyle='--', label=f'Root ≈ {root:.6f}')
        plt.legend()
        plt.grid(True)
        st.pyplot(plt)
        
    except Exception as e:
        st.error(f"Invalid input: {e}")
