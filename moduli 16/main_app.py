import streamlit as st

if st.button("Click Me"):
    st.write("Cliked")

if st.checkbox("Check me to show some text"):
   st.write("You're seeing this text ")

user_input = st.text_input("Enter a text", "Sample text")
st.write("You entered", user_input)

age = st.number_input("Enter your age", min_value = 0, max_value = 100)
st.write(f"Your age is : {age}")

message = st.text_area("Enter a message")
st.write(f"Your message: {message}")

choice = st.radio("Pick one ", ["Html","Css", "JavaScript"] )
st.write(f"You choose: {choice}")


if st.button("success"):
    st.success("Operation was succsesfull")