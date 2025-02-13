import streamlit as st
import random
from streamlit_theme import \
    st_theme


# st.chat_message("user" / "ai" ) -- changes the icons of who is talking to you!
# play around with buttons
# organizing, putting flows togteher will be the most difficult about this. invest time!
# life path number - cycle information

def figure_out(day):
    if day is None:
        return "Please enter a valid day"
    if 1 <= day <= 5:
        return "menstrual phase"
    elif 6 <= day <= 13:
        return "follicular phase"
    elif 13 <= day <= 15:
        return "ovulation phase"
    elif 16 <= day <= 28:
        return "luteal phase"
    else:
        return "... erks! Sorry! Please choose a number from 1-28"


def my_cycle_page():
    theme = st_theme()
    if theme["base"] == "light":
        st.image("images/light_my_cycle.png")

    else:
        st.image("images/my_cycle.png")
    # st.title("MY CYCLE")
    st.write(f"Understanding your body can make all the difference. "
             f"Do you want to know what’s happening **right now**, **inside you**? "
             f"Explore your menstrual cycle, get personalized workout suggestions, "
             f"and **improve your well-being**. "
             f"Let’s make information and self-care simple, natural, and stigma-free. ")
    st.write(f"And most importantly: **Listen to your body.**")
    st.divider()
    with st.chat_message("user"):
        st.write("Hello Human! ☺️ "
                 "Let me help you identify your cycle.")
        st.session_state.name = st.text_input("What's your name?",
                                                  value=None)
        if st.session_state.name:
            st.write(f"Hello {st.session_state.name}! Glad to see you.")
            day = st.number_input(f"What day of your cycle are you currently on, {st.session_state.name}?",
                                  min_value=0, max_value=28)
            phase = figure_out(day)

            if day:
                st.write(f"You are (most likely) in the {phase}.")
                st.info("Please note that Cycle lengths can vary, and many factors can affect your menstrual cycle.")

                with st.expander(f"Tell me more about the {phase}!"):
                    if phase == "menstrual phase":
                        st.write(f"Estrogen and progesterone are at their lowest, and your body "
                                 f"is busy shedding your uterine lining. It’s not uncommon to feel "
                                 f"lethargic in this phase, so it may help to focus on low impact "
                                 f"movements, like **yoga** or **low intensity walks**. While listening to "
                                 f"your body is key through all stages of your cycle, it’s "
                                 f"especially important during menstruation. If you experience period "
                                 f"related pain or fatigue, **there’s no need to “push through”**! Your "
                                 f"menstrual flow can also affect which types of exercise feel most comfortable."
                                 )
                    elif phase == "follicular phase":
                        st.write(f"As estrogen and progesterone start to increase, you may "
                                 f"find yourself regaining energy. This can be a good time "
                                 f"to focus on **endurance or resistance training**. Going for "
                                 f"**a hike** or **brisk walk** may **feel especially good in this phase**. "
                                 f"The same goes for **weight training**.")
                    elif phase == "ovulation phase":
                        st.write(f"thanks to the LH surge, you may feel extra "
                                 f"alert and ready to move. you might find that  "
                                 f"intense exercise, such as high intensity interval "
                                 f"training and spin classes, feels more manageable. "
                                 f"however, some might experience abdominal pain "
                                 f"during ovulation, so don’t hesitate to take it easy "
                                 f"as needed.")
                    elif phase == "luteal phase":
                        st.write(f"this is where you’re more likely to start losing steam. you might also notice "
                                 f"that it takes you longer to recover from an intense workout. plus, PMS symptoms, "
                                 f"like breast pain or cramps, can make certain types of exercise uncomfortable. "
                                 f"the luteal phase can also have a greater effect on mental health, especially if "
                                 f"you have PMDD or PME. if you tend to feel “down” during this phase, focus on the "
                                 f"types of exercise you enjoy to help manage emotional stress, whether that’s an "
                                 f"easy stroll with a friend or restorative yoga. if you feel up for high intensity "
                                 f"exercise or find that it helps with your mood, go for it, just give yourself "
                                 f"some extra time to recover.")

                with st.expander(f"Show me today's workout recommendation."):
                    st.write("If you feel like it, today's workout can look like this:")
                    if phase == "menstrual phase":
                        # creating a list from which a video can be chosen from randomly
                        ## rahmen anpassen dass es perfekt passt - geht nicht?
                        menstrual_pool = [
                            "https://www.youtube.com/watch?v=VaVIvmQx_Xw",
                            "https://www.youtube.com/watch?v=1bVwzw7m0XM",
                            "https://www.youtube.com/watch?v=vCytq0eygo8&t=29s",
                            "https://www.youtube.com/watch?v=WPBi5cgmsL0"
                        ]
                        # order: received help from DM Lab
                        menstrual_workout = random.choice(menstrual_pool)
                        st.video(menstrual_workout)
                    elif phase == "follicular phase":
                        follicular_pool = [
                            "https://www.youtube.com/watch?v=aBtP7008EfA",
                            "https://www.youtube.com/watch?v=xxa8IdKd8M0",
                            "https://www.youtube.com/watch?v=cw-Wx0fWCEE",
                            "https://www.youtube.com/watch?v=KY8jENkQpDQ"
                        ]
                        follicular_workout = random.choice(follicular_pool)
                        st.video(follicular_workout)
                    elif phase == "ovulation phase":
                        ovulation_pool = [
                            "https://www.youtube.com/watch?v=2xNcUjKLZto",
                            "https://www.youtube.com/watch?v=8MImdWV2WfI",
                            "https://www.youtube.com/watch?v=guE14YKcA6Q",
                            "https://www.youtube.com/watch?v=VGMdIGIAcuw"
                        ]
                        ovulation_workout = random.choice(ovulation_pool)
                        st.video(ovulation_workout)
                    elif phase == "luteal phase":
                        luteal_pool = [
                            "https://www.youtube.com/watch?v=40bPxbFUCj4",
                            "https://www.youtube.com/watch?v=JQ0-ja3SdHU",
                            "https://www.youtube.com/watch?v=NesbXoccSyY",
                            "https://www.youtube.com/watch?v=WbuqNUoA8MM"
                        ]
                        luteal_workout = random.choice(luteal_pool)
                        st.video(luteal_workout)

                    st.write("Remember: If something doesn’t feel right, it’s okay to rest or adjust.")


