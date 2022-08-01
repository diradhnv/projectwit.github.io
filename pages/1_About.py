import json
import requests
import streamlit as st
from streamlit_lottie import st_lottie
import pandas as pd
import numpy as np

st.write("Hello!")
st.write("I'am Diaz Ramadhiani, from central java, people usually call me 'Dira'")
st.write("I'am 5th semester student of Informatics Engineering from the Institute Technology PLN.")
st.write("I have an interest in the IT world especially in cybersecurity.")
st.write("That's all from me. Thank You.")

def load_lottiefile(filepath:str):
    with open(filepath, "r") as f:
        return json.load(f)

def load_lottieurl(url:str):
    r = requests.get(url)
    if r.status_code!=200:
        return None
    return r.json()

lottie_hello = load_lottieurl("https://assets2.lottiefiles.com/private_files/lf30_twbpyk8b.json")

st_lottie(lottie_hello, key="Hello!")