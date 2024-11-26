import streamlit as st

def main():
    # Set the title of the Streamlit app
    st.title("My Biography")

    # Introduction section
    st.header("Introduction")
    st.write("Welcome to my biography app! Please fill in your details below.")

    # Input fields for user to provide their biography details
    name = st.text_input("What is your name?", "")
    age = st.number_input("How old are you?", min_value=0, max_value=150, step=1, value=0)
    profession = st.text_input("What is your profession?", "")
    hobbies = st.text_area("What are your hobbies?", "")
    additional_info = st.text_area("Additional Information", "")

    # Display biography details when user clicks the button
    if st.button("Show My Biography"):
        st.subheader("Biography")
        if name:
            st.write(f"**Name:** {name}")
        if age > 0:
            st.write(f"**Age:** {age}")
        if profession:
            st.write(f"**Profession:** {profession}")
        if hobbies:
            st.write(f"**Hobbies:** {hobbies}")
        if additional_info:
            st.write(f"**Additional Information:** {additional_info}")

if __name__ == "__main__":
    main()







