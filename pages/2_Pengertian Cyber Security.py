import streamlit as st
import pandas as pd
import numpy as np

st.header("Cyber Security")
st.subheader("Pengertian Cyber Security")
st.write("Cyber security adalah tindakan yang dilakukan untuk melindungi sebuah perangkat, \
    jaringan, program, dan data dari serangan digital yang berbahaya. \
    Tindakan cyber security mencakup pemasangan firewall, backup data, multi factor authentication, dll \
    yang dapat digunakan untuk mencegah cyber criminals memasuki sistem.")

st.subheader("Konsep Cyber Security")
st.write("Cyber Security mengikuti praktek CIA Triad sebagai konsep dasarnya yang meliputi : ")
st.write("1. Confidentiality (Kerahasiaan)")
st.write("Upaya untuk merahasiakan sebuah informasi dan data agar tidak terjadi pencurian maupun kebocoran data.")

st.write("2. Integrity (Integritas)")
st.write("Memastikan bahwa semua data dan informasi yang diberikan tetap konsisten, akurat, dan terpercaya.")

st.write("3. Availability (Ketersediaan)")
st.write("Data dan informasi yang ada dapat diakses dengan mudah dan lancar.")