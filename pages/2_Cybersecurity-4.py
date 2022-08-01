import streamlit as st
import pandas as pd
import numpy as np

st.subheader("Metode Ancaman Cyber")
st.subheader("1. Malware")
st.write("Malware atau malicious software adalah salah satu ancaman cyber paling umum. Perangkat lunak ini dibuat untuk mengganggu atau merusak komputer pengguna. Malware seringkali menyebar melalui lampiran email atau unduhan yang nampak sah.")
st.write("Beberapa jenis malware yaitu:")
st.write("a. Virus: Program yang mereplikasi diri, menempel pada file bersih dan menyebar ke seluruh sistem komputer. Virus menginfeksi file dengan kode berbahaya.")
st.write("b. Trojans: Sejenis malware yang menyamar sebagai perangkat lunak yang sah. Penjahat cyber menipu pengguna agar mengunggah Trojan ke komputer mereka untuk mengumpulkan data atau menyebabkan kerusakan.")
st.write("c. Spyware: Program ini secara diam-diam merekam apa yang dilakukan pengguna, sehingga penjahat dunia maya dapat menggunakan informasi ini. Misalnya spyware digunakan untuk menangkap detail kartu kredit.")
st.write("d. Ransomware: Malware yang mengunci file dan data pengguna, dengan ancaman akan menghapusnya kecuali pemilik data membayar tebusan.")
st.write("e. Adware: Perangkat lunak periklanan yang dapat digunakan untuk menyebarkan malware.")
st.write("f. Botnet: Jaringan komputer yang terinfeksi malware dapat digunakan penjahat cyber untuk melakukan aktivitas secara online tanpa izin pengguna.")

st.subheader("2. Injeksi SQL")
st.write("Injeksi SQL (structured query language) adalah jenis ancaman cyber yang digunakan untuk mengambil kendali dan mencuri data dari pusat data. Penjahat cyber memanfaatkan kerentanan dalam aplikasi berbasis data untuk memasukkan kode berbahaya ke dalam basis data melalui pernyataan SQL. Ini memberi mereka akses ke informasi sensitif yang terdapat dalam pusat data.")

st.subheader("3. Phishing")
st.write("Jika Anda pernah mendapat email yang nampaknya berasal dari perusahaan sah, dan meminta informasi sensitif, bisa jadi Anda menjadi target phishing. Serangan ini sering digunakan untuk menipu orang agar memberikan data dan informasi pribadi.")

st.subheader("4. Serangan Man-in-the-Middle")
st.write("Ancaman jenis ini berbentuk penyadapan komunikasi antara dua individu untuk mencuri data. Misalnya, pada jaringan WIFI yang tidak aman, penyerang dapat mencegat data yang dikirimkan dari perangkat dan jaringan korban.")

st.subheader("5. Serangan Denial-of-Service")
st.write("Metode cyber crime ini mencegah sistem komputer memenuhi permintaan akses yang sah. Caranya dengan membanjiri jaringan dan server dengan traffic, sehingga sistem tidak bisa dijalankan.")