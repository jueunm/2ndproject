import streamlit as st
import folium
from streamlit_folium import st_folium

# -----------------------------
# 관광지 정보 정의
# -----------------------------
tourist_spots = {
    "리스본 (Lisbon)": {
        "location": [38.7169, -9.1399],
        "description": """포르투갈의 수도 리스본은 7개의 언덕 위에 지어진 도시로, 역사와 현대가 공존합니다.
- 꼭 가봐야 할 장소: 벨렘 타워, 제로니모 수도원, 알파마 지구
- 맛집 추천: Pastéis de Belém에서 먹는 에그 타르트는 필수!
"""
    },
    "포르투 (Porto)": {
        "location": [41.1579, -8.6291],
        "description": """포르투는 도루 강을 따라 펼쳐진 도시로, 포트 와인의 본고장입니다.
- 랜드마크: 루이스 1세 다리, 리베이라 지구, 클레리고스 타워
- 특산물: 포트 와인 테이스팅 투어는 놓치지 마세요!
"""
    },
    "신트라 (Sintra)": {
        "location": [38.7984, -9.3960],
        "description": """신트라는 동화 속 풍경 같은 궁전과 정원이 있는 마법 같은 마을입니다.
- 주요 명소: 페나 궁전, 무어 성, 레갈레이라 저택
- 팁: 리스본에서 기차로 40분 거리로 당일치기 여행에 딱 좋아요.
"""
    },
    "파루 (Faro)": {
        "location": [37.0194, -7.9304],
        "description": """알가르브 지역의 중심 도시로, 아름다운 해변과 역사적인 구시가지가 유명합니다.
- 관광지: 파루 대성당, 본 에스페랑사 해변
- 추천: 조용하고 여유로운 휴양을 원한다면 최고의 선택!
"""
    },
    "마데이라 (Madeira)": {
        "location": [32.7607, -16.9595],
        "description": """대서양에 위치한 포르투갈의 섬으로, 천혜의 자연경관이 펼쳐집니다.
- 하이라이트: 레반다 트레킹, 피코 두 아리에이루 산
- 팁: 1년 내내 온화한 기후로 여행하기 좋은 섬이에요.
"""
    }
}

# -----------------------------
# Streamlit 페이지 설정
# -----------------------------
st.set_page_config(page_title="포르투갈 관광 가이드", layout="wide")

st.title("🇵🇹 포르투갈 주요 관광지 가이드")
st.markdown("포르투갈의 아름다운 도시들을 **지도로 보고**, 각 지역에 대한 **친절한 설명**을 함께 확인하세요!")

# -----------------------------
# 관광지 선택
# -----------------------------
selected_city = st.sidebar.selectbox("🔎 관광지를 선택하세요", list(tourist_spots.keys()))

# -----------------------------
# Folium 지도 생성
# -----------------------------
m = folium.Map(location=[39.5, -8.0], zoom_start=6)

for city, info in tourist_spots.items():
    popup_html = f"<b>{city}</b><br><pre style='white-space: pre-wrap;'>{info['description']}</pre>"
    folium.Marker(
        location=info["location"],
        popup=folium.Popup(popup_html, max_width=300),
        tooltip=city,
        icon=folium.Icon(color="blue" if city != selected_city else "red", icon="info-sign")
    ).add_to(m)

# -----------------------------
# 지도 출력
# -----------------------------
st.subheader(f"🗺️ {selected_city} 지도 위치")
st_data = st_folium(m, width=700, height=500)

# -----------------------------
# 상세 설명 출력
# -----------------------------
st.subheader(f"📍 {selected_city} 소개")
st.markdown(tourist_spots[selected_city]["description"])
