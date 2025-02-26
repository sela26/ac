import streamlit as st
from streamlit_theme import st_theme  # external component: https://discuss.streamlit.io/t/new-component-st-theme-it-returns-the-active-theme-of-the-streamlit-app/64424
from about import about_page
from resources import resources_page
from my_cycle_chatbot import my_cycle_page
from get_active import get_active_page
from selfcare import selfcare_page


# the streamlit app
st.set_page_config(
    page_icon="🩸",
    page_title="ACTIVE CYCLE"
)


def home_page():
    # title banner
    # used external component:
    # https://discuss.streamlit.io/t/new-component-st-theme-it-returns-the-active-theme-of-the-streamlit-app/64424
    theme = st_theme()
    # searches in theme dictionary for what stands behind "base" - light / dark
    if theme["base"] == "light":
        st.image("images/light_banner.jpg")

    else:
        st.image("images/Banner.jpg")

    # set title
    st.title("Welcome to Active Cycle!")
    st.divider()
    st.subheader("Hey, good to see you!")
    st.write("Active Cycle is designed to help you sync your workouts with your menstrual cycle, "
                "offering personalized recommendations based on your current phase. Whether you’re "
                "full of energy or in need of a slower pace, we’ve got you covered. ")
    st.write("")
    st.write("**What you’ll find here:**")
    st.write("❋ **Cycle-Aware Workouts**: Get movement suggestions tailored to your cycle phase. ")
    st.write("❋ **Smart Chatbot Support**: Easily track your phase and get fitness guidance. ")
    st.write("❋ **Self-Care & Wellness**: Discover daily self-care activities and uplifting quotes.")
    st.write("❋ **Resources Hub**: Learn about your cycle, find workout videos, and explore tips for cycle syncing.")
    st.write("Whether you're looking for a high-energy workout, a restorative stretch, or just some self-care inspiration, "
            "Active Cycle is here to support you—every step of the way.")


# page selection list
options = ['Home',
           'My Cycle',
           'Resources',
           'Get ACTIVE',
           'Selfcare',
           'About',
           # 'menstrual'
           ]
page_selection = st.sidebar.selectbox("Menu", options)

# navigating between the pages
if page_selection == 'Home':
    home_page()
elif page_selection == 'About':
    about_page()
elif page_selection == 'Resources':
    resources_page()
elif page_selection == 'My Cycle':
    my_cycle_page()
elif page_selection == 'Get ACTIVE':
    get_active_page()
elif page_selection == 'Selfcare':
    selfcare_page()
