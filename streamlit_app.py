import streamlit as st

def main():
    # Set the title of the Streamlit app
    st.title("My Biography")

    # Display biography details
    st.header("Biography")

    # Hardcoded biography details
    name = "John Doe"
    age = 30
    profession = "Software Developer"
    hobbies = "Reading, Hiking, and Coding"
    additional_info = "Passionate about technology and education."

    # Display the biography
    st.write(f"**Name:** {name}")
    st.write(f"**Age:** {age}")
    st.write(f"**Profession:** {profession}")
    st.write(f"**Hobbies:** {hobbies}")
    st.write(f"**Additional Information:** {additional_info}")

if __name__ == "__main__":
    main()
