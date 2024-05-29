import streamlit as st
from st_pages import Page, _hide_pages, show_pages
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(page_title="SAR App", layout='wide')

show_pages(
    [
        Page('main.py', 'SAR', icon="🎥"),
        Page('pages/diego.py', 'DIEGO', icon='10' )
            ]
)

# oculto la pagina de resultados del modelo que se activa unicamente cuando el usuario completa el form
_hide_pages(["DIEGO"])


left_1, cent_co,right_2 = st.columns(3)
with cent_co:
    st.markdown("<h1 style='text-align: center; font-size: 60px;'>SAR.</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center; font-size: 20px;'>Find the next masterpiece.</h1>", unsafe_allow_html=True)
    st.write('---')


movie_script = st.text_input('Enter your movie script and unveil the magic')
button = st.button('Try SAR')

if movie_script and button:
    switch_page('DIEGO')
