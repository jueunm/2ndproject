import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.express as px
from datetime import datetime, timedelta

# --- 페이지 설정 ---
st.set_page_config(
    page_title="글로벌 Top 10 기업 주가",
    page_icon="📈",
    layout="wide"
)

# --- 제목 ---
st.title("글로벌 시가총액 Top 10 기업 주가 변화 (최근 3년)")
st.write(f"데이터 기준일: {datetime.now().strftime('%Y-%m-%d')}")

# --- Top 10 기업 정보 ---
TOP_10_COMPANIES = {
    "NVIDIA": "NVDA",
    "Microsoft": "MSFT",
    "Apple": "AAPL",
    "Alphabet (Google)": "GOOGL",
    "Amazon": "AMZN",
    "Saudi Aramco": "2222.SR",
    "Meta Platforms": "META",
    "TSMC": "TSM",
    "Berkshire Hathaway": "BRK-B",
    "Eli Lilly": "LLY"
}

# --- 데이터 불러오기 ---
@st.cache_data
def load_stock_data(ticker, start_date, end_date):
    """지정된 기간 동안의 주가 데이터를 yfinance를 통해 불러옵니다."""
    try:
        data = yf.download(ticker, start=start_date, end=end_date)
        if data.empty:
            return None
        return data
    except Exception as e:
        st.error(f"{ticker} 데이터를 불러오는 중 오류가 발생했습니다: {e}")
        return None

# --- 날짜 설정 ---
end_date = datetime.now()
start_date = end_date - timedelta(days=3*365)

# --- 사이드바 설정 ---
st.sidebar.header("기업 선택")
selected_company_name = st.sidebar.selectbox(
    "확인하고 싶은 기업을 선택하세요.",
    list(TOP_10_COMPANIES.keys())
)
selected_ticker = TOP_10_COMPANIES[selected_company_name]

# --- 메인 화면 ---
st.header(f"'{selected_company_name}' 주가 차트")

# 데이터 로딩 및 시각화
stock_data = load_stock_data(selected_ticker, start_date, end_date)

if stock_data is not None and not stock_data.empty:
    # 종가 그래프 (수정된 부분)
    fig_close = px.line(
        stock_data,
        y="Close",
        title=f"{selected_company_name} 종가 (3년)",
        labels={"Close": "종가", "index": "날짜"}
    )
    fig_close.update_layout(
        xaxis_title="날짜",
        yaxis_title="주가",
        showlegend=False
    )
    st.plotly_chart(fig_close, use_container_width=True)

    # 거래량 그래프 (수정된 부분)
    fig_volume = px.bar(
        stock_data,
        y="Volume",
        title=f"{selected_company_name} 거래량 (3년)",
        labels={"Volume": "거래량", "index": "날짜"}
    )
    fig_volume.update_layout(
        xaxis_title="날짜",
        yaxis_title="거래량",
        showlegend=False
    )
    st.plotly_chart(fig_volume, use_container_width=True)

    # 최근 데이터 테이블
    st.subheader("최근 주가 데이터")
    st.dataframe(stock_data.tail().style.format("{:.2f}"))

else:
    st.warning("선택하신 기업의 주가 데이터를 불러올 수 없습니다.")

# --- 참고 정보 ---
st.sidebar.markdown("---")
st.sidebar.info(
    """
    **정보:**
    - 이 앱은 `yfinance` 라이브러리를 사용하여 주가 데이터를 실시간으로 가져옵니다.
    - 시가총액 순위는 변동될 수 있습니다.
    - 데이터는 참고용이며, 투자 결정에 대한 책임은 본인에게 있습니다.
    """
)
