import streamlit as st
from streamlit_theme import st_theme


def resources_page():
    theme = st_theme()
    if theme["base"] == "light":
        st.image("images/light_resources.png")

    else:
        st.image("images/resources.png")

    # st.title("Resources")
    st.header("Information on different Cycle Phases")
    st.markdown("If you just need an overview on the menstrual cycle and it's "
                "functions, find it here. Have fun and explore. ")
    #st.divider()

    tab1, tab2, tab3, tab4 = st.tabs(["Menstrual phase", "Follicular Phase", "Ovulation Phase", "Luteal Phase"])

    # Menstrual Expander
    #    with st.expander("Menstrual Phase"):
    with tab1:
        st.write(f"Estrogen and progesterone are at their lowest, and your body "
                 f"is busy shedding your uterine lining. It’s not uncommon to feel "
                 f"lethargic in this phase, so it may help to focus on low impact "
                 f"movements, like **yoga** or **low intensity walks**. While listening to "
                 f"your body is key through all stages of your cycle, it’s "
                 f"especially important during menstruation. If you experience period "
                 f"related pain or fatigue, **there’s no need to “push through”**! Your "
                 f"menstrual flow can also affect which types of exercise feel most comfortable."
                 )
        with st.expander("These are examples for what movement could look like, during this phase:"):
            c1, c2 = st.columns(2)
            c3, c4 = st.columns(2)
            with c1:
                st.video("https://www.youtube.com/watch?v=VaVIvmQx_Xw")
            with c2:
                st.video("https://www.youtube.com/watch?v=1bVwzw7m0XM")
            with c3:
                st.video("https://www.youtube.com/watch?v=vCytq0eygo8&t=29s")
            with c4:
                st.video("https://www.youtube.com/watch?v=WPBi5cgmsL0")

    # Follicular Expander
    with tab2:
        st.write(f"As estrogen and progesterone start to increase, you may "
                 f"find yourself regaining energy. This can be a good time "
                 f"to focus on **endurance or resistance training**. Going for "
                 f"**a hike** or **brisk walk** may **feel especially good in this phase**. "
                 f"The same goes for **weight training**.")
        with st.expander("These are examples for what movement could look like, during this phase:"):
            c1, c2 = st.columns(2)
            c3, c4 = st.columns(2)
            with c1:
                st.video("https://www.youtube.com/watch?v=aBtP7008EfA")
            with c2:
                st.video("https://www.youtube.com/watch?v=xxa8IdKd8M0")
            with c3:
                st.video("https://www.youtube.com/watch?v=cw-Wx0fWCEE")
            with c4:
                st.video("https://www.youtube.com/watch?v=KY8jENkQpDQ")

    # Ovulation Expander
    with tab3:
        st.write(f"Thanks to the LH surge, you may feel extra "
                 f"alert and ready to move. You might find that  "
                 f"**intense exercise**, such as high intensity interval "
                 f"training and spin classes, **feels more manageable**. "
                 f"However, some might experience abdominal pain "
                 f"during ovulation, so **don’t hesitate to take it easy "
                 f"as needed**.")
        with st.expander("These are examples for what movement could look like, during this phase:"):
            c1, c2 = st.columns(2)
            c3, c4 = st.columns(2)
            with c1:
                st.video("https://www.youtube.com/watch?v=2xNcUjKLZto")
            with c2:
                st.video("https://www.youtube.com/watch?v=8MImdWV2WfI")
            with c3:
                st.video("https://www.youtube.com/watch?v=guE14YKcA6Q")
            with c4:
                st.video("https://www.youtube.com/watch?v=VGMdIGIAcuw")

    # Luteal Expander
    with tab4:
        st.write(f"This is where you’re more likely to start losing steam. you might also notice "
                 f"that it takes you longer to recover from an intense workout. Plus, PMS symptoms, "
                 f"like breast pain or cramps, can make certain types of exercise uncomfortable. "
                 f"The luteal phase can also have a **greater effect on mental health**, especially if "
                 f"you have **PMDD** or **PME**. If you tend to feel “down” during this phase, focus on the "
                 f"types of exercise you enjoy to help manage emotional stress, whether that’s an "
                 f"**easy stroll with a friend or restorative yoga**. If you feel up for high intensity "
                 f"exercise or find that it helps with your mood, **go for it**, just give yourself "
                 f"some **extra time to recover**.")
        with st.expander("These are examples for what movement could look like, during this phase:"):
            c1, c2 = st.columns(2)
            c3, c4 = st.columns(2)
            with c1:
                st.video("https://www.youtube.com/watch?v=40bPxbFUCj4")
            with c2:
                st.video("https://www.youtube.com/watch?v=JQ0-ja3SdHU")
            with c3:
                st.video("https://www.youtube.com/watch?v=NesbXoccSyY")
            with c4:
                st.video("https://www.youtube.com/watch?v=WbuqNUoA8MM")

    # create some space inbetween
    st.divider()
    st.write("")
    st.header("Cycle Syncing")
    st.write("You may ask yourself - why should I even sync my workouts with my cycle in the first place? ")
    st.write("If all of this feels very new to you, consider taking a look on this selection "
             "of video resources. Keep in mind: these are external sources and you may want to "
             "pay attention to the disclaimer on our *About* page.")
    st.write("")

    st.video("https://youtu.be/vh0fHMw7t9Q?si=0EUaUQdiGXlWCFft")
    st.caption("If you would like to see someone testing cycle synching - watch this! "
               "This video can give you a better idea of what a real implementation of cycle synching could look like. ")

    #c1, c2 = st.columns(2)
    #with c1:
        #st.video("https://youtu.be/vh0fHMw7t9Q?si=0EUaUQdiGXlWCFft")
        #st.caption("If you would like to see someone testing cycle synching - watch this!")
    #with c2:
        #st.text(
            #"This video can give you a better idea of what a real implementation of cycle synching could look like. ")

    # create small space
    st.write("")
    st.write("")
    st.subheader("Additional resources")
    st.text("Feel free to browse through these!")

    c3, c4 = st.columns(2)
    with c3:
        st.video("https://youtu.be/wtxQRuEmgyM?si=M1_DvVzRGpy6WPiN")
        st.caption("Learn more about how periods and hormones can affect your mood.")
    with c4:
        st.video("https://youtu.be/BFa2egx-jI8?si=F_ftFj84ekQB_ikW")
        st.caption("Why your menstrual cycle is your SUPER POWER, NOT A WEAKNESS!")
