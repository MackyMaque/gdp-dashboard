import streamlit as st
from PIL import Image

def display_title(app_title, subtitle):
    
    st.markdown(f"""
        <div style="text-align: center; margin-bottom: 20px;">
            <h1 style="color: #4CAF50; font-size: 3em; margin-bottom: 0;">{app_title}</h1>
            <h3 style="color: #6c757d; margin-top: 5px;">{subtitle}</h3>
        </div>
    """, unsafe_allow_html=True)


st.set_page_config(page_title="Title Template Example", layout="centered")

display_title("MAQUE, JERYLLE ", "BSCpE-1B")

st.set_page_config(page_title="Picture Uploader", layout="centered")

st.title("Upload Your Picture")

# File uploader widget
uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Open and display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)
    st.success("Image uploaded successfully!")
else:
    st.info("Please upload an image file to see it displayed here.")
