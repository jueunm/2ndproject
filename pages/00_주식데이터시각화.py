import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime, timedelta
import numpy as np

# 페이지 설정
st.set_page_config(
    page_title="글로벌 시총 Top10 주가 분석",
    page_icon="📈",
    layout="wide"
)

# 글로벌 시총 상위 10개 기업 (2024년 기준)
TOP_10_COMPANIES = {
    'AAPL': 'Apple Inc.',
    'MSFT': 'Microsoft Corporation',
    'GOOGL': 'Alphabet Inc.',
    'AMZN': 'Amazon.com Inc.',
    'NVDA': 'NVIDIA Corporation',
    'TSLA': 'Tesla Inc.',
    'META': 'Meta Platforms Inc.',
    'BRK-B': 'Berkshire Hathaway Inc.',
    'UNH': 'UnitedHealth Group Inc.',
    'JNJ': 'Johnson & Johnson'
}

@st.cache_data(ttl=3600)  # 1시간 캐시
def fetch_stock_data(symbols, period="3y"):
    """주식 데이터를 가져오는 함수"""
    data = {}
    progress_bar = st.progress(0)
    
    for i, symbol in enumerate(symbols):
        try:
            ticker = yf.Ticker(symbol)
            hist = ticker.history(period=period)
            if not hist.empty:
                data[symbol] = hist
            progress_bar.progress((i + 1) / len(symbols))
        except Exception as e:
            st.error(f"{symbol} 데이터 가져오기 실패: {str(e)}")
    
    progress_bar.empty()
    return data

def calculate_returns(data):
    """수익률 계산 함수"""
    returns_data = {}
    for symbol, df in data.items():
        if not df.empty:
            start_price = df['Close'].iloc[0]
            current_price = df['Close'].iloc[-1]
            total_return = ((current_price - start_price) / start_price) * 100
            returns_data[symbol] = {
                'company': TOP_10_COMPANIES[symbol],
                'start_price': start_price,
                'current_price': current_price,
                'total_return': total_return,
                'data': df
            }
    return returns_data

