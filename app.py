
import streamlit as st
import streamlit.components.v1 as components
import os

st.set_page_config(layout="wide")

# 主標題
st.title("天文科展網站")

# HTML 檔案路徑與對應的顯示名稱
html_files = {
    "50PC_density": "/content/50PC_density.html",
    "10PC_hist_filtered": "/content/10PC_hist_filtered.html",
    "50PC_3D": "/content/50PC_3D.html",
    "20PC_3D": "/content/20PC_3D.html",
    "50PC_hist_filtered": "/content/50PC_hist_filtered.html",
    "10PC_stars": "/content/10PC_stars.html",
    "10PC_HR": "/content/10PC_HR.html",
    "20PC_hist_filtered": "/content/20PC_hist_filtered.html",
    "20PC_HR": "/content/20PC_HR.html",
    "50PC_luminosity": "/content/50PC_luminosity.html",
    "10PC_luminosity": "/content/10PC_luminosity.html",
    "20PC_density": "/content/20PC_density.html",
    "10PC_3D": "/content/10PC_3D.html",
    "10PC_density": "/content/10PC_density.html",
    "50PC_stars": "/content/50PC_stars.html",
    "20PC_luminosity": "/content/20PC_luminosity.html",
    "50PC_HR": "/content/50PC_HR.html",
}

# 導覽頁
st.sidebar.title("觀看各類圖片")

# 創建子分頁選項
pages = list(html_files.keys())
selected_page = st.sidebar.radio("選擇分頁", pages)

# 根據選擇顯示內容
if selected_page:
    st.header(selected_page)
    file_path = html_files[selected_page]
    
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            html_content = f.read()
        components.html(html_content, height=700, scrolling=True) # 使用 height 和 scrolling 參數確保內容正常顯示
    else:
        st.error(f"錯誤：找不到檔案 {file_path}")

