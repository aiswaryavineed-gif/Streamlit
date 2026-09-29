import streamlit as st

#text_input()
#number_input()

#NUMBER
num1=st.number_input('enter number1',min_value=0)
num2=st.number_input('enter number2',min_value=0)
st.write(num1)
st.write(num2)

#TEXT
name=st.text_input('enter your name')
st.write(name)

#DATE
date=st.date_input('enter date')
st.write(date)


#Button function
btn=st.button('Click')
print(btn)

if btn:   # if button clicked only then it displays values of
    st.write(num1)
    st.write(num2)
    st.write(name)
    st.write(date)