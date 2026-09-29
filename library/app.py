import streamlit as st
from library_db import BookListCreateRetrieveUpdateDelete

st.title('Welcome to Library App')
b=BookListCreateRetrieveUpdateDelete()

tab1,tab2,tab3,tab4,tab5=st.tabs(['ADD','READ','RETRIEVE','UPDATE','DELETE'])

with tab1:
    st.write('ADD')
    st.title('Add New Record')
    title = st.text_input('Enter title')
    author = st.text_input('Enter author name')
    price = st.number_input('enter price', min_value=0)
    language = st.selectbox('Languages', ['English', 'Hindi', 'Malayalam'])
    pages = st.number_input('enter pages', min_value=0)
    btn = st.button('ADD')
    print(btn)
    if btn:
        b.create(title, author, price, language, pages)
        st.success('Create data successfully')

with tab2:
    st.write('READ')
    st.title('Book List')
    records = b.list()
    st.write("")
    if records:
        st.table(records)
    else:
        st.info('no records found')

with tab3:
    st.write('RETRIEVE')

with tab4:
    st.write('UPDATE')

with tab5:
    st.write('DELETE')