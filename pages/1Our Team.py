import streamlit as st


st.title("Meet our Team")
base = "dark"

#Spencer Bertsch
#PhD Candiate, Operations Research, Computer Science

def main():

    team_members = [
        {
            "name": "Vikrant Vaze",
            "title": "Stata Family Career Development Associate Professor of Engineering and Faculty Director, Master of Engineering Management Program, Program Area Lead: Mechanical, Operations & Systems Engineering",
            "photo_url": "https://drive.google.com/uc?id=1jsSNzUzS56XuC0y5AOORIRAqF2QR4Dmg",
        },
        {
            "name": "Spencer Bertsch",
            "title": "Lead Reseacher, PhD Candiate, Operations Research, Computer Science",
            "photo_url": "https://drive.google.com/uc?id=1jsSNzUzS56XuC0y5AOORIRAqF2QR4Dmg",
        },
        {
            "name": "Michal Demeter",
            "title": "Software Engineer",
            "photo_url": "https://example.com/alice_johnson.jpg",
        },
        {
            "name": "Gary Ding",
            "title": "Developer",
            "photo_url": "https://example.com/spencer.jpg",
        },
        {
            "name": "Daisy Granholm",
            "title": "Designer",
            "photo_url": "https://example.com/daisy.jpg",
        },
        {
            "name": "Nathalie Taylor",
            "title": "Marketing Manager",
            "photo_url": "https://example.com/chloe.jpg",
        }
    ]

    # Define CSS style for the grid layout
    st.markdown(
        """
        <style>
        .grid-container {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            grid-gap: 20px;
        }
        .profile-card {
            display: flex;
            align-items: center;
            padding: 20px;
            border: 1px solid #ddd;
            border-radius: 5px;
        }
        .profile-img {
            width: 100px;
            height: 100px;
            border-radius: 50%;
            margin-right: 20px;
        }
        .profile-details {
            flex-grow: 1;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Display the grid container for profile cards
    st.markdown("<div class='grid-container'>", unsafe_allow_html=True)

    # Define the specific order of team members for the grid layout
    order = ["Vikrant Vaze", "Spencer Bertsch", "Michal Demeter", "Gary Ding", "Daisy Granholm", "Nathalie Taylor"]

    for name in order:
        member = next(member for member in team_members if member["name"] == name)
        # Display each team member's profile card inside the grid
        st.markdown(
            f"""
            <div class="profile-card">
                <img src="{member['photo_url']}" alt="Photo" class="profile-img">
                <div class="profile-details">
                    <h3>{member['name']}</h3>
                    <p><strong>{member['title']}</strong></p>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    # Close the grid container
    st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()