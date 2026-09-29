import streamlit as st

from library_db import BookListCreateRetrieveUpdateDelete

st.title('UPDATE')
id=st.number_input('enter id',min_value=0)
title=st.text_input('Enter title')
author=st.text_input('Enter author name')
price=st.number_input('enter price',min_value=0)
language=st.selectbox('Languages',['English','Hindi','Malayalam'])
pages=st.number_input('enter pages',min_value=0)
btn=st.button('UPDATE')

if btn:
    b = BookListCreateRetrieveUpdateDelete()
    record=b.update(title,author,price,language,pages,id)
    print(record)
    if record:
        st.success('Data Updated')
    else:
        st.error('No record found')

