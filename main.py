import streamlit as st
from PIL import Image, ImageOps
import numpy as np
import matplotlib.pyplot as plt

st.title("은하 사진으로 추정한 성간물질 온도 분포 시각화")

# 이미지 업로드
uploaded_file = st.file_uploader("은하 이미지를 업로드하세요 (FITS)", type=["FITS"])

if uploaded_file:
    # 원본 이미지 열기
    image = Image.open(uploaded_file)
    st.image(image, caption='업로드한 은하 이미지', use_column_width=True)

    # 흑백(밝기) 이미지로 변환
    gray_image = ImageOps.grayscale(image)
    gray_array = np.array(gray_image)

    # 밝기를 임의의 온도로 변환 (예: 0~255 → 1000~10000K 범위 매핑)
    temp_array = 1000 + (gray_array / 255) * 9000

    st.write("🔍 아래는 추정된 온도 분포입니다 (단위: K)")

    # 온도 분포 히트맵 출력
    fig, ax = plt.subplots()
    temp_plot = ax.imshow(temp_array, cmap='plasma')
    plt.colorbar(temp_plot, label="온도 (K)")
    st.pyplot(fig)

    # 간단한 평균 온도 표시
    avg_temp = np.mean(temp_array)
    st.write(f"📊 이미지 전체의 평균 추정 온도: **{avg_temp:.1f} K**")

    st.markdown("""
    > ❗ 주의: 이 온도는 밝기를 바탕으로 단순 추정한 값으로,  
    > 실제 성간물질의 물리적 온도와는 차이가 있습니다.
    """)
