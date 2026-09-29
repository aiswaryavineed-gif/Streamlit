import streamlit as st

from library_db import BookListCreateRetrieveUpdateDelete

st.title('DELETE')
id=st.number_input('enter id',min_value=0)
btn=st.button('DELETE')
if btn:
    b = BookListCreateRetrieveUpdateDelete()
    record=b.delete(id)
    print(record)
    if record:
        st.success('True')
    else:
        st.error('False')