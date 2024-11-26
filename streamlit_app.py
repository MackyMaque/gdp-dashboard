import streamlit as st

def main():

    st.title("My Biography")
    st.image("me.jpeg")
    # Display biography details in a blog-like format
    st.header("Biography")

    # Hardcoded biography details
    full_name = "John Doe"
    address = "123 Main Street, Springfield, USA"
    school_attended = "Springfield University"
    achievements = [
        "Graduated with Honors",
        "Employee of the Year 2020",
        "Published Research on Artificial Intelligence"
    ]
    trainings_seminars = [
        "Advanced Python Programming (2021)",
        "Machine Learning Bootcamp (2020)",
        "Leadership and Management Workshop (2019)"
    ]

    # Display the biography in sections with left-aligned content
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
