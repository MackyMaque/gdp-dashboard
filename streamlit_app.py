import streamlit as st

def main():

    st.title("MAQUE, JERYLLE M. ")
    st.header("BSCpE -1B ")
    st.write("Surigao Del Norte State University")
    st.write("")
    st.markdown('<hr>', unsafe_allow_html=True)
    # Display biography details in a blog-like format
    st.header("Biography")
    
   

    # Display the biography in sections with left-aligned content
    st.subheader("Full Name")
    st.write(full_name)
    st.subheader("Full Name")
    st.write(full_name)

    st.subheader("Address")
    st.write(address)

    st.subheader("School Attended")
    st.write(school_attended)

    st.subheader("Achievements")
    for achievement in achievements:
        st.write(f"- {achievement}")

    st.subheader("Trainings and Seminars")
    for training in trainings_seminars:
        st.write(f"- {training}")

if __name__ == "__main__":
    main()



