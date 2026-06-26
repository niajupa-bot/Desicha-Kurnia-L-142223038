import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import io

# Konfigurasi halaman
st.set_page_config(
    page_title="Data Mining Pelanggan",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Dashboard Data Mining Pelanggan")

# Data langsung embed (tidak perlu upload)
data_csv = """ID Pelanggan,Nama,Jenis Kelamin,Pendapatan,Produk,Harga,Jumlah,Total,Tingkat Kepuasan
1,Arif,1,600000,A,100000,4,400000,2
2,Dian,2,1200000,D,250000,4,1000000,2
3,Dinda,2,950000,D,250000,3,750000,3
4,Fajar,1,400000,A,100000,2,200000,3
5,Ika,2,1200000,D,250000,4,1000000,2
6,Ilham,1,800000,B,150000,4,600000,3
7,Indra,1,950000,B,150000,5,750000,1
8,Kartika,2,1100000,E,300000,3,900000,3
9,Lestari,2,800000,E,300000,2,600000,1
10,Lia,2,1700000,E,300000,5,1500000,1
11,Maria,2,600000,A,100000,4,400000,3
12,Maya,2,950000,B,150000,5,750000,3
13,Mila,2,400000,C,200000,1,200000,2
14,Nurul,2,6450000,D,250000,5,1250000,1
15,Retno,2,1000000,C,200000,4,800000,2
16,Rini,2,800000,B,150000,4,600000,1
17,Rizki,1,1200000,C,200000,5,1000000,3
18,Sari,2,700000,D,250000,2,500000,1
19,Tyas,2,600000,A,100000,4,400000,3
20,Wahyu,1,800000,C,200000,3,600000,1"""

df = pd.read_csv(io.StringIO(data_csv))
df.columns = df.columns.str.strip()

# Preview Data
st.subheader("📋 Preview Dataset")
st.dataframe(df.head())

# Informasi Dataset
st.subheader("📑 Informasi Dataset")
st.write(f"Jumlah Baris : {df.shape[0]}")
st.write(f"Jumlah Kolom : {df.shape[1]}")

# Menampilkan nama kolom
st.subheader("📝 Nama Kolom")
st.write(df.columns.tolist())

# Statistik Deskriptif
st.subheader("📈 Statistik Deskriptif")
st.dataframe(df.describe())

# KPI
st.subheader("📊 Ringkasan Data")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total Pendapatan", f"Rp {df['Pendapatan'].sum():,.0f}")
with col2:
    st.metric("Total Penjualan", f"Rp {df['Total'].sum():,.0f}")
with col3:
    st.metric("Jumlah Pelanggan", df.shape[0])

# Histogram Pendapatan
st.subheader("💰 Distribusi Pendapatan")
fig, ax = plt.subplots()
ax.hist(df["Pendapatan"], bins=10)
ax.set_xlabel("Pendapatan")
ax.set_ylabel("Jumlah Pelanggan")
st.pyplot(fig)

# Grafik Produk
st.subheader("🛍 Jumlah Produk Terjual")
produk_count = df["Produk"].value_counts()
st.bar_chart(produk_count)

# Grafik Jenis Kelamin
st.subheader("👨‍🦰👩‍🦰 Distribusi Jenis Kelamin")
gender_count = df["Jenis Kelamin"].value_counts()
st.bar_chart(gender_count)

# Tingkat Kepuasan
st.subheader("⭐ Tingkat Kepuasan Pelanggan")
kepuasan = df["Tingkat Kepuasan"].value_counts()
st.bar_chart(kepuasan)

# Data Lengkap
st.subheader("📄 Data Lengkap")
st.dataframe(df)
