import json
import requests
import streamlit as st
from streamlit_lottie import st_lottie
import pandas as pd
import numpy as np

def load_lottiefile(filepath:str):
    with open(filepath, "r") as f:
        return json.load(f)

def load_lottieurl(url:str):
    r = requests.get(url)
    if r.status_code!=200:
        return None
    return r.json()

lottie_hello = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_g7dj7gha.json")

st_lottie(lottie_hello, key="Hello!")

st.title('Welcome to My Personal Website!')
st.subheader("I'am so glad you are here!")