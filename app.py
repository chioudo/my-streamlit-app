
import streamlit as st
import streamlit.components.v1 as components
import os

st.set_page_config(layout="wide")

# 主標題
st.title("天文科展網站")

# HTML 檔案路徑與對應的顯示名稱 (移除 /content/ 前綴)
html_files = {
    "50PC恆星密度3D體積圖": "50PC_density.html",
    "10PC次數分布圖": "10PC_hist_filtered.html",
    "3D圖(50PC)": "50PC_3D.html",
    "3D圖(20PC)": "20PC_3D.html",
    "50PC次數分布圖": "50PC_hist_filtered.html",
    "10PC恆星密度3D體積圖": "10PC_stars.html",
    "10PC赫羅圖": "10PC_HR.html",
    "20PC次數分布圖": "20PC_hist_filtered.html",
    "20PC赫羅圖": "20PC_HR.html",
    "50PC光度密度3D體積圖": "50PC_luminosity.html",
    "10PC光度密度3D體積圖": "10PC_luminosity.html",
    "20PC恆星密度3D體積圖": "20PC_density.html",
    "3D圖(10PC)": "10PC_3D.html",
    "10PC恆星密度3D體積圖": "10PC_density.html",
    "50PC恆星密度3D體積圖": "50PC_stars.html",
    "10PC光度密度3D體積圖": "20PC_luminosity.html",
    "50PC赫羅圖": "50PC_HR.html",
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
    
    # 在 Streamlit Cloud 環境中，檔案通常在應用程式的根目錄或相對路徑下
    # 這裡假設 HTML 檔案與 app.py 位於同一目錄
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            html_content = f.read()
        components.html(html_content, height=700, scrolling=True) # 使用 height 和 scrolling 參數確保內容正常顯示
    else:
        st.error(f"錯誤：找不到檔案 {file_path}。請確認它已上傳到 GitHub 儲存庫的正確位置。")

