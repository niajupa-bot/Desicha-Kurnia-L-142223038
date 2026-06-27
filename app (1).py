import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# --------------------------------------------------
# Konfigurasi Halaman
# --------------------------------------------------
st.set_page_config(
    page_title="Dashboard Data Mining Pelanggan",
    page_icon="📊",
    layout="wide"
)

# --------------------------------------------------
# Fungsi Rupiah
# --------------------------------------------------
def rupiah(x):
    return f"Rp {x:,.0f}".replace(",", ".")

# --------------------------------------------------
# Load Data
# --------------------------------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("Customers.csv")
    df.columns = df.columns.str.strip()

    if "Jenis Kelamin" in df.columns:
        df["Jenis Kelamin"] = df["Jenis Kelamin"].replace({
            1: "Laki-laki",
            2: "Perempuan"
        })

    return df

df = load_data()

# --------------------------------------------------
# Sidebar
# --------------------------------------------------
st.sidebar.title("📚 Menu")

menu = st.sidebar.radio(
    "Pilih Halaman",
    [
        "Dashboard",
        "Dataset",
        "Statistik",
        "Visualisasi",
        "Kesimpulan"
    ]
)

# ==================================================
# DASHBOARD
# ==================================================
if menu == "Dashboard":

    st.title("📊 Dashboard Data Mining Pelanggan")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Jumlah Pelanggan",
            len(df)
        )

    with col2:
        st.metric(
            "Total Pendapatan",
            rupiah(df["Pendapatan"].sum())
        )

    with col3:
        st.metric(
            "Total Penjualan",
            rupiah(df["Total"].sum())
        )

    st.markdown("---")

    st.subheader("Preview Dataset")

    st.dataframe(df.head())

# ==================================================
# DATASET
# ==================================================
elif menu == "Dataset":

    st.title("📋 Dataset")

    produk = st.selectbox(
        "Filter Produk",
        ["Semua"] + sorted(df["Produk"].unique())
    )

    if produk == "Semua":
        tampil = df
    else:
        tampil = df[df["Produk"] == produk]

    st.dataframe(tampil)

    csv = tampil.to_csv(index=False).encode("utf-8")

    st.download_button(
        "⬇ Download Dataset",
        csv,
        "Customers.csv",
        "text/csv"
    )

# ==================================================
# STATISTIK
# ==================================================
elif menu == "Statistik":

    st.title("📈 Statistik Deskriptif")

    st.write("Jumlah Baris :", df.shape[0])
    st.write("Jumlah Kolom :", df.shape[1])

    st.write("Nama Kolom")

    st.write(df.columns.tolist())

    st.dataframe(df.describe())

# ==================================================
# VISUALISASI
# ==================================================
elif menu == "Visualisasi":

    st.title("📉 Visualisasi Data")

    # Histogram
    st.subheader("Distribusi Pendapatan")

    fig, ax = plt.subplots(figsize=(8,4))

    ax.hist(df["Pendapatan"], bins=8)

    ax.set_xlabel("Pendapatan")

    ax.set_ylabel("Jumlah")

    st.pyplot(fig)

    # Produk
    st.subheader("Jumlah Produk Terjual")

    produk = df["Produk"].value_counts()

    st.bar_chart(produk)

    # Jenis Kelamin
    st.subheader("Distribusi Jenis Kelamin")

    gender = df["Jenis Kelamin"].value_counts()

    st.bar_chart(gender)

    # Kepuasan
    st.subheader("Tingkat Kepuasan")

    puas = df["Tingkat Kepuasan"].value_counts()

    st.bar_chart(puas)

    # Pie Chart Produk

    st.subheader("Persentase Produk")

    fig2, ax2 = plt.subplots()

    ax2.pie(
        produk,
        labels=produk.index,
        autopct="%1.1f%%",
        startangle=90
    )

    ax2.axis("equal")

    st.pyplot(fig2)

# ==================================================
# KESIMPULAN
# ==================================================
else:

    st.title("📄 Kesimpulan")

    st.success(f"""
Jumlah pelanggan sebanyak **{len(df)}** orang.

Total pendapatan pelanggan sebesar **{rupiah(df['Pendapatan'].sum())}**.

Total transaksi penjualan sebesar **{rupiah(df['Total'].sum())}**.

Produk yang paling banyak dibeli adalah **{df['Produk'].mode()[0]}**.

Rata-rata pendapatan pelanggan sebesar **{rupiah(df['Pendapatan'].mean())}**.

Dashboard ini menunjukkan distribusi pelanggan berdasarkan pendapatan, jenis kelamin, produk yang dibeli, serta tingkat kepuasan pelanggan sehingga dapat membantu proses analisis data dalam pengambilan keputusan.
""")
