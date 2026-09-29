import streamlit as st
from blood_db import BloodDonation
st.title('Read ')

b=BloodDonation()
records=b.read()
st.write("")
if records:
    st.table(records)
else:
    st.error('no records found')