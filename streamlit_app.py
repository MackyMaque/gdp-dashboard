import streamlit as st
import pandas as pd

def main():

    st.title("MAQUE, JERYLLE M.")
    st.subheader("BSCpE 1B")
    st.write("Surigao Del Norte State University")
    st.markdown('<hr>', unsafe_allow_html=True)
    st.header("Personal information")                                                                                                                                                                 
    
    # Hardcoded biography details
    full_name = "Jerylle Morados Maque"
    address = "P4 Justiniana Edera San Jose Dinagat Islands"
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

    # Data for the school attended table (organized by educational level)
    school_data = {
        "Educational Level": [
            "Elementary",
            "Elementary",
            "Junior High",
            "Junior High",
            "Senior High",
            "Senior High",
            "College"
        ],
        "School Name": [
            "Sunrise Primary School",
            "Green Valley Elementary",
            "Oceanview Junior High",
            "Mountain Peak Junior High",
            "Riverdale Senior High",
            "Sunshine Senior High",
            "Springfield University"
        ],
        "Location": [
            "Sunrise, USA",
            "Green Valley, USA",
            "Oceanview, USA",
            "Mountain Peak, USA",
            "Riverdale, USA",
            "Sunshine, USA",
            "Springfield, USA"
        ],
        "Degree/Program": [
            "Elementary Education",
            "Elementary Education",
            "Junior High School",
            "Junior High School",
            "Senior High School (STEM)",
            "Senior High School (ABM)",
            "Bachelor of Science in Computer Engineering"
        ],
        "Year Graduated": [
            2011, 2012, 2016, 2017, 2019, 2020, 2023
        ]
    }

    school_df = pd.DataFrame(school_data)

    # Display the biography in sections with left-aligned content
    st.subheader("Full Name")
    st.write(full_name)

    st.subheader("Home Address")
    st.write(address)

    st.subheader("School Attended")
    st.table(school_df)  # Display the school table

    st.subheader("Achievements")
    for achievement in achievements:
        st.write(f"- {achievement}")

    st.subheader("Trainings and Seminars")
    for training in trainings_seminars:
        st.write(f"- {training}")

if __name__ == "__main__":
    main()
