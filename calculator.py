import streamlit as st

# App Title
st.title("🧮 Simple Calculator")

# Input fields
num1 = st.number_input("Enter the first number", value=0.0, format="%.2f")
num2 = st.number_input("Enter the second number", value=0.0, format="%.2f")

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
            st.error("Error: Division by zero is not allowed.")
