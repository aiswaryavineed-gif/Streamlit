import streamlit as st
num1=st.number_input('Enter number1',min_value=0)
num2=st.number_input('Enter number2',min_value=0)
s=num1*num2

btn=st.button('MUL')
print(btn)
if btn:
    # st.write(num1)
    # st.write(num2)
    st.write("product is ",s)