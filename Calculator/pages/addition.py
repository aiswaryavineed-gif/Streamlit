import streamlit as st
num1=st.number_input('Enter number1',min_value=0)
num2=st.number_input('Enter number2',min_value=0)
sum=num1+num2

btn=st.button('ADD')
print(btn)
if btn:
    # st.write(num1)
    # st.write(num2)
    st.write("sum is ",sum)