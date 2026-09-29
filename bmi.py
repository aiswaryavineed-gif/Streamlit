import streamlit as st
weight=st.number_input('Enter weight in kg',min_value=0)
height=st.number_input('Enter height in cm',min_value=0)
#BMI=weight /((height/100)**2)
btn=st.button('bmi')
print(btn)
if btn:
    BMI = weight / ((height / 100) ** 2)
    st.write('BMI is',BMI)
    if BMI<18.5:
        st.info('underweight')
    elif 18.5<=BMI<25:
        st.success('normal')
    elif 25<=BMI<30:
        st.warning('overweight')
    else:
        st.error('obesity')