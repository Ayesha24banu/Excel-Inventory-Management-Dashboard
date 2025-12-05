import streamlit as st

# --- PAGE SETTINGS ---
st.set_page_config(
    page_title="Excel Inventory Management Dashboard",
    page_icon="📊",
    layout="wide"
)

# --- TITLE SECTION ---
st.title("📊 Excel Inventory Management Dashboard")
st.write("""
### A Professional Excel-based Inventory Analytics System  
This project demonstrates a fully interactive **inventory management dashboard** built in Excel using:
- PivotTables  
- PivotCharts  
- Slicers & Filters  
- Conditional Formatting  
- VBA Macros (Excel Automation)  

This Streamlit page showcases the dashboard for portfolio and demonstration purposes.
""")

# --- DOWNLOAD SECTION ---
st.subheader("📥 Download Excel Dashboard (.xlsm)")

with open("Inventory Management System .xlsm", "rb") as f:
    st.download_button(
        label="Download Excel Inventory Dashboard",
        data=f,
        file_name="Inventory-Management-System.xlsm",
        mime="application/vnd.ms-excel.sheet.macroEnabled.12"
    )

# --- SCREENSHOTS SECTION ---
st.subheader("📸 Dashboard Screenshots")

st.write("Below are the key pages from the Excel Inventory Dashboard:")

image_paths = [
    "assets/screenshot_1.png",
    "assets/screenshot_2.png",
    "assets/screenshot_3.png",
    "assets/screenshot_4.png",
    "assets/screenshot_5.png"
]

for img in image_paths:
    st.image(img, use_container_width=True)
    st.divider()

# --- FEATURES ---
st.subheader("🧰 Key Features")
st.markdown("""
- 📦 Tracks stock levels across warehouses  
- 📈 PivotCharts for real-time visualization  
- ⚠️ Low-stock alerts with conditional formatting  
- 🔄 Automated recalculation using macros  
- 🔍 Interactive Slicers for filtering by category & supplier  
- 📊 Reorder-level monitoring
""")

# --- OUTCOMES ---
st.subheader("📈 Outcomes & Impact")
st.markdown("""
- ⏳ Reduced manual report time by **30%**
- 📉 Eliminated errors caused by manual tracking
- 📦 Improved visibility of warehouse-wise stock
- 🤝 Data-backed inventory restocking decisions
""")

# --- FOOTER ---
st.info("Created by **Ayesha Banu** | Excel Dashboard Project | Portfolio Showcase")
