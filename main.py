import streamlit as st
#import streamlit.components.v1 as components
import pandas as pd
import altair as alt
#from numerize import numerize

st.set_page_config(layout='wide')

df_jumlah_desa = pd.read_csv('dataset/data_desa_provinsi_baru.csv', sep=';', index_col=None)
df_bts_sinyal_kuat = pd.read_csv('dataset/bts_sinyal_kuat.csv', sep=';', index_col=None)
df_bts_sinyal_lemah = pd.read_csv('dataset/bts_sinyal_lemah.csv', sep=';', index_col=None)
df_bts_sinyal_tiada = pd.read_csv('dataset/bts_sinyal_tiada.csv', sep=';', index_col=None)
df_nonbts_sinyal_kuat = pd.read_csv('dataset/nonbts_sinyal_kuat.csv', sep=';', index_col=None)
df_nonbts_sinyal_lemah = pd.read_csv('dataset/nonbts_sinyal_lemah.csv', sep=';', index_col=None)
df_nonbts_sinyal_tiada = pd.read_csv('dataset/nonbts_sinyal_tiada.csv', sep=';', index_col=None)

df_bts_total = pd.concat([df_jumlah_desa['Provinsi'], 
                             df_bts_sinyal_kuat['2018']+df_bts_sinyal_lemah['2018']+df_bts_sinyal_tiada['2018'],
                             df_bts_sinyal_kuat['2019']+df_bts_sinyal_lemah['2019']+df_bts_sinyal_tiada['2019'],
                             df_bts_sinyal_kuat['2020']+df_bts_sinyal_lemah['2020']+df_bts_sinyal_tiada['2020'],
                             df_bts_sinyal_kuat['2021']+df_bts_sinyal_lemah['2021']+df_bts_sinyal_tiada['2021']
                             ], axis=1, keys=['Provinsi','2018','2019','2020','2021'])

df_nonbts_total = pd.concat([df_jumlah_desa['Provinsi'], 
                             df_nonbts_sinyal_kuat['2018']+df_nonbts_sinyal_lemah['2018']+df_nonbts_sinyal_tiada['2018'],
                             df_nonbts_sinyal_kuat['2019']+df_nonbts_sinyal_lemah['2019']+df_nonbts_sinyal_tiada['2019'],
                             df_nonbts_sinyal_kuat['2020']+df_nonbts_sinyal_lemah['2020']+df_nonbts_sinyal_tiada['2020'],
                             df_nonbts_sinyal_kuat['2021']+df_nonbts_sinyal_lemah['2021']+df_nonbts_sinyal_tiada['2021']
                             ], axis=1, keys=['Provinsi','2018','2019','2020','2021'])


st.title("Analisis Singkat Distribusi Base Transceiver Station (BTS) dan Cakupan Sinyal BTS pada Desa/Kelurahan di Indonesia")

st.subheader("Oleh Hasnito Lailu Sobrian; hasnitos@gmail.com")

st.header('Pendahuluan')
st.markdown('<div style="text-align: justify;">Sekarang ini, peran internet telah menjadi sangat penting dan mendominasi hampir setiap aspek kehidupan kita. Internet telah mengubah cara kita bekerja, berkomunikasi, berbelanja, mengakses informasi, dan menjalankan bisnis. Pentingnya internet sangat terasa ketika wabah COVID-19 terjadi di mana pemerintah menggalakkan program Work From Home dan School From Home. Belum lagi ditambah mulainya Revolusi Industri 4.0 yang menghadirkan teknologi baru seperti Kecerdasan Buatan dan Internet of Things di mana peran internet sangat krusial untuk menunjang keberlangsungannya.</div>', unsafe_allow_html=True)
st.markdown('<div style="text-align: justify;">Salah satu perangkat yang dapat digunakan untuk mengakses internet adalah smartphone. Kelebihan smartphone dibanding perangkat lain seperti laptop dan komputer adalah harganya yang relatif terjangkau untuk semua kalangan dan ukuran yang praktis untuk digunakan di mana saja asalkan ada jaringan seluler. Hal ini menyebabkan lebih banyak orang menggunakan smartphone dibandingkan laptop dan komputer untuk melakukan aktivitas sehari-hari.</div>', unsafe_allow_html=True)
st.markdown('<div style="text-align: justify;">Untuk menunjang kebergunaan smartphone, diperlukan jaringan seluler yang kuat. Jaringan seluler dipancarkan dari menara Base Transceiver Station (BTS) kemudian ditangkap oleh smartphone yang dapat dijangkau jaringannya. Pada smartphone, kriteria kuat tidaknya jaringan yang ditangkap yaitu dengan indikator batang sinyal, di mana semakin penuh batang sinyal maka kualitas jaringan akan semakin kuat. Oleh karena itu, BTS merupakan infrastruktur penting untuk menunjang aksesibilitas internet pada masyarakat luas. Dari sinilah, analisis dilakukan untuk mencari tahu bagaimana persebaran BTS dan kualitas sinyalnya di Indonesia.</div>', unsafe_allow_html=True)

