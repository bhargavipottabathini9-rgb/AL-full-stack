import streamlit as st

st.set_page_config(page_tittle="Text Input Demo", page_icon="".)
st.tittle("Text Input Demo")
st.markdown("""
<style>
.stApp{
background-colour : #5D100A}
</style>
""",unsafe_allow_html=True)

name=st.text_input("Enter your name:",placeholder="e.g. Bhargavi")
st.write(f"Hi,{name}!")

secret = st.Text_input("Enter your password:",type="password")
st.write(f"You entered{len(secret)} characters.")

comments=st.text_area("Enter additional comments:",height=150)
st.write(f"You entered {len(comments)} characters")

if st.button("submit"):
    st.write("You clicked me!")

if st.checkbox("Show Additional msg?"):
    st.write("This is the additional message. Have a god day!")