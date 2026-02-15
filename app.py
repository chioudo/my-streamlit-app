
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")

# 主標題
st.title("天文科展網站")

# 導覽頁
st.sidebar.title("觀看各類圖片")

# 創建 1 到 15 的子分頁選項
pages = [f"分頁 {i}" for i in range(1, 16)]
selected_page = st.sidebar.radio("選擇分頁", pages)

# 根據選擇顯示內容
if selected_page:
    st.header(selected_page)
    # 這裡將是您嵌入 HTML 內容的地方
    st.write(f"這裡將顯示 {selected_page} 的 HTML 內容。")
    
    # 當您提供 HTML 內容時，可以像這樣使用：
    # if selected_page == "分頁 1":
    #     html_content_page1 = "<h1>這是分頁 1 的內容</h1>"
    #     components.html(html_content_page1, height=600)
    # elif selected_page == "分頁 2":
    #     html_content_page2 = "<p>這是分頁 2 的內容。</p>"
    #     components.html(html_content_page2, height=600)
    # ... (依此類推，為每個分頁添加您的 HTML 內容)
