import streamlit as st
from st_pages import Page, _hide_pages, show_pages


left_1, cent_co,right_2 = st.columns(3)
with cent_co:
    st.markdown("<h1 style='text-align: center; font-size: 25px;'>Aprobado por el Diego</h1>", unsafe_allow_html=True)
    st.image('diego.jpg')