def main():
    st.title("📈 글로벌 시총 Top10 기업 주가 분석")
    st.markdown("### 최근 3년간 주가 변화 추이")
    
    # 사이드바 설정
    st.sidebar.header("설정")
    
    # 기간 선택
    period_options = {
        "1년": "1y",
        "2년": "2y", 
        "3년": "3y",
        "5년": "5y"
    }
    selected_period = st.sidebar.selectbox(
        "분석 기간 선택",
        options=list(period_options.keys()),
        index=2  # 기본값 3년
    )
    
    # 회사 선택
    selected_companies = st.sidebar.multiselect(
        "분석할 회사 선택",
        options=list(TOP_10_COMPANIES.keys()),
        default=list(TOP_10_COMPANIES.keys()),
        format_func=lambda x: f"{x} - {TOP_10_COMPANIES[x]}"
    )
    
    if not selected_companies:
        st.warning("최소 하나의 회사를 선택해주세요.")
        return
    
    # 데이터 로딩
    with st.spinner("주식 데이터를 가져오는 중..."):
        stock_data = fetch_stock_data(selected_companies, period_options[selected_period])
    
    if not stock_data:
        st.error("데이터를 가져올 수 없습니다.")
        return
    
    # 수익률 계산
    returns_data = calculate_returns(stock_data)
    
    # 메인 차트 - 정규화된 가격 변화
    st.subheader("📊 정규화된 주가 변화 (시작점 100 기준)")
    
    fig_normalized = go.Figure()
    
    for symbol, info in returns_data.items():
        df = info['data']
        normalized_prices = (df['Close'] / df['Close'].iloc[0]) * 100
        
        fig_normalized.add_trace(go.Scatter(
            x=df.index,
            y=normalized_prices,
            mode='lines',
            name=f"{symbol} - {info['company'][:20]}",
            line=dict(width=2),
            hovertemplate=f"<b>{symbol}</b><br>" +
                         "날짜: %{x}<br>" +
                         "정규화 가격: %{y:.2f}<br>" +
                         "<extra></extra>"
        ))
    
    fig_normalized.update_layout(
        title=f"최근 {selected_period} 정규화 주가 추이",
        xaxis_title="날짜",
        yaxis_title="정규화된 가격 (시작점=100)",
        hovermode='x unified',
        height=600,
        showlegend=True
    )
    
    st.plotly_chart(fig_normalized, use_container_width=True)
    
    # 수익률 요약 테이블
    st.subheader("💰 수익률 요약")
    
    summary_df = pd.DataFrame([
        {
            '종목코드': symbol,
            '회사명': info['company'],
            '시작가격($)': f"{info['start_price']:.2f}",
            '현재가격($)': f"{info['current_price']:.2f}",
            f'{selected_period} 수익률(%)': f"{info['total_return']:.2f}%"
        }
        for symbol, info in returns_data.items()
    ])
    
    # 수익률 기준 정렬
    summary_df['수익률_숫자'] = [info['total_return'] for info in returns_data.values()]
    summary_df = summary_df.sort_values('수익률_숫자', ascending=False)
    summary_df = summary_df.drop('수익률_숫자', axis=1)
    
    st.dataframe(summary_df, use_container_width=True, hide_index=True)
    
    # 수익률 바차트
    st.subheader("📊 수익률 비교")
    
    returns_df = pd.DataFrame([
        {'회사': f"{symbol}\n{info['company'][:15]}", '수익률': info['total_return']}
        for symbol, info in returns_data.items()
    ]).sort_values('수익률', ascending=True)
    
    fig_bar = px.bar(
        returns_df,
        x='수익률',
        y='회사',
        orientation='h',
        title=f"최근 {selected_period} 수익률 비교",
        color='수익률',
        color_continuous_scale='RdYlGn',
        text='수익률'
    )
    
    fig_bar.update_traces(texttemplate='%{text:.1f}%', textposition='outside')
    fig_bar.update_layout(
        height=400,
        xaxis_title="수익률 (%)",
        yaxis_title="회사",
        showlegend=False
    )
    
    st.plotly_chart(fig_bar, use_container_width=True)
    
    # 개별 주가 차트 (선택사항)
    if st.checkbox("개별 회사 상세 차트 보기"):
        st.subheader("📈 개별 회사 주가 차트")
        
        selected_company = st.selectbox(
            "상세 분석할 회사 선택",
            options=selected_companies,
            format_func=lambda x: f"{x} - {TOP_10_COMPANIES[x]}"
        )
        
        if selected_company in returns_data:
            info = returns_data[selected_company]
            df = info['data']
            
            fig_individual = go.Figure()
            
            # 캔들스틱 차트
            fig_individual.add_trace(go.Candlestick(
                x=df.index,
                open=df['Open'],
                high=df['High'],
                low=df['Low'],
                close=df['Close'],
                name=f"{selected_company} 주가"
            ))
            
            # 볼륨 차트 (보조축)
            fig_individual.add_trace(go.Bar(
                x=df.index,
                y=df['Volume'],
                name="거래량",
                yaxis='y2',
                opacity=0.3
            ))
            
            fig_individual.update_layout(
                title=f"{selected_company} - {info['company']} 상세 차트",
                xaxis_title="날짜",
                yaxis_title="주가 ($)",
                yaxis2=dict(
                    title="거래량",
                    overlaying='y',
                    side='right'
                ),
                height=600
            )
            
            st.plotly_chart(fig_individual, use_container_width=True)
            
            # 통계 정보
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                st.metric("현재가", f"${info['current_price']:.2f}")
            with col2:
                st.metric("총 수익률", f"{info['total_return']:.2f}%")
            with col3:
                st.metric("최고가", f"${df['High'].max():.2f}")
            with col4:
                st.metric("최저가", f"${df['Low'].min():.2f}")
    
    # 데이터 업데이트 정보
    st.sidebar.markdown("---")
    st.sidebar.info(f"마지막 업데이트: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    st.sidebar.markdown("💡 데이터는 1시간마다 자동 갱신됩니다.")

if __name__ == "__main__":
    main()
