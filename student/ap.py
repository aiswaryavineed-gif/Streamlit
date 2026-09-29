import streamlit as st
from datetime import date
st.title('Student Registration Form')
name=st.text_input('Enter student name')
age=st.number_input('Enter age',min_value=-0)
DOB=st.date_input('Enter DOB',min_value=date(1990,1,1),
                  max_value=date.today(),value=date(2006,1,1))
email=st.text_input('Enter email')
Gender=st.radio('Gender',['male','female'])
courses=st.selectbox('courses',['Python','dotnet','testing'])
btn=st.button('SUBMIT')
print(btn)
if btn:
    st.write(name)
    st.write(age)
    st.write(DOB)
    st.write(email)
    st.write(Gender)
    st.write(courses)