st.markdown('<br>', unsafe_allow_html=True)
st.header('Analisis')
col1, col2 = st.columns([1,2])

with col1:
    st.markdown(f'<div style="text-align: justify;">Dari data yang disediakan web bps.go.id, didapatkan data berupa jumlah desa/kelurahan yang telah terpasang ataupun belum terpasang BTS serta kualitas sinyalnya. Data ini kemudian dianalisis di mana didapatkan bahwa pada tahun 2021, dari {int(df_jumlah_desa["2021"].sum())} desa/kelurahan di Indonesia, baru {float((df_bts_sinyal_kuat["2021"].sum()+df_nonbts_sinyal_kuat["2021"].sum())/df_jumlah_desa["2021"].sum()):.0%} yang terjangkau sinyal BTS secara efektif. Selain itu, jumlah desa/kelurahan yang terpasang BTS baru {df_bts_total["2021"].sum()} desa/kelurahan, yang berarti hanya {float(df_bts_total["2021"].sum()/df_jumlah_desa["2021"].sum()):.0%} dari keseluruhan desa/kelurahan. Adapun data yang didapat hanya sampai tahun 2021 karena kemungkinan sensus tersendat birokrasi di mana pada tahun 2022 terjadi pemekaran provinsi sehingga jumlah provinsi di Indonesia ada 38 bukan 34.</div>', unsafe_allow_html=True)
    st.markdown(f'<div style="text-align: justify;">Jika sekilas dilihat, cakupan BTS 73% merupakan angka yang tidak buruk. Namun, apabila dilihat lebih dalam, terlihat perbedaan efektivitas yang mencolok antara Provinsi dengan efektivitas sinyal terbaik dan provinsi dengan efektivitas sinyal yang paling kurang. Kesenjangan ini tentu saja dapat menghambat aktivitas masyarakat di wilayah dengan efektivitas sinyal kurang baik ketika memerlukan internet, utamanya pada saat social distancing pandemi COVID-19 yang sebelumnya diberlakukan.', unsafe_allow_html=True)
    st.markdown(f'<div style="text-align: justify;">Dari grafik di samping, dapat dilihat bahwa Papua merupakan provinsi dengan cakupan sinyal efektif dan jumlah desa/kelurahan terpasang BTS yang terendah. Hal ini disebabkan karena Papua merupakan daerah konflik di mana didapatkan berita terkini bahwa ada teknisi BTS disandera oleh terduga anggota KKB.', unsafe_allow_html=True)
    st.markdown(f'<div style="text-align: justify;">Usaha untuk mengurangi kesenjangan pun telah dilakukan. Pada grafik, apabila dilihat perubahan nilai tiap tahunnya diganti, nilainya akan cenderung meningkat. Namun, pada grafik Cakupan Sinyal Efektif, grafik teratas tetap menunjukkan kondisi yang relatif Jawa-Bali sentris di mana Provinsi di Pulau Jawa dan Bali berturut mendapatkan cakupan sinyal yang paling efektif.', unsafe_allow_html=True)
    st.markdown(f'<div style="text-align: justify;">Pada tahun 2021, untuk grafik Rasio Desa/Kelurahan Terpasang BTS, dapat dilihat bahwa Nusa Tenggara Barat dan Bangka Belitung menempati posisi lima besar. Hal ini tentu saja mengundang tanda tanya karena kedua Provinsi tidak masuk lima besar Cakupan Sinyal Efisien. Hal ini menunjukkan bahwa banyaknya Desa/Kelurahan yang terpasang BTS belum tentu berhubungan dengan Cakupan Sinyal Efektif yang didapatkan. Karena keterbatasan waktu dan data yang ada, tidak dapat dilakukan analisis lebih lanjut tentang korelasi keduanya dikarenakan terdapat faktor lain seperti luas desa/kelurahan dan jumlah BTS yang terpasang pada tiap desa/kelurahan.', unsafe_allow_html=True)

