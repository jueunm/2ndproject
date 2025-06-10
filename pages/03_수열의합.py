import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go # 3D 시각화 고려 시

st.set_page_config(layout="wide") # 페이지 전체 너비 사용

st.title("자연수의 거듭제곱의 합 시각화")

st.sidebar.header("설정")
selected_formula = st.sidebar.radio(
    "어떤 공식을 시각화하시겠습니까?",
    ("1의 합", "제곱의 합", "세제곱의 합")
)
n = st.sidebar.slider("n 값 선택", 1, 10, 5) # n 값 조절 슬라이더

st.write(f"## {selected_formula} 시각화 ($n = {n}$)")

if selected_formula == "1의 합":
    # 1의 합 시각화 코드
    st.write("### $\sum_{k=1}^{n} k = \\frac{n(n+1)}{2}$")
    st.write("블록 쌓기를 통해 삼각형을 만들고, 이를 복제하여 직사각형을 만드는 과정을 보여줍니다.")

    # 예시: 간단한 블록 시각화 (더 개선 필요)
    for i in range(1, n + 1):
        st.write("🟪" * i)
    
    st.write(f"총 블록 수: {sum(range(1, n + 1))}")
    st.write(f"공식에 의한 값: {n * (n + 1) // 2}")

    # 추가적인 시각화 아이디어: Matplotlib으로 사각형 그리기
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_aspect('equal', adjustable='box')
    ax.set_xlim(0, n + 1)
    ax.set_ylim(0, n + 1)
    ax.set_xticks([])
    ax.set_yticks([])

    current_x = 0
    for i in range(1, n + 1):
        for j in range(i):
            rect = plt.Rectangle((current_x + j, i - 1), 1, 1, facecolor='blue', edgecolor='black')
            ax.add_patch(rect)
    st.pyplot(fig)


elif selected_formula == "제곱의 합":
    # 제곱의 합 시각화 코드
    st.write("### $\sum_{k=1}^{n} k^2 = \\frac{n(n+1)(2n+1)}{6}$")
    st.write("정사각형 블록을 쌓아 피라미드 형태를 만들고, 세 개의 피라미드가 직육면체를 이루는 것을 보여줍니다.")

    # 2D 평면에서 시각적으로 유추할 수 있는 방법 (개념 설명)
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/e/e6/Sum_of_squares.svg/300px-Sum_of_squares.svg.png", 
             caption="제곱의 합 시각화 (위키백과 예시)")
    st.write("위 그림처럼 세 개의 피라미드를 조합하여 직육면체를 만들고, 이를 6으로 나누는 과정을 설명합니다.")
    st.markdown("""
    * **첫 번째 피라미드:** $n$개 층으로 이루어진 피라미드 (각 층은 $k \times k$ 정사각형)
    * **두 번째 피라미드:** 첫 번째 피라미드와 동일
    * **세 번째 피라미드:** 첫 번째 피라미드의 블록을 회전하거나 재배치하여 직육면체를 만듭니다.
    """)
    st.write(f"총 블록 수: {sum(k**2 for k in range(1, n + 1))}")
    st.write(f"공식에 의한 값: {n * (n + 1) * (2 * n + 1) // 6}")

    # Plotly 3D 시각화는 더 복잡하므로, 일단 개념 설명과 2D 시각화에 집중하는 것이 좋습니다.
    # 예시: 3D 블록을 구현하려면 복잡한 계산 필요 (여기서는 생략)


elif selected_formula == "세제곱의 합":
    # 세제곱의 합 시각화 코드
    st.write("### $\sum_{k=1}^{n} k^3 = \\left(\\frac{n(n+1)}{2}\\right)^2$")
    st.write("각 $k^3$을 정육면체로 표현하고, 이들을 조합하여 큰 정사각형의 형태로 만드는 것을 보여줍니다.")

    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/Sum_of_cubes.svg/300px-Sum_of_cubes.svg.png",
             caption="세제곱의 합 시각화 (위키백과 예시)")
    st.write("위 그림처럼 $1^3, 2^3, \dots, n^3$ 블록들을 조합하면 $\left(\\frac{n(n+1)}{2}\\right)$을 한 변으로 하는 큰 정사각형을 만들 수 있습니다.")
    st.write(f"총 블록 수: {sum(k**3 for k in range(1, n + 1))}")
    st.write(f"공식에 의한 값: {(n * (n + 1) // 2)**2}")

    # Plotly 3D 시각화는 더 복잡하므로, 일단 개념 설명과 2D 시각화에 집중하는 것이 좋습니다.
