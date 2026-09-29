import streamlit as st

from blood_db import BloodDonation

st.title('Retrieve Data')
id=st.number_input('enter id',min_value=0)
btn=st.button('RETRIEVE')
if btn:
    b=BloodDonation()
    record=b.retrieve(id)
    if record:
        st.write('Name',record[1])
        st.write('Bloodgroup',record[2])
        st.write('Phone',record[3])
        st.write('City',record[4])
        st.write('last_donation',record[5])
    else:
        st.error('no record found')
