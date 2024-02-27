from pathlib import Path 
import json
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_extras.let_it_rain import rain

# Directories and file paths
THIS_DIR = Path(__file__).parent
CSS_FILE = THIS_DIR / "style" / "style.css"
ASSETS = THIS_DIR / "assets"
LOTTIE_ANIMATION = ASSETS / "Polite_Chicky.json"


# Function to Load and display the Lottie animation
def load_lottie_animation(file_path):
    with open(file_path, "r") as f:
        return json.load(f)
    

# Function to apply snowfall effect
def run_snow_animation():
    rain(emoji="🥳", font_size=20, falling_speed=5, animation_length="infinite")


# Function to get the name from query parameters
def get_person_name():
    query_params = st.experimental_get_query_params()
    return query_params.get("name", ["Yeisha"])[0]


#page configuration
st.set_page_config(page_title= "happy birthday", page_icon= "🥰")

# run snowfall animation
run_snow_animation()

#apply custom css
with open(CSS_FILE) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

#display header with personalized name
PERSON_NAME = get_person_name()
st.header(f"happy birthday, {PERSON_NAME}!🥳"  ,anchor=False)

#display the lottie animation
lottie_animation = load_lottie_animation(LOTTIE_ANIMATION)
st_lottie(lottie_animation, key="Polite_Chicky", height=300)

#pesonalized holiday message
st.markdown(
    f"Dear {PERSON_NAME}, wishing you happy birthday and more birthday to come sha. 🥳"
)
    

