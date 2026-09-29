import streamlit as st

from blood_db import BloodDonation

st.title('DELETE')
id=st.number_input('enter id',min_value=0)
btn=st.button('DELETE')
print(btn)
if btn:
    b=BloodDonation()
    record=b.delete(id)
    if record:
        st.success('True')
    else:
        st.error('False')