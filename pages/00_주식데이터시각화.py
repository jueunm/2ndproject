import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime, timedelta
import numpy as np

# 페이지 설정
st.set_page_config(
    page_title="글로벌 시총 Top10 기업 주가 분석",
    page_icon="📈",
    layout="wide"
)

# 제목
st.title("📈 글로벌 시총 Top10 기업 주가 분석 (최근 3년)")
st.markdown("---")

# 글로벌 시총 상위 10개 기업 (2025년 기준)
companies = {
    'Apple': 'AAPL',
    'Microsoft': 'MSFT', 
    'Nvidia': 'NVDA',
    'Amazon': 'AMZN',
    'Alphabet': 'GOOGL',
    'Saudi Aramco': '2222.SR',
    'Meta Platforms': 'META',
    'Berkshire Hathaway': 'BRK-A',
    'Tesla': 'TSLA',
    'Broadcom': 'AVGO'
}

# 사이드바 설정
st.sidebar.header("설정")

# 기간 설정
end_date = datetime.now()
start_date = end_date - timedelta(days=3*365)  # 3년

# 선택할 기업들
selected_companies = st.sidebar.multiselect(
    "분석할 기업 선택:",
    list(companies.keys()),
    default=list(companies.keys())[:5]  # 기본으로 상위 5개 선택
)

# 차트 유형 선택
chart_type = st.sidebar.selectbox(
    "차트 유형:",
    ["종가 추이", "정규화된 수익률", "거래량", "시가총액 변화"]
)

# 데이터 로딩 함수
@st.cache_data
def load_stock_data(symbols, start_date, end_date):
    data = {}
    progress_bar = st.progress(0)
    
    for i, (name, symbol) in enumerate(symbols.items()):
        try:
            # yf.download() 사용 (ticker.download()가 아님)
            hist = yf.download(symbol, start=start_date, end=end_date)
            
            if not hist.empty:
                # 기업 정보 가져오기
                ticker = yf.Ticker(symbol)
                try:
                    info = ticker.info
                except:
                    info = {}
                
                data[name] = {
                    'data': hist,
                    'info': info
                }
            else:
                st.warning(f"{name} ({symbol}) 데이터를 가져올 수 없습니다.")
                
        except Exception as e:
            st.error(f"{name} ({symbol}) 데이터 로딩 중 오류: {str(e)}")
            
        progress_bar.progress((i + 1) / len(symbols))
    
    progress_bar.empty()
    return data

