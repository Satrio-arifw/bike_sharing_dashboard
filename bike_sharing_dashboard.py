# Proyek Analisis Data - Bike Sharing Dataset

## 1. Pertanyaan Bisnis
- **Pertanyaan 1:** Bagaimana tren penggunaan sepeda berdasarkan waktu (harian dan jam)?
- **Pertanyaan 2:** Apa pengaruh kondisi cuaca terhadap jumlah pengguna sepeda?

---

## 2. Import Library/Packages
```python
# Import library yang dibutuhkan
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
```

> Pada langkah ini, kita memuat pustaka yang diperlukan untuk analisis data, visualisasi, dan pembuatan dashboard interaktif.

---

## 3. Data Wrangling
### 3.1 Gathering Data
```python
# Memuat dataset
path_day = "day.csv"
path_hour = "hour.csv"

data_day = pd.read_csv(path_day)
data_hour = pd.read_csv(path_hour)

# Menampilkan informasi awal dataset
print("Informasi Dataset Day:")
data_day.info()

print("\nInformasi Dataset Hour:")
data_hour.info()

# Menampilkan statistik deskriptif
print("\nStatistik Deskriptif Dataset Day:")
print(data_day.describe())

print("\nStatistik Deskriptif Dataset Hour:")
print(data_hour.describe())

# Melihat distribusi jumlah pengguna sepeda harian
sns.histplot(data_day['cnt'], kde=True, bins=30)
plt.title('Distribusi Penggunaan Sepeda Harian')
plt.xlabel('Total Pengguna')
plt.ylabel('Frekuensi')
plt.show()

# Melihat distribusi pengguna sepeda per jam
sns.histplot(data_hour['cnt'], kde=True, bins=30)
plt.title('Distribusi Penggunaan Sepeda per Jam')
plt.xlabel('Total Pengguna')
plt.ylabel('Frekuensi')
plt.show()
```
> Gathering data mencakup pemuatan data, inspeksi awal, dan eksplorasi statistik untuk memahami distribusi data. Distribusi membantu mengidentifikasi pola atau anomali dalam data pengguna sepeda.

---

### 3.2 Assessing Data
```python
# Mengecek nilai kosong
print("\nMissing Values in Day Dataset:")
print(data_day.isnull().sum())

print("\nMissing Values in Hour Dataset:")
print(data_hour.isnull().sum())

# Mendeteksi duplikasi
print("\nDuplicated Rows in Day Dataset:")
print(data_day.duplicated().sum())

print("\nDuplicated Rows in Hour Dataset:")
print(data_hour.duplicated().sum())
```
> Pada langkah ini, kita mencari nilai yang hilang dan duplikasi untuk memastikan kualitas data sebelum analisis lebih lanjut.

---

### 3.3 Cleaning Data
```python
# Menghapus nilai duplikat jika ada
data_day = data_day.drop_duplicates()
data_hour = data_hour.drop_duplicates()

# Menangani nilai kosong (jika ada)
data_day = data_day.dropna()
data_hour = data_hour.dropna()
```
> Data yang bersih adalah fondasi analisis yang akurat. Nilai kosong dan duplikasi dihapus untuk mencegah hasil yang bias.

---

## 4. Exploratory Data Analysis (EDA)
```python
# Distribusi total pengguna sepeda harian
sns.histplot(data_day['cnt'], kde=True, bins=30)
plt.title('Distribusi Penggunaan Sepeda Harian')
plt.xlabel('Total Pengguna')
plt.ylabel('Frekuensi')
plt.show()

# Distribusi pengguna sepeda per jam
sns.histplot(data_hour['cnt'], kde=True, bins=30)
plt.title('Distribusi Penggunaan Sepeda per Jam')
plt.xlabel('Total Pengguna')
plt.ylabel('Frekuensi')
plt.show()
```
> EDA bertujuan untuk mengeksplorasi data lebih dalam. Distribusi menunjukkan pola umum dalam jumlah pengguna sepeda.

---

## 5. Visualisasi dan Penjelasan (Explanatory Analysis)
### Pertanyaan 1: Tren Penggunaan Sepeda Berdasarkan Waktu
```python
plt.figure(figsize=(12, 6))
plt.plot(data_day['dteday'], data_day['cnt'], label='Total Users', color='blue')
plt.xlabel('Tanggal')
plt.ylabel('Total Pengguna')
plt.title('Tren Penggunaan Sepeda Harian')
plt.legend()
plt.show()
```

