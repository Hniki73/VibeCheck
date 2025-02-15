import segno
from io import BytesIO
import streamlit as st
import time
import random

# APP DESIGN
st.set_page_config(page_title="VibeCheck", page_icon="✨", layout="centered")

# BACKGROUND
# Code adapted from: keshavsingh2004, 2023. & Fanilo Andriansolo´s video tutorial, 2022
# Source: https://discuss.streamlit.io/t/can-i-put-these-animations-in-the-background/53685/2
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(45deg, 
            #FF9A9E 0%, 
            #FAD0C4 20%, 
            #FBC2EB 40%, 
            #A6C1EE 60%, 
            #C2E9FB 80%, 
            #D4FC79 100%);
        background-size: 400% 400%;
        animation: gradientBG 15s ease infinite;
    }

    @keyframes gradientBG {
        0% {background-position: 0% 50%;}
        50% {background-position: 100% 50%;}
        100% {background-position: 0% 50%;}
    }

    body, .stMarkdown {
        color: black;
        font-family: 'Roboto', sans-serif;
    }
    .big-text {font-size:24px; text-align:center; font-weight:bold;}
    </style>
    """,
    unsafe_allow_html=True
)

# NAME INPUT
def get_user_name():
    if 'user_name' not in st.session_state or not st.session_state.user_name:
        st.title("🌈 VibeCheck 🌈")
        st.write("Welcome! What's your name?")
        user_name = st.text_input("Enter your name:")
        if user_name:
            st.session_state.user_name = user_name
            st.rerun()
    return st.session_state.get('user_name', '')

# USER´S NAME FUNCTION THAT CAN BE CARRIED FORWARD
user_name = get_user_name()

# ONLY PROCEED IF A NAME HAS BEEN ENTERED
if user_name:
    st.title(f"🌈 Welcome, {user_name}! 🌈")
    st.write("Let's check your vibe!")

    # STRESS LEVELS
    stress_levels = {
        "🌤️": "Chill",
        "🌥️": "Meh",
        "🌧️": "Stressed",
        "⛈️": "Overwhelmed",
        "🚨": "Crisis"
    }
    selected_level = st.selectbox("Select your stress level:", list(stress_levels.keys()), index=None, placeholder="Choose one...")

    # SOLUTIONS
    solutions = {
        "🌤️": ["No worries, it could be worse too."],
        "🌥️": ["Scan the QR code to see something funny! 🐮"],
        "🌧️": ["Try some deep breathing exercises. Inhale for 5 seconds, hold for 5 and exhale for 5 seconds"],
        "⛈️": ["Play this, I hope you'll love it as much as I do, and it fascinates you as much as it did me."],
        "🚨": ["Reach out to a loved one or professional 📞. You are not alone ❤️"]
    }

    st.write("### Your vibe reset:")
    st.markdown(
        f'<p style="color: black; font-size: 20px; font-weight: bold;">{random.choice(solutions[selected_level])}</p>',
        unsafe_allow_html=True
    )

    # MEMES FOR LEVEL 1 (🌤️)
    meme_links = [
        "https://i.chzbgr.com/full/9008088320/h92788AA5/is-already-serving-the-next-customer-and-youre-not-finished-putting-your-change-in-your-wallet",
        "https://i.pinimg.com/550x/f6/42/60/f64260de169551e8ab21915866fe076c.jpg",
        "https://www.nairaland.com/attachments/11517896_images11_jpeg0a11a8ec37620e47e4feab56245e56df",
        "https://i.imgflip.com/197ym7.jpg",
        "https://img.buzzfeed.com/buzzfeed-static/static/2018-04/30/14/enhanced/buzzfeed-prod-web-02/original-30027-1525112427-4.png",
        "https://img.buzzfeed.com/buzzfeed-static/static/2018-04/27/16/asset/buzzfeed-prod-web-01/sub-buzz-18535-1524860227-1.png"
    ]

    # DISPLAY MEMES FOR LEVEL 1 (🌤️)
    # Source: ChatGPT
    if selected_level == "🌤️":
        random_meme = random.choice(meme_links)
        st.image(random_meme, caption="😂 Hope this made you smile!")

    # QR CODE FOR COW TIKTOK (LEVEL 2)
    if selected_level == "🌥️":
        qr = segno.make("https://vm.tiktok.com/ZGdyYVspY/")
        qr_img = BytesIO()
        qr.save(qr_img, scale=5, kind='png')
        st.image(qr_img, caption="Scan me to watch 🐄")

    # BREATHING EXERCISE FOR LEVEL 3 (🌧️)
    if selected_level == "🌧️":
        st.write("### Guided Breathing Exercise")
        st.write("Follow the breathing guide below:")
        progress_bar = st.progress(0)
        for i in range(16):  # 15 seconds total
            time.sleep(1)
            progress_bar.progress(i / 15)
        st.success("Great job! Keep breathing deeply.")

    # YOUTUBE BUTTON FOR LEVEL 4 (⛈️)
    # Source: ChatGPT
    if selected_level == "⛈️":
        video_url = "https://youtube.com/shorts/x35j2Q50gT8"
        st.markdown(f'[▶️ Watch Now]({video_url})', unsafe_allow_html=True)

    # RESET BUTTON
    if st.button("🏠 Home"):
        del st.session_state['user_name']
        st.rerun()
