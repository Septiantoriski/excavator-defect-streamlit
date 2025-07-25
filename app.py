import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Analisa Barang Defect - Excavator Unit")
st.write("Project by Riski")


uploaded_file = st.file_uploader("Upload File Defect (CSV)", type="csv")
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("📊 Data Preview:")
    st.dataframe(df)

    st.write("📈 Jumlah Defect per Kategori:")
    st.bar_chart(df['kategori_defect'].value_counts())

    st.write("💥 Analisa Defect Berdasarkan Komponen:")
    fig, ax = plt.subplots()
    sns.countplot(data=df, y='komponen', hue='kategori_defect', ax=ax)
    st.pyplot(fig)
