import streamlit as st
import pandas as pd
import numpy as np

st.subheader("Tipe Ancaman Cyber")
st.subheader("1. Malware")
st.write("Malware atau malicious software adalah program maupun file yang dibuat untuk \
    mengeksploitasi atau merusak perangkat, server, maupun jaringan.")
st.write("Beberapa jenis malware yaitu:")
st.write("a. Virus: Program yang mereplikasi diri, menempel pada file bersih dan \
    menyebar ke seluruh sistem komputer. Virus menginfeksi file dengan kode berbahaya.")
st.write("b. Trojans: Malware yang menyamar sebagai perangkat lunak yang sah. \
    Penjahat cyber menipu pengguna agar mengunggah Trojan ke komputer mereka untuk mengumpulkan data \
    atau menyebabkan kerusakan.")
st.write("c. Spyware: Malware yang mampu mengumpulkan informasi tentang seseorang atau perusahaan \
    tanpa sepengetahuan mereka. Spyware bertujuan untuk melacak dan menjual data penggunaan internet, \
    menangkap informasi kartu kredit atau rekening bank, dan mencuri informasi pengenal pribadi.")
st.write("d. Ransomware: Malware yang didesain untuk mengunci file atau perangkat, \
    kemudian meminta bayaran sejumlah uang sebagai tebusan.")
st.write("e. Adware: Grayware yang dirancang untuk memasang iklan di layar. \
    Biasanya ditemukan di browser web atau popup.")

st.subheader("2. Injeksi SQL")
st.write("Injeksi SQL (structured query language) adalah jenis ancaman cyber yang digunakan \
    untuk mengambil kendali dan mencuri data dari pusat data. \
    Penjahat cyber memanfaatkan kerentanan dalam aplikasi berbasis data \
    untuk memasukkan kode berbahaya ke dalam basis data melalui pernyataan SQL.")

st.subheader("3. Phishing")
st.write("Attackers berusaha mencuri data sensitif korban dengan cara menyamar sebagai \
    institusi legal dan menghubungi mereka melalui email, telepon, maupun pesan teks.")

st.subheader("4. Serangan Man-in-the-Middle")
st.write("Ancaman jenis ini berbentuk penyadapan komunikasi antara dua individu untuk mencuri data. \
    Misalnya, pada jaringan WIFI yang tidak aman, \
    penyerang dapat mencegat data yang dikirimkan dari perangkat dan jaringan korban.")

st.subheader("5. Serangan Denial-of-Service")
st.write("Metode cyber crime ini mencegah sistem komputer memenuhi permintaan akses yang sah. \
    Caranya dengan membanjiri jaringan dan server dengan traffic, \
    sehingga sistem tidak bisa dijalankan.")