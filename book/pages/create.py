import streamlit as st

from library_db import BookListCreateRetrieveUpdateDelete

st.title('Add New Record')
title=st.text_input('Enter title')
author=st.text_input('Enter author name')
price=st.number_input('enter price',min_value=0)
language=st.selectbox('Languages',['English','Hindi','Malayalam'])
pages=st.number_input('enter pages',min_value=0)
btn=st.button('ADD')
print(btn)
if btn:
    b=BookListCreateRetrieveUpdateDelete()
    b.create(title,author,price,language,pages)
    st.success('Create data successfully')
