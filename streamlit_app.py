import streamlit as st
import pandas as pd

def main():

    st.title("MAQUE, JERYLLE M.")
    st.subheader("BSCpE 1B")
    st.write("Surigao Del Norte State University")
    st.markdown('<hr>', unsafe_allow_html=True)
    st.header("Personal Information")                                                                                                                                                                 
    
    # Hardcoded biography details
    full_name = "Jerylle Morados Maque"
    address = "P4 Justiniana Edera San Jose Dinagat Islands"
    birth_date = "April 06, 2006"
    place_of_birth = "Zapote Bacoor Cavite "
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
            "Senior High",
            "College"
        ],
        "School Name": [
            "Golden Acres Elementary School",
            "Justiniana Edera Elementary School",
            "Don Ruben E Ecleo Sr. Memorial National High School",
            "Don Jose Ecleo Memorial College",
            "Surigao Del Norte State University"
        ],
        "Location": [
            "las pinas, Metro Manila",
            "Justiniana Edera San Jose PDI",
            "Don Ruben San Jose PDI",
            "Justiniana Edera San Jose",
            " Taft Surigao City Surigao Del Norte "
        ],
        "Degree/Program": [
            "Elementary Education",
            "Elementary Education",
            "Junior High School",
            "Senior High School (TVL-ICT)",
            "Bachelor of Science in Computer Engineering"
        ],
        "Year Graduated": [
            0, 2018, 2022, 2024, 0000
        ]
    }

    school_df = pd.DataFrame(school_data)

    # Display the biography in sections with left-aligned content
    st.subheader("Full Name")
    st.write(full_name)
    
    st.subheader("Home Address")
    st.write(address)

    st.subheader("Birth Date")
    st.write(birth_date)

    st.subheader("Place of Birth")
    st.write(place_of_birth)

    st.markdown('<hr>', unsafe_allow_html=True)

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
