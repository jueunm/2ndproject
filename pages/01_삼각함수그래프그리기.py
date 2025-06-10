import streamlit as st
import numpy as np
import plotly.graph_objects as go

st.set_page_config(layout="wide") # 페이지 전체 너비 사용

st.title("삼각함수 그래프 그리기 📊")

st.write("""
이 활동에서는 $\sin$, $\cos$, $\tan$ 함수 중 하나를 선택하고,
$y = a \sin(bx)$, $y = a \cos(bx)$, $y = a \tan(bx)$ 형태의 그래프에서
$a$와 $b$ 값을 직접 입력하여 그래프가 어떻게 변하는지 탐색할 수 있습니다.
""")

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
st.header(f"선택된 함수: {function_type.upper()} 그래프")

x = np.linspace(-2 * np.pi, 2 * np.pi, 500) # -2π 부터 2π 까지 500개의 점 생성

if function_type == 'sin':
    y = a_value * np.sin(b_value * x)
    equation = f"y = {a_value:.2f} sin({b_value:.2f}x)"
elif function_type == 'cos':
    y = a_value * np.cos(b_value * x)
    equation = f"y = {a_value:.2f} cos({b_value:.2f}x)"
elif function_type == 'tan':
    # tan 함수의 경우, 점근선 근처에서 값이 발산하므로 주의
    # b*x 값이 홀수 파이/2 근처에서 문제가 발생하므로 해당 부분을 제외하거나 범위를 조절해야 합니다.
    # 여기서는 간단하게 처리하고, 실제 수업에서는 이 부분을 설명해주는 것이 좋습니다.
    y = a_value * np.tan(b_value * x)
    equation = f"y = {a_value:.2f} tan({b_value:.2f}x)"
    # tan 함수의 특성상 y축 범위 제한
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

st.markdown("---")

# 4. 활동을 마무리한 후 하단 공간에 a, b 값에 따른 특징에 대한 자기 의견을 적게 하기
st.header("나의 탐구 결과📝")
st.write(f"""
선택한 함수: **{function_type.upper()}**
입력한 $a$ 값: **{a_value:.2f}**
입력한 $b$ 값: **{b_value:.2f}**
""")

student_opinion = st.text_area(
    "위 그래프를 보며 $a$와 $b$ 값이 그래프의 모양에 어떤 영향을 주는지 자유롭게 적어주세요. "
    "예를 들어, 'a 값을 크게 하니 그래프의 높이가 높아졌어요.'와 같이 작성할 수 있습니다.",
    height=150,
    key="student_opinion_box"
)

if student_opinion:
    st.write("---")
    st.subheader("제출된 의견:")
    st.write(student_opinion)
    st.success("의견이 성공적으로 저장되었습니다!")
    st.info("실제 환경에서는 제출된 의견을 데이터베이스에 저장하거나 다른 방식으로 활용할 수 있습니다.")

st.markdown("---")
st.caption("powered by Streamlit & Plotly")
