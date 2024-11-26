import streamlit as st


def display_title(app_title, subtitle):
    
    st.markdown(f"""
        <div style="text-align: center; margin-bottom: 20px;">
            <h1 style="color: #4CAF50; font-size: 3em; margin-bottom: 0;">{app_title}</h1>
            <h3 style="color: #6c757d; margin-top: 5px;">{subtitle}</h3>
        </div>
    """, unsafe_allow_html=True)


st.set_page_config(page_title="Title Template Example", layout="centered")

display_title("MAQUE, JERYLLE ", "BSCpE-1B")

st.image("/home/eb204-u7/Pictures/h.png", caption="This is my picture.")







