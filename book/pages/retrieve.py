import streamlit as st

from library_db import BookListCreateRetrieveUpdateDelete

st.title('RETRIEVE')
id=st.number_input('enter id',min_value=0)
btn=st.button('RETRIEVE')
if btn:
    b = BookListCreateRetrieveUpdateDelete()
    record=b.retrieve(id)
    print(record)
    if record:
        st.write("Title",record[1])
        st.write("Author",record[2])
        st.write("Price",record[3])
        st.write("Language",record[4])
        st.write("Pages",record[5])

    else:
        st.error('no record found')