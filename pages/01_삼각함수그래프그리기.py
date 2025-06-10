import streamlit as st
import numpy as np
import plotly.graph_objects as go

st.set_page_config(layout="wide") # 페이지 전체 너비 사용

# 세션 상태 초기화 (처음에만 실행)
if 'sin_opinion' not in st.session_state:
    st.session_state.sin_opinion = ""
if 'cos_opinion' not in st.session_state:
    st.session_state.cos_opinion = ""
if 'tan_opinion' not in st.session_state:
    st.session_state.tan_opinion = ""

st.title("삼각함수 그래프 그리기 📊")

st.write("""
이 활동에서는 $\sin$, $\cos$, $\tan$ 함수 중 하나를 선택하고,
$y = a \sin(bx)$, $y = a \cos(bx)$, $y = a \tan(bx)$ 형태의 그래프에서
**$a$와 $b$ 값을 직접 입력**하여 그래프가 어떻게 변하는지 탐색할 수 있습니다.

충분히 탐색한 후 **'나의 탐구 결과' 탭**으로 이동하여 $a$와 $b$의 역할에 대한 여러분의 생각을 정리해 보세요!
""")

# 탭 메뉴 생성
tab1, tab2 = st.tabs(["그래프 탐색", "나의 탐구 결과"])

with tab1:
    st.header("그래프 탐색하기")

    # 1. sin, cos, tan 중 그래프 하나 선택하기
    st.sidebar.header("함수 선택 및 파라미터 설정")
    function_type = st.sidebar.radio(
        "어떤 함수의 그래프를 그려볼까요?",
        ('sin', 'cos', 'tan')
    )

    # 2. y=asinbx 형태에서 a, b 값 입력받기
    col1, col2 = st.sidebar.columns(2)
    with col1:
        a_value = st.number_input("a 값 입력", value=1.0, format="%.2f", step=0.1, key="a_input")
    with col2:
        b_value = st.number_input("b 값 입력", value=1.0, format="%.2f", step=0.1, key="b_input")

    st.sidebar.markdown("---")

    # 3. 학생들이 작성한 a,b 값에 따른 그래프 보여주기
    st.subheader(f"선택된 함수: {function_type.upper()} 그래프")

    x = np.linspace(-2 * np.pi, 2 * np.pi, 500) # -2π 부터 2π 까지 500개의 점 생성

    if function_type == 'sin':
        y = a_value * np.sin(b_value * x)
        equation = f"y = {a_value:.2f} sin({b_value:.2f}x)"
    elif function_type == 'cos':
        y = a_value * np.cos(b_value * x)
        equation = f"y = {a_value:.2f} cos({b_value:.2f}x)"
    elif function_type == 'tan':
        y = a_value * np.tan(b_value * x)
        equation = f"y = {a_value:.2f} tan({b_value:.2f}x)"
        y[y > 10] = np.nan # 너무 큰 값은 nan으로 처리하여 그래프에서 제외
        y[y < -10] = np.nan # 너무 작은 값도 nan으로 처리

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name=equation))

    fig.update_layout(
        title=f"**{equation}**",
        xaxis_title="x",
        yaxis_title="y",
        yaxis_range=[-5, 5] if function_type != 'tan' else [-10, 10] # tan은 범위 넓게
    )
    st.plotly_chart(fig, use_container_width=True)

with tab2:
    st.header("나의 탐구 결과📝")
    st.write("그래프를 충분히 탐색한 후, 아래 질문에 대한 여러분의 생각을 정리하여 작성해 주세요.")

    # sin 함수에 대한 탐구 결과
    st.subheader("1. $y = a \sin(bx)$ 에서 $a$와 $b$의 역할은 무엇일까요?")
    st.session_state.sin_opinion = st.text_area(
        "$\sin$ 함수에 대한 여러분의 의견을 자유롭게 적어주세요.",
        value=st.session_state.sin_opinion, # 세션 상태 값 불러오기
        height=150,
        key="sin_opinion_box"
    )

    st.markdown("---")

    # cos 함수에 대한 탐구 결과
    st.subheader("2. $y = a \cos(bx)$ 에서 $a$와 $b$의 역할은 무엇일까요?")
    st.session_state.cos_opinion = st.text_area(
        "$\cos$ 함수에 대한 여러분의 의견을 자유롭게 적어주세요.",
        value=st.session_state.cos_opinion, # 세션 상태 값 불러오기
        height=150,
        key="cos_opinion_box"
    )

    st.markdown("---")

    # tan 함수에 대한 탐구 결과
    st.subheader("3. $y = a \tan(bx)$ 에서 $a$와 $b$의 역할은 무엇일까요?")
    st.session_state.tan_opinion = st.text_area(
        "$\tan$ 함수에 대한 여러분의 의견을 자유롭게 적어주세요.",
        value=st.session_state.tan_opinion, # 세션 상태 값 불러오기
        height=150,
        key="tan_opinion_box"
    )

    st.markdown("---")
    st.info("작성된 내용은 페이지를 새로고침하거나 닫기 전까지 유지됩니다. (실제 환경에서는 제출된 의견을 데이터베이스에 저장하거나 다른 방식으로 활용할 수 있습니다.)")

st.markdown("---")
st.caption("powered by Streamlit & Plotly")