### Pertanyaan 2: Pengaruh Kondisi Cuaca
```python
sns.boxplot(x='weathersit', y='cnt', data=data_hour)
plt.title('Pengaruh Kondisi Cuaca terhadap Jumlah Pengguna Sepeda')
plt.xlabel('Kondisi Cuaca')
plt.ylabel('Total Pengguna')
plt.show()
```
> Visualisasi ini menjawab pertanyaan bisnis yang telah dirumuskan, memberikan wawasan mengenai pola waktu dan dampak cuaca terhadap pengguna sepeda.

---

## 6. Analisis Lanjutan: Clustering
#### Pengelompokan Berdasarkan Jam Sibuk
```python
bins_time = [0, 6, 10, 16, 20, 24]
labels_time = ['Dini Hari', 'Pagi', 'Siang', 'Sore', 'Malam']
data_hour['time_category'] = pd.cut(data_hour['hr'], bins=bins_time, labels=labels_time, right=False)

# Visualisasi rata-rata pengguna berdasarkan kategori waktu
avg_users_time = data_hour.groupby('time_category')['cnt'].mean().reset_index()
plt.bar(avg_users_time['time_category'], avg_users_time['cnt'], color='skyblue')
plt.title('Rata-Rata Pengguna Berdasarkan Kategori Waktu')
plt.xlabel('Kategori Waktu')
plt.ylabel('Rata-Rata Pengguna')
plt.show()
```

#### Pengelompokan Berdasarkan Jumlah Pengguna
```python
bins_user = [0, 100, 500, 1000, 5000]
labels_user = ['Rendah', 'Sedang', 'Tinggi', 'Sangat Tinggi']
data_hour['user_category'] = pd.cut(data_hour['cnt'], bins=bins_user, labels=labels_user, right=False)

# Visualisasi distribusi kategori jumlah pengguna
sns.countplot(x='user_category', data=data_hour, palette='Set2')
plt.title('Distribusi Kategori Jumlah Pengguna')
plt.xlabel('Kategori Pengguna')
plt.ylabel('Frekuensi')
plt.show()
```
> Clustering manual membantu mengidentifikasi pola penggunaan sepeda berdasarkan waktu dan jumlah pengguna.

---

## 7. Kesimpulan
1. Penggunaan sepeda harian menunjukkan pola musiman dan waktu sibuk.
2. Cuaca memiliki pengaruh signifikan pada jumlah pengguna sepeda.
3. Analisis clustering menunjukkan waktu sibuk adalah pagi dan sore, dengan mayoritas pengguna dalam kategori "Sedang" dan "Tinggi".

---

## 8. Deploy Dashboard ke Streamlit
```python
st.title("Dashboard Analisis Data - Bike Sharing Dataset")
st.sidebar.header("Navigasi")
menu = st.sidebar.selectbox("Pilih Analisis", ["Penggunaan Sepeda Harian", "Penggunaan Sepeda per Jam", "Clustering"])

if menu == "Penggunaan Sepeda Harian":
    st.header("Penggunaan Sepeda Berdasarkan Hari")
    st.line_chart(data_day[['cnt']])

elif menu == "Penggunaan Sepeda per Jam":
    st.header("Penggunaan Sepeda Berdasarkan Jam")
    fig, ax = plt.subplots()
    sns.lineplot(x='hr', y='cnt', data=data_hour, hue='weekday', ci=None, ax=ax)
    ax.set_title("Penggunaan Sepeda per Jam")
    ax.set_xlabel("Jam")
    ax.set_ylabel("Total Pengguna")
    st.pyplot(fig)

elif menu == "Clustering":
    st.header("Hasil Clustering")
    st.subheader("Pengelompokan Berdasarkan Jam Sibuk")
    avg_users_time = data_hour.groupby('time_category')['cnt'].mean().reset_index()
    fig, ax = plt.subplots()
    ax.bar(avg_users_time['time_category'], avg_users_time['cnt'], color='skyblue')
    ax.set_title('Rata-Rata Pengguna Berdasarkan Kategori Waktu')
    ax.set_xlabel('Kategori Waktu')
    ax.set_ylabel('Rata-Rata Pengguna')
    st.pyplot(fig)

    st.subheader("Pengelompokan Berdasarkan Jumlah Pengguna")
    fig, ax = plt.subplots()
    sns.countplot(x='user_category', data=data_hour, palette='Set2', ax=ax)
    ax.set_title("Distribusi Kategori Jumlah Pengguna")
    ax.set_xlabel("Kategori Pengguna")
    ax.set_ylabel("Frekuensi")
    st.pyplot(fig)

st.sidebar.markdown("---")
st.sidebar.text("© 2025 Bike Sharing Dashboard")
```
> Deploy dashboard ke Streamlit Cloud dengan perintah `streamlit run` agar dapat diakses publik. Panduan deployment dapat disertakan dalam README.
