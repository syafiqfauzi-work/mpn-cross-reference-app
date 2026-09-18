import streamlit as st
import pandas as pd

# Konfigurasi muka surat
st.set_page_config(
    page_title="MPN Cross-Reference App",
    page_icon="🔍",
    layout="wide"
)

# Fungsi carian (Tempat kita letak logic API atau Scraper nanti)
def search_mpn(mpn):
    # Mock Data untuk Exact Match
    exact_df = pd.DataFrame({
        "Manufacturer": ["Texas Instruments", "STMicroelectronics"],
        "Part Number": [mpn, mpn + "-ST"],
        "Package": ["SOIC-8", "SOIC-8"],
        "Status": ["Active", "Active"]
    })
    
    # Mock Data untuk Almost Same
    almost_df = pd.DataFrame({
        "Manufacturer": ["ON Semiconductor", "Microchip"],
        "Alternative Part": ["MC1458", "MCP602"],
        "Similarity": ["95% (Pin-to-Pin)", "90% (Similar Specs)"],
        "Package": ["SOIC-8", "SOIC-8"]
    })
    
    return exact_df, almost_df

# Tajuk Aplikasi
st.title("🔍 MPN Cross-Reference & Alternate Search")
st.markdown("Find *Exact Match* & *Almost Same* alternative part.")

# Kotak Carian MPN
mpn_input = st.text_input("Input Manufacturer Part Number (MPN):", placeholder="Example: LM358N")

# Button Search
if st.button("Find", type="primary"):
    if mpn_input:
        with st.spinner(f"Scouring the web for parts: **{mpn_input}**..."):
            # Panggil fungsi carian
            exact_match_data, almost_same_data = search_mpn(mpn_input.strip())
        
        # Bahagian keputusan
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("🎯 Exact Match")
            st.dataframe(exact_match_data, hide_index=True)
            
        with col2:
            st.subheader("🔄 Almost Same")
            st.dataframe(almost_same_data, hide_index=True)
            
    else:
        st.warning("Please enter MPN first!")
