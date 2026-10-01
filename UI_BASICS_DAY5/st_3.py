import Streamlit as st
import time

st.set_page_config(page_tittle="chart UI Demo")
st.tittle("chart UI Demo")

with st.chart_message("assistant"):
    st.write(f"Hello my name is Alexa ! Type something to get started.")

user_message=st.chart_input("Type Something....")
if user_message:
    with st.chart_message("user"):
        st.write("user_message")
    with st.chart_message("assistant"):
        with st.spinner("Thinking..."):
            time.sleep(1.5)
        st.write(f"you said{ user_message}.But, i am still in development. I cant reply yet.")

