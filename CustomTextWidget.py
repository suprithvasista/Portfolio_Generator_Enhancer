import streamlit as st


# Function to render a text input with dynamic border color
def animated_text_input(label, key):
    input_value = st.text_input(label, key=key)

    # Simple validation for demonstration
    if input_value:
        if input_value.isalpha():  # Valid if only letters
            border_color = "green"
        else:
            border_color = "red"
    else:
        border_color = "gray"

    # Custom CSS for the text input
    st.markdown(
        f"""
        <style>
        input[type="text"] {{
            border: 2px solid {border_color};
            transition: border-color 2s ease;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

    return input_value


# Using the animated text input function
animated_text_input("Enter some text:", key="dynamic_input")
