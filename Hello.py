import streamlit as st

# Title of the app
st.title('My First Streamlit App')

# Add a text input
user_input = st.text_input('Please enter your name:', 'John Doe')

# Display the input
st.write('Hello,', user_input, '! Welcome to Streamlit!')
