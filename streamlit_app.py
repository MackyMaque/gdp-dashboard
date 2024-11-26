import streamlit as st

def main():
    # Set the title of the Streamlit app
    st.title("My Biography")

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

    # Display the biography in sections
    st.subheader("Full Name")
    st.markdown(f"**{full_name}**")

    st.subheader("Address")
    st.markdown(f"**{address}**")

    st.subheader("School Attended")
    st.markdown(f"**{school_attended}**")

    st.subheader("Achievements")
    st.markdown("\n".join([f"- {achievement}" for achievement in achievements]))

    st.subheader("Trainings and Seminars")
    st.markdown("\n".join([f"- {training}" for training in trainings_seminars]))

if __name__ == "__main__":
    main()