# 선택된 기업들의 데이터 로딩
if selected_companies:
    selected_symbols = {name: companies[name] for name in selected_companies}
    
    with st.spinner("주식 데이터를 로딩중입니다..."):
        stock_data = load_stock_data(selected_symbols, start_date, end_date)
    
    if stock_data:
        # 메인 차트 영역
        col1, col2 = st.columns([3, 1])
        
        with col1:
            st.subheader(f"{chart_type} 차트")
            
            fig = go.Figure()
            
            if chart_type == "종가 추이":
                for company, data in stock_data.items():
                    if 'data' in data and not data['data'].empty:
                        fig.add_trace(go.Scatter(
                            x=data['data'].index,
                            y=data['data']['Close'],
                            mode='lines',
                            name=company,
                            line=dict(width=2)
                        ))
                
                fig.update_layout(
                    title="주가 종가 추이 (USD)",
                    xaxis_title="날짜",
                    yaxis_title="주가 (USD)",
                    hovermode='x unified',
                    height=600
                )
                
            elif chart_type == "정규화된 수익률":
                for company, data in stock_data.items():
                    if 'data' in data and not data['data'].empty:
                        normalized = (data['data']['Close'] / data['data']['Close'].iloc[0] - 1) * 100
                        fig.add_trace(go.Scatter(
                            x=data['data'].index,
                            y=normalized,
                            mode='lines',
                            name=company,
                            line=dict(width=2)
                        ))
                
                fig.update_layout(
                    title="정규화된 수익률 (%)",
                    xaxis_title="날짜",
                    yaxis_title="수익률 (%)",
                    hovermode='x unified',
                    height=600
                )
                
            elif chart_type == "거래량":
                for company, data in stock_data.items():
                    if 'data' in data and not data['data'].empty:
                        fig.add_trace(go.Scatter(
                            x=data['data'].index,
                            y=data['data']['Volume'],
                            mode='lines',
                            name=company,
                            line=dict(width=2)
                        ))
                
                fig.update_layout(
                    title="거래량 추이",
                    xaxis_title="날짜",
                    yaxis_title="거래량",
                    hovermode='x unified',
                    height=600
                )
                
            elif chart_type == "시가총액 변화":
                for company, data in stock_data.items():
                    if 'data' in data and not data['data'].empty and 'info' in data:
                        try:
                            shares_outstanding = data['info'].get('sharesOutstanding', 0)
                            if shares_outstanding > 0:
                                market_cap = data['data']['Close'] * shares_outstanding / 1e12  # 조 달러 단위
                                fig.add_trace(go.Scatter(
                                    x=data['data'].index,
                                    y=market_cap,
                                    mode='lines',
                                    name=company,
                                    line=dict(width=2)
                                ))
                        except:
                            pass
                
                fig.update_layout(
                    title="시가총액 변화 (조 달러)",
                    xaxis_title="날짜",
                    yaxis_title="시가총액 (조 USD)",
                    hovermode='x unified',
                    height=600
                )
            
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            st.subheader("📊 주요 지표")
            
            # 각 기업별 주요 지표 표시
            for company, data in stock_data.items():
                if 'data' in data and not data['data'].empty:
                    try:
                        current_price = float(data['data']['Close'].iloc[-1])
                        start_price = float(data['data']['Close'].iloc[0])
                        total_return = ((current_price - start_price) / start_price) * 100
                        
                        st.metric(
                            label=f"{company}",
                            value=f"${current_price:.2f}",
                            delta=f"{total_return:.1f}%"
                        )
                    except (ValueError, TypeError, IndexError) as e:
                        st.error(f"{company} 데이터 처리 오류: {str(e)}")
        
        # 상세 분석 섹션
        st.markdown("---")
        st.subheader("📈 상세 분석")
        
        # 수익률 비교 테이블
        returns_data = []
        for company, data in stock_data.items():
            if 'data' in data and not data['data'].empty:
                try:
                    prices = data['data']['Close']
                    current_price = float(prices.iloc[-1])
                    start_price = float(prices.iloc[0])
                    
                    # 1년 전 가격 (가능한 경우)
                    one_year_ago = datetime.now() - timedelta(days=365)
                    one_year_return = None
                    try:
                        one_year_price_data = prices[prices.index >= one_year_ago]
                        if not one_year_price_data.empty:
                            one_year_price = float(one_year_price_data.iloc[0])
                            one_year_return = ((current_price - one_year_price) / one_year_price) * 100
                    except:
                        pass
                    
                    # 변동성 계산
                    daily_returns = prices.pct_change().dropna()
                    if not daily_returns.empty:
                        volatility = daily_returns.std() * np.sqrt(252) * 100  # 연간화된 변동성
                    else:
                        volatility = 0
                    
                    returns_data.append({
                        '기업명': company,
                        '현재가 (USD)': f"${current_price:.2f}",
                        '3년 수익률 (%)': f"{((current_price - start_price) / start_price) * 100:.1f}%",
                        '1년 수익률 (%)': f"{one_year_return:.1f}%" if one_year_return is not None else "N/A",
                        '연간 변동성 (%)': f"{volatility:.1f}%"
                    })
                except Exception as e:
                    st.error(f"{company} 수익률 계산 오류: {str(e)}")
        
        if returns_data:
            returns_df = pd.DataFrame(returns_data)
            st.dataframe(returns_df, use_container_width=True)
        
        # 상관관계 분석
        if len(stock_data) > 1:
            st.subheader("🔗 주가 상관관계 분석")
            
            try:
                # 상관관계 매트릭스 생성
                correlation_data = {}
                min_length = float('inf')
                
                # 먼저 모든 데이터의 일일 수익률을 계산하고 최소 길이 찾기
                for company, data in stock_data.items():
                    if 'data' in data and not data['data'].empty:
                        daily_returns = data['data']['Close'].pct_change().dropna()
                        if len(daily_returns) > 10:  # 최소 10일 이상의 데이터가 있어야 함
                            correlation_data[company] = daily_returns
                            min_length = min(min_length, len(daily_returns))
                
                if len(correlation_data) > 1 and min_length > 10:
                    # 모든 시리즈를 같은 길이로 맞추기 (뒤에서부터 자르기)
                    aligned_data = {}
                    for company, returns in correlation_data.items():
                        aligned_data[company] = returns.tail(min_length)
                    
                    # DataFrame 생성 및 상관관계 계산
                    corr_df = pd.DataFrame(aligned_data).corr()
                    
                    if not corr_df.empty:
                        # 히트맵 생성
                        fig_corr = px.imshow(
                            corr_df,
                            text_auto=True,
                            aspect="auto",
                            color_continuous_scale="RdBu_r",
                            title="일일 수익률 상관관계",
                            zmin=-1,
                            zmax=1
                        )
                        fig_corr.update_layout(height=400)
                        st.plotly_chart(fig_corr, use_container_width=True)
                    else:
                        st.warning("상관관계 분석을 위한 충분한 데이터가 없습니다.")
                else:
                    st.warning("상관관계 분석을 위해서는 최소 2개 기업의 충분한 데이터가 필요합니다.")
                    
            except Exception as e:
                st.error(f"상관관계 분석 중 오류가 발생했습니다: {str(e)}")
                st.info("다른 기업들을 선택하거나 다시 시도해보세요.")
        
        # 데이터 출처 및 주의사항
        st.markdown("---")
        st.info("""
        **데이터 출처**: Yahoo Finance (yfinance)  
        **주의사항**: 
        - 과거 주가는 미래 수익률을 보장하지 않습니다.
        - 투자 결정 시 충분한 조사와 전문가 상담을 권장합니다.
        - Saudi Aramco의 경우 사우디 증시 데이터로, 환율 변동이 반영되지 않을 수 있습니다.
        """)
        
else:
    st.warning("분석할 기업을 선택해주세요.")

# 푸터
st.markdown("---")
st.markdown("*Made with Streamlit and yfinance*")
