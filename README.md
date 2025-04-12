# Streamlit-Calculator
import streamlit as st //helps you build web apps easily.

# App Title
st.title("🧮 Simple Calculator") // for the title

# Input fields
num1 = st.number_input("Enter the first number", value=0.0, format="%.2f") // To input 1st number and format="%.2f" means show up to 2 decimal places
num2 = st.number_input("Enter the second number", value=0.0, format="%.2f") // To input 2nd number and format="%.2f" means show up to 2 decimal places

# Operation selection
operation = st.selectbox("Choose operation", ["Add", "Subtract", "Multiply", "Divide"])

# Calculate based on selected operation
if st.button("Calculate"):
    if operation == "Add":
        result = num1 + num2
        st.success(f"Result: {result:.2f}")
    elif operation == "Subtract":
        result = num1 - num2
        st.success(f"Result: {result:.2f}")
    elif operation == "Multiply":
        result = num1 * num2
        st.success(f"Result: {result:.2f}")
    elif operation == "Divide":
        if num2 != 0:
            result = num1 / num2
            st.success(f"Result: {result:.2f}")
        else:
            st.error("Error: Division by zero is not allowed.") //If the second number is zero, it shows an error message instead of crashing.
