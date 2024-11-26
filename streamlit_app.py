import streamlit as st
import pandas as pd

def main():
    # Image URL
    image_url = 'https://3863c30cf6.cbaul-cdnwnd.com/84666889e4c11d1601e4759f497cf43b/200000009-c5d6bc5d6d/1000046473.webp?ph=3863c30cf6'
    
    # Display the image with custom styling (making it larger and circular)
    st.markdown(
        """
        <style>
        .circle-img {
            width: 150px;  /* Adjust the image size */
            height: 150px; /* Adjust the image size */
            border-radius: 50%;
            object-fit: cover;
        }
        </style>
        """, unsafe_allow_html=True)
    
    # Display the image using the custom style class
    st.markdown(f'<img src="{image_url}" class="circle-img">', unsafe_allow_html=True)

    # Title and other sections
    st.title("MAQUE, JERYLLE M.")
    st.subheader("BSCpE 1B")
    st.write("Surigao Del Norte State University")
    st.write("Activity In Programming Logic and Design")
    st.markdown('<hr>', unsafe_allow_html=True)
    st.header("Personal Information")                                                                                                                                                                 
    
    # Hardcoded biography details
    full_name = "Jerylle Morados Maque"
    address = "P4 Justiniana Edera San Jose Dinagat Islands"
    birth_date = "April 06, 2006"
    place_of_birth = "Zapote Bacoor Cavite "
    achievements = [
        "Graduated with Honors on TVL ICT STRAND in SHS at DJEMC "
       
    ]
    trainings_seminars = [
        "Seminar on Theoretical Driving Course and Defensive driving",
        "Work Immersion / On The Job Training",
    
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
            "Las Pinas, Metro Manila",
            "Justiniana Edera, San Jose PDI",
            "Don Ruben, San Jose PDI",
            "Justiniana Edera, San Jose",
            "Taft, Surigao City, Surigao Del Norte"
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
    st.markdown('<hr>', unsafe_allow_html=True)
    st.subheader("Achievements")
    for achievement in achievements:
        st.write(f"- {achievement}")

    st.subheader("Trainings and Seminars")
    for training in trainings_seminars:
      st.write(f"- {training}")
    st.markdown('<hr>', unsafe_allow_html=True)

    st.title("Trainings and Seminars")
    
    st.header("Seminar on Theoretical Driving Course and Defensive driving")
    st.write("Date.       : July 20, 2024")
    st.write("Venue     : Don Ruben Gymnasium San jose Dinagat Islands")
    st.write("Speaker  :  LTO, Maam Marife Gambe Head, Traffic Safety Unit ")
    st.write("Number of Hours : 8 Hours")
    image_url = 'https://scontent.fcgy2-4.fna.fbcdn.net/v/t1.15752-9/462561930_1786046622221725_1031899513280745191_n.jpg?_nc_cat=110&ccb=1-7&_nc_sid=9f807c&_nc_eui2=AeHDD5b2JJvY3ImsnhEts3l4XFLo_zRnlv5cUuj_NGeW_l0rCA6lQgcrnt3X97pGcarrDEcADDivRDUWvQOeavUD&_nc_ohc=tllPn-pVDLMQ7kNvgGaXwEe&_nc_zt=23&_nc_ht=scontent.fcgy2-4.fna&oh=03_Q7cD1QFko6KA9Cl3Yqr8QdZZtClMVtIKpRtRD9QJQNnIAupYGA&oe=676CF9CE'
    st.image(image_url, caption='Actual Pic')
    st.markdown('<hr>', unsafe_allow_html=True)
    st.header("Work Immersion / On The Job Training")
    st.write("Work site: Provincial capitol/Provincial Governor's Office")
    st.write("Number of  Hours : 80 hours or 10 days")
    st.write("Date:           May ,2024")

    image_url = 'https://3863c30cf6.cbaul-cdnwnd.com/84666889e4c11d1601e4759f497cf43b/200000013-7391073912/1000048674.webp?ph=3863c30cf6'
    st.image(image_url, caption='Picture of Certificate')
    
        
    
if __name__ == "__main__":
    main()


