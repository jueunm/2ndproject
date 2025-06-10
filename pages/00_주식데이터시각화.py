import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

st.title("글로벌 시총 Top 10 기업 최근 3년 주가 변화")

# Top 10 기업 티커 리스트 (필요시 변경 가능)
tickers = {
    "Apple": "AAPL",
    "Microsoft": "MSFT",
    "Saudi Aramco": "2222.SR",
    "Alphabet": "GOOGL",
    "Amazon": "AMZN",
    "NVIDIA": "NVDA",
    "Berkshire Hathaway": "BRK-B",
    "Tesla": "TSLA",
    "Meta Platforms": "META",
    "Taiwan Semiconductor": "TSM"
}

# 시작, 끝 날짜 설정 (오늘 기준 3년 전부터)
end_date = pd.Timestamp.today()
start_date = end_date - pd.DateOffset(years=3)

# 데이터 다운로드
@st.cache_data(ttl=86400)  # 하루 캐싱
def download_data(tickers, start, end):
    data = yf.download(list(tickers.values()), start=start, end=end)["Adj Close"]
    return data

data = download_data(tickers, start_date, end_date)

# 종목 선택 (여러 개 선택 가능)
selected = st.multiselect("기업 선택", options=list(tickers.keys()), default=list(tickers.keys()))

if selected:
    st.subheader("주가 그래프 (조정 종가)")
    fig, ax = plt.subplots(figsize=(12, 6))

    for company in selected:
        ticker = tickers[company]
        ax.plot(data.index, data[ticker], label=company)

    ax.set_xlabel("날짜")
    ax.set_ylabel("주가 (USD 기준, 조정 종가)")
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)
else:
    st.info("하단에서 최소 1개 이상의 기업을 선택해 주세요.")
