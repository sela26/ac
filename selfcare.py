import streamlit as st
import random
import time
from streamlit_theme import st_theme

# st.write(st.session_state.name)
if 'name' in st.session_state:
    st.session_state.name = st.session_state.name

def selfcare_page():
    theme = st_theme()
    if theme["base"] == "light":
        st.image("images/light_selfcare.png")

    else:
        st.image("images/selfcare.png")
    # st.title("Selfcare Area")
    if "name" not in st.session_state:
        st.session_state.name = "User"

    # code to transform streamlit name variable into name variable to avoid output "None"
    # might look a bit weird but that was the only solution we could come up with in the dm lab!
    name = st.session_state.name
    if 'name' not in st.session_state:
        st.session_state.name = "User"
    if name == None:
        name = "User"

    st.subheader(f"Hi {name}!")
    st.divider()
    st.write("Let us tell you a secret - actually, the whole space we provide for you is trying to be a "
             "self care area. But what you will find here is just for you. "
             "Thank you for your support. "
             "Here, you can receive a personal quote or a small activity to start or end "
             "your day with the right intention - or just to pick up a positive impulse in-between.")

    # Quotes
    selfcare_quote_pool = [
                            "“Self-care is never a selfish act—it is simply good stewardship of the only gift "
                            "I have, the gift I was put on earth to offer to others.” — Parker Palmer",
                            "“One of the greatest regrets in life is being what others would want you to be, "
                            "rather than being yourself.”―Shannon L. Alder",
                            "“It is interesting how often we can’t see all the ways in which we are being "
                            "strong.”—Lena Dunham",
                            "“Life isn’t about finding yourself. Life is about creating yourself.”—George Bernard Shaw",
                            "“If you’re not someone who has a natural and effortless love for yourself, it’s hard to let "
                            "go of your desire to please other people, and that’s really not an ingredient for a happy life.”—Anne Hathaway",
                            "“Find out who you are and do it on purpose.”—Dolly Parton",
                            "“I’m all about body positivity and self-love because I believe that we can save the world if we first save ourselves.”—Lizzo ",
                            "“Rest and self-care are so important. When you take time to replenish your spirit, it allows you to serve others from the overflow. You cannot serve from an empty vessel.” —Eleanor Brownn",
                            ]
    quote_button = st.button("Discover a quote")

    selfcare_activity_pool = ["Take five deep breaths. Inhale through your nose, hold for a few seconds, and exhale slowly. It’s a small reset for your body and mind.",
                              "Put on a song you love. Whether it’s something calming or upbeat, let yourself enjoy the music. Maybe even move a little if you feel like it.",
                              "Write down three good things from today. They don’t have to be big—just anything that made the day a little better.",
                              "Drink a glass of water. If you’ve been running on caffeine or just forgetting, this is your reminder to hydrate.",
                              "Look out the window and notice something new. A building, a plant, a passerby—just something you hadn’t paid attention to before.",
                              "Jot down whatever’s on your mind. No structure, no pressure—just get your thoughts out, even if it’s a messy brain dump.",
                              "Do something small for yourself. Make your bed, change into comfy clothes, or tidy up your space just a little.",
                              "Sit still for a minute and just exist. No distractions, no expectations—just take a moment to do nothing at all.",

                              ]
    activity_button = st.button("Discover an activity")

    if quote_button:
        with st.spinner("Picking a quote for you..."):
            time.sleep(2)
            selfcare_quote = random.choice(selfcare_quote_pool)
            st.warning(selfcare_quote)

    if activity_button:
        with st.spinner("Picking an activity for you..."):
            time.sleep(2)
            selfcare_activity = random.choice(selfcare_activity_pool)
            st.success(selfcare_activity)

    st.divider()