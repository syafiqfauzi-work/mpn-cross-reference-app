import streamlit as st

# Konfigurasi muka surat
st.set_page_config(
    page_title="MPN Cross-Reference App",
    page_icon="🔍",
    layout="wide"
)

# Tajuk Aplikasi
st.title("🔍 MPN Cross-Reference & Alternate Search")
st.markdown("Cari *Exact Match* dan *Almost Same* part alternatif dengan pantas tanpa perlu buka banyak website.")

# Kotak Carian MPN
mpn_input = st.text_input("Masukkan Manufacturer Part Number (MPN):", placeholder="Contoh: LM358N")

# Button Search
if st.button("Cari Alternatif", type="primary"):
    if mpn_input:
        st.info( sedang mencari maklumat untuk MPN: **{mpn_input}**...)
        
        # Bahagian keputusan (kita akan masukkan logic scraping/data nanti)
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("🎯 Exact Match")
            st.write("Keputusan untuk exact match akan dipaparkan di sini.")
            
        with col2:
            st.subheader("🔄 Almost Same (Alternatif)")
            st.write("Keputusan untuk part hampir serupa akan dipaparkan di sini.")
            
    else:
        st.warning("Sila masukkan MPN terlebih dahulu!")
