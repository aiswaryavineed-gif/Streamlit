import streamlit as st

from blood_db import BloodDonation
from datetime import date

st.title('Update Data')
id=st.number_input('enter id',min_value=0)
name=st.text_input('enter donor name')
bloodgroup=st.text_input('enter bloodgroup')
phone=st.number_input('enter number',min_value=0)
city=st.text_input('enter city')
last_donation=st.date_input('enter date',min_value=date(1990,1,1),max_value=date.today(),value=date(2026,1,1))
btn=st.button('UPDATE')
print(btn)
if btn:
    b=BloodDonation()
    record=b.update(name,bloodgroup,phone,city,last_donation,id)
    if record:
        st.success('update data successfully')
    else:
        st.error('no records found')
