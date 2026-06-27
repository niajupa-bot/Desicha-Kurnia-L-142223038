import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ===========================================
# Konfigurasi Halaman
# ===========================================
st.set_page_config(
    page_title="Dashboard Data Mining Pelanggan",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Dashboard Data Mining Pelanggan")

# ===========================================
# Load Dataset
# ===========================================
@st.cache_data
def load_data():
    df = pd.read_csv("Customers.csv")
    df.columns = df.columns.str.strip()
    return df

df = load_data()

# ===========================================
# Sidebar
# ===========================================
menu = st.sidebar.selectbox(
    "Pilih Menu",
    [
        "Dashboard",
        "Dataset",
        "Statistik",
        "Visualisasi"
    ]
)

# ===========================================
# Dashboard
# ===========================================
if menu == "Dashboard":

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Jumlah Pelanggan",
        len(df)
    )

    col2.metric(
        "Rata-rata Pendapatan",
        f"${df['Annual Income ($)'].mean():.2f}"
    )

    col3.metric(
        "Rata-rata Spending Score",
        f"{df['Spending Score (1-100)'].mean():.2f}"
    )

    st.markdown("---")

    st.subheader("Preview Dataset")

    st.dataframe(df.head())

# ===========================================
# Dataset
# ===========================================
elif menu == "Dataset":

    st.subheader("Data Lengkap")

    gender = st.selectbox(
        "Filter Gender",
        ["Semua"] + list(df["Gender"].unique())
    )

    if gender == "Semua":
        tampil = df
    else:
        tampil = df[df["Gender"] == gender]

    st.dataframe(tampil)

# ===========================================
# Statistik
# ===========================================
elif menu == "Statistik":

    st.subheader("Informasi Dataset")

    st.write("Jumlah Baris :", df.shape[0])

    st.write("Jumlah Kolom :", df.shape[1])

    st.write("Nama Kolom")

    st.write(df.columns.tolist())

    st.subheader("Statistik Deskriptif")

    st.dataframe(df.describe())

# ===========================================
# Visualisasi
# ===========================================
else:

    st.subheader("Distribusi Gender")

    gender = df["Gender"].value_counts()

    st.bar_chart(gender)

    st.subheader("Distribusi Umur")

    fig, ax = plt.subplots()

    ax.hist(df["Age"], bins=10)

    ax.set_xlabel("Age")

    ax.set_ylabel("Jumlah")

    st.pyplot(fig)

    st.subheader("Distribusi Pendapatan Tahunan")

    fig2, ax2 = plt.subplots()

    ax2.hist(df["Annual Income ($)"], bins=10)

    ax2.set_xlabel("Annual Income ($)")

    st.pyplot(fig2)

    st.subheader("Rata-rata Pendapatan Berdasarkan Gender")

    income = df.groupby("Gender")["Annual Income ($)"].mean()

    st.bar_chart(income)

    st.subheader("Rata-rata Spending Score Berdasarkan Gender")

    spending = df.groupby("Gender")["Spending Score (1-100)"].mean()

    st.bar_chart(spending)

    st.subheader("Distribusi Profesi")

    profesi = df["Profession"].value_counts()

    st.bar_chart(profesi)

    st.subheader("Distribusi Family Size")

    family = df["Family Size"].value_counts().sort_index()

    st.bar_chart(family)
