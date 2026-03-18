import streamlit as st
import numpy as np
import pandas as pd

st.set_page_config(page_title="Secant Method Platform", layout="centered")
st.title("🔍 Secant Method Platform")

# User inputs
func_str = st.text_input("f(x): ", "x**3 - x - 2")
x0 = st.number_input("x0:", value=0.0, format="%.2f")
x1 = st.number_input("x1:", value=2.0, format="%.2f")
tol = st.number_input("Tolerance:", value=1e-6, format="%.1e")

if st.button("Calculate"):
    try:
        def f(x):
            return eval(func_str, {"x": x, "np": np})
        
        st.write("---")
        st.subheader("📊 Iteration Steps")
        
        # Create table headers
        col1, col2, col3, col4 = st.columns(4)
        col1.write("**Iteration**")
        col2.write("**x_n**")
        col3.write("**x_{n+1}**")
        col4.write("**f(x_{n+1})**")
        
        max_iter = 100
        iterations_data = []
        
        for i in range(max_iter):
            f_x0 = f(x0)
            f_x1 = f(x1)
            
            if abs(f_x1 - f_x0) < 1e-12:
                st.error("⚠️ Division by zero! The method failed.")
                break
            
            x2 = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)
            f_x2 = f(x2)
            
            # Save data for table and chart
            iterations_data.append({
                "Iteration": i+1,
                "x_n": x1,
                "x_{n+1}": x2,
                "f(x)": f_x2
            })
            
            # Display step
            col1, col2, col3, col4 = st.columns(4)
            col1.write(f"{i+1}")
            col2.write(f"{x1:.6f}")
            col3.write(f"{x2:.6f}")
            col4.write(f"{f_x2:.2e}")
            
            if abs(x2 - x1) < tol:
                st.success(f"✅ **Root found: x = {x2:.10f}**")
                st.write(f"f(x) = {f_x2:.2e}")
                break
            else:
                x0, x1 = x1, x2
        else:
            st.warning("⚠️ Maximum iterations reached without convergence.")
        
        # Display chart using Streamlit native line chart
        if iterations_data:
            st.subheader("📈 Convergence Chart")
            df = pd.DataFrame(iterations_data)
            
            # Show the chart
            st.line_chart(df.set_index("Iteration")[["x_n", "x_{n+1}"]])
            
            # Also show the data table
            with st.expander("📋 Show detailed data table"):
                st.dataframe(df)
            
    except Exception as e:
        st.error(f"❌ Error: {e}")
