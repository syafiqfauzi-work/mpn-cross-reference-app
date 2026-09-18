import streamlit as st
import pandas as pd

# Konfigurasi muka surat
st.set_page_config(
    page_title="MPN Cross-Reference App",
    page_icon="🔍",
    layout="wide"
)

# Tajuk Aplikasi
st.title("🔍 MPN Cross-Reference & Alternate Search")
st.markdown("Find *Exact Match* & *Almost Same* alternative part.")

# Kotak Carian MPN
mpn_input = st.text_input("Input Manufacturer Part Number (MPN):", placeholder="Example: LM358N")

# Button Search
if st.button("Find", type="primary"):
    if mpn_input:
        st.info(f"Scouring the web for parts: **{mpn_input}**...")
        
        # Mock Data untuk Exact Match
        exact_match_data = pd.DataFrame({
            "Manufacturer": ["Texas Instruments", "STMicroelectronics"],
            "Part Number": [mpn_input, mpn_input + "-ST"],
            "Package": ["SOIC-8", "SOIC-8"],
            "Status": ["Active", "Active"]
        })
        
        # Mock Data untuk Almost Same
        almost_same_data = pd.DataFrame({
            "Manufacturer": ["ON Semiconductor", "Microchip"],
            "Alternative Part": ["MC1458", "MCP602"],
            "Similarity": ["95% (Pin-to-Pin)", "90% (Similar Specs)"],
            "Package": ["SOIC-8", "SOIC-8"]
        })
        
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
