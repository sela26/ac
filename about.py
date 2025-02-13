import streamlit as st
from streamlit_theme import \
    st_theme

def about_page():
    theme = st_theme()
    if theme["base"] == "light":
        st.image("images/light_about.png")

    else:
        st.image("images/about.png")
    # set title
    # st.title("ABOUT")
    st.write("Find out about our purpose and ethics.")
    st.write("Please notice the disclaimer for optimal and safe use of *Active Cycle*.")
    st.divider()

    # Purpose Text
    purpose = ("**Active Cycle is designed to help people seamlessly integrate more movement into their "
               "daily lives, even when things get busy.** "
               "We understand that juggling work, personal commitments, and "
               "self-care can make regular gym visits seem impossible. "
               "That's why we've created a solution for those with hectic schedules, "
               "those unsure where to begin, and anyone interested in syncing their "
               "activity with their menstrual cycle. "
               "Whether you’re just getting started or seeking a holistic approach to well-being, "
               "Active Cycle is here to guide and support you on your journey.")

    st.header("Purpose")
    st.markdown(purpose)
    st.divider()

    # Ethics Text
    ethics = ("The intention of this application is to encourage people to work "
              "**with their bodies, not against them**. Physical activity is often closely "
              "tied to body image, which can be a sensitive issue. "
              "Active Cycle aims to promote a **balanced, active lifestyle** "
              "rather than an obsessive one. "
              "For this reason, we are committed to using mindful and inclusive language that "
              " fosters a healthy relationship with exercise and body image. "
              "Our goal is to support users in cultivating a positive, sustainable approach "
              "to physical activity, respecting the natural rhythms of their bodies.")

    st.header("Ethics")
    st.markdown(ethics)
    st.divider()

    # Disclaimer Text

    disclaimer = ("**Every body is different!** "
                  "The app is based on average values. "
                  "However, variations in cycle length are completely normal. "
                  "Therefore, *my cycle* should be used as a guideline rather than a strict rule.")

    st.header("Disclaimer")
    st.markdown(disclaimer)
    st.divider()