import streamlit as st
from blood_db import BloodDonation
from datetime import date

st.subheader('ADD DONOR DETAILS')


name=st.text_input('enter donor name')
bloodgroup=st.text_input('enter bloodgroup')
phone=st.number_input('enter number',min_value=0)
city=st.text_input('enter city')
last_donation=st.date_input('enter date',min_value=date(1990,1,1),max_value=date.today(),value=date(2026,1,1))
btn=st.button('CREATE')
print(btn)
if btn:
    b=BloodDonation()
    b.create(name,bloodgroup,phone,city,last_donation)
    st.success('data inserted successfully')