with col2:
    tahun = st.radio("Pilihan Tahun", ['2018','2019','2020','2021'], horizontal=True)
    
    #variabel untuk menambah view data pada grafik, maks 17
    headtail = 10

    dict_tahun = {
        '2018':'2018',
        '2019':'2019',
        '2020':'2020',
        '2021':'2021'
    }
    df_bts_ratio = pd.concat([df_jumlah_desa['Provinsi'], df_bts_total[tahun]/df_jumlah_desa[tahun]],axis=1, keys=['Provinsi',tahun]).sort_values(by=[tahun], ascending=False)
    df_efektivitas_sinyal = pd.concat([df_jumlah_desa['Provinsi'], (df_bts_sinyal_kuat[tahun]+df_nonbts_sinyal_kuat[tahun])/df_jumlah_desa[tahun]],axis=1, keys=['Provinsi',tahun]).sort_values(by=[tahun], ascending=False)

    bts_efektivitas_bar = alt.Chart(pd.concat([df_efektivitas_sinyal.head(headtail),df_efektivitas_sinyal.tail(headtail)])).mark_bar().encode(
    #bts_efektivitas_bar = alt.Chart(df_efektivitas_sinyal).mark_bar().encode(
        alt.X(tahun, title='Efektivitas'),
        alt.Y('Provinsi', title='Provinsi').sort('-x')
    ).properties(
        title='Cakupan Sinyal Efektif Tiap Provinsi'
    )
    st.altair_chart(bts_efektivitas_bar,use_container_width=True)

    bts_ratio_bar = alt.Chart(pd.concat([df_bts_ratio.head(headtail),df_bts_ratio.tail(headtail)])).mark_bar().encode(
    #bts_ratio_bar = alt.Chart(df_bts_ratio).mark_bar().encode(
        alt.X(tahun, title='Rasio'),
        alt.Y('Provinsi', title='Provinsi').sort('-x')
    ).properties(
        title='Rasio Desa/Kelurahan Terpasang BTS Dibanding Jumlah Desa/Kelurahan Pada Satu Provinsi'
    )
    st.altair_chart(bts_ratio_bar,use_container_width=True)

st.markdown('<br>', unsafe_allow_html=True)

st.header('Sugesti')
st.write("Berikut ini beberapa sugesti yang diajukan berdasarkan temuan pada analisis:")
st.markdown("- Untuk Papua, konflik bersenjata perlu dituntaskan dahulu sebelum pembangunan dapat dilanjutkan secara optimal.")
st.markdown("- Diperlukan analisis lebih lanjut tentang korelasi Jumlah BTS dan Cakupan Sinyal Efektif di mana analisis ini membutuhkan data lain seperti luas desa/kelurahan dan jumlah BTS yang terpasang pada tiap desa/kelurahan.")
st.markdown("- Untuk analisis kedepannya, diperlukan penyesuaian data karena terjadi pemekaran provinsi di tahun 2022 sehingga jumlah provinsi menjadi 38.")

st.markdown('''
<style>
[data-testid="stMarkdownContainer"] ul{
    list-style-position: inside;
}
</style>
''', unsafe_allow_html=True)