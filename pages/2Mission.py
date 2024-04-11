import streamlit as st
#changing backround image. 
page_bg_img = """
<style>
[data-testid =“stAppViewContainer”] {
background-color: #e5e5f7;
opacity: 0.8;
background-image:  repeating-radial-gradient( circle at 0 0, transparent 0, #e5e5f7 10px ), repeating-linear-gradient( #f7454555, #f74545 );
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)
st.title("Mission")