import streamlit as st
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import style
from PIL import Image

st.title('Kaspersky Mencatat Indonesia Hadapi 11 Juta Serangan Siber pada Kuartal Pertama 2022')
st.write('Maraknya ancaman siber dipicu oleh banyaknya orang yang menggunakan dunia maya untuk NFT, metaverse, transaksi aset kripto dan adopsi investasi di kalangan anak muda.')
st.write('Kaspersky mencatat pada Januari-Maret 2022, produk mereka mendeteksi dan memblokir 11.802.558 ancaman siber yang berbeda.')
st.metric(label="Serangan Siber 2021", value=9639740,
     delta_color="inverse")

st.metric(label="Serangan Siber 2022", value=11802558, delta=2162818,
     delta_color="inverse")
    
st.write('Berdasarkan statistik diatas, Kaspersky mencatat Indonesia berada di urutan teratas di wilayah Asia Tenggara dan urutan 60 di dunia dalam hal bahaya yang ditimbulkan dari berselancar di internet.')
df = pd.DataFrame({
     'Negara' : ["Malaysia", "Singapura", "Thailand", "Filipina", "Brunei Darussalam", "Indonesia", \
          "Vietnam", "Laos", "Kamboja", "Myanmar"],
     'Skor (skala 0-100)' : [79.22, 71.43, 64.94, 63.64, 41.56, 38.96, 36.36, 18.18, 15.58, 10.39]
})
df

image = Image.open('rank_cybersecurity.png')
st.image(image)

st.write('Kaspersky mengingatkan masyarakat untuk berpikir ulang sebelum mengklik tautan yang mencurigakan dari email atau pesan teks.')
st.write('Ketika memasang aplikasi, pastikan hanya mengunduh dari tempat resmi seperti Google Play dan App Store. Meskipun tidak menjamin 100% aman, tetapi risiko menghadapi serangan siber, seperti malware Trojan akan jauh lebih rendah.')
st.write('Biasakan untuk memperbarui sistem operasi dan aplikasi untuk menjaga keamanan data dan perangkat.')
st.write('Gunakan koneksi yang aman ketika menggunakan internet. Hindari mengakses bank atau layanan penting menggunakan WiFi publik.')
