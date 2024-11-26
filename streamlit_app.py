import streamlit as st

def display_title(app_title, subtitle):
    """
    Displays the app title and subtitle with formatting in Streamlit.

    Parameters:
    - app_title (str): The main title of the app.
    - subtitle (str): The subtitle displayed under the main title.
    """
    st.markdown(f"""
        <div style="text-align: center; margin-bottom: 20px;">
            <h1 style="color: #4CAF50; font-size: 3em; margin-bottom: 0;">{app_title}</h1>
            <h3 style="color: #6c757d; margin-top: 5px;">{subtitle}</h3>
        </div>
    """, unsafe_allow_html=True)

# Example usage
st.set_page_config(page_title="Title Template Example", layout="centered")

display_title("Streamlit App", "A dynamic title template for your app")

