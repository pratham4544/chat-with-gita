from src.helper import *
import streamlit as st
from dotenv import load_dotenv
import os
import random
from src.registration import *
from src.mongo import *
from pages import *
from streamlit_option_menu import option_menu
from src.logger import *
from src.google_analytics import *


logging.info('all imports successfully initiatied..')

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
GoogleGenerativeAIEmbeddings.api_key = api_key
os.environ['LANGCHAIN_TRACING_V2'] = 'true'
LANGCHAIN_API_KEY = os.getenv('LANGCHAIN_API_KEY')

st.set_page_config(
    page_title="Chat with Gita",
    page_icon=":om:",
    layout="centered",
    initial_sidebar_state="collapsed",
)
def main():
    
    st.header("Chat with Bhagwat Geet 💭")
    st.subheader("Seeking Guidance for Life's Questions 📚")
    inject_google_analytics()  # Inject GA code
    inject_ga() # antoher method to check GA working or not
    


# Include Google Analytics tracking code
    with open(r"src/google_analytics.html", "r") as f:
        html_code = f.read()
        components.html(html_code, height=0)


    st.image("assets/geeta.jpeg")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("Register"):
            
            logging.info("user press the register button")
            st.switch_page('pages/Registration.py')
    
    with col2:
        if st.button("Login"):
            logging.info("user press the login button")
            st.switch_page('pages/Login.py')
            
    with col3:
        if st.button("Chat"):
            logging.info("user press the chat button")
            st.switch_page('pages/Chat.py')
            
    logging.info('homepage load successfully')


if __name__ == "__main__":
    main()
