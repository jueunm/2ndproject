import streamlit as st
import folium
from streamlit_folium import folium_static

st.set_page_config(layout="wide", page_title="포르투갈 관광 가이드", page_icon="🇵🇹")

# --- CSS for Styling ---
st.markdown("""
<style>
    .main-header {
        font-size: 3.5em;
        color: #0047AB; /* Dark Blue */
        text-align: center;
        margin-bottom: 0.5em;
        text-shadow: 2px 2px 5px rgba(0,0,0,0.2);
    }
    .sub-header {
        font-size: 2.5em;
        color: #0066CC; /* Medium Blue */
        margin-top: 1em;
        margin-bottom: 0.5em;
        border-bottom: 2px solid #0066CC;
        padding-bottom: 5px;
    }
    .section-header {
        font-size: 2em;
        color: #008CBA; /* Light Blue */
        margin-top: 1.5em;
        margin-bottom: 0.7em;
        border-left: 8px solid #FFD700; /* Gold */
        padding-left: 10px;
    }
    .attraction-title {
        font-size: 1.8em;
        color: #0047AB;
        margin-top: 1.2em;
        margin-bottom: 0.5em;
    }
    .stApp {
        background-color: #F0F8FF; /* Alice Blue */
        color: #333333;
    }
    .stMarkdown {
        line-height: 1.8;
    }
    .stButton>button {
        background-color: #FFD700; /* Gold */
        color: #0047AB;
        font-weight: bold;
        border-radius: 10px;
        padding: 10px 20px;
        border: none;
        cursor: pointer;
    }
    .stButton>button:hover {
        background-color: #E0B500; /* Darker Gold */
        color: #FFFFFF;
    }
    .info-box {
        background-color: #E0F2F7; /* Lighter Blue */
        border-left: 5px solid #FFD700;
        padding: 15px;
        margin-bottom: 15px;
        border-radius: 5px;
    }
    .folium-map {
        border-radius: 10px;
        overflow: hidden;
        box-shadow: 5px 5px 15px rgba(0,0,0,0.2);
    }
</style>
""", unsafe_allow_html=True)

# --- Header ---
st.markdown("<h1 class='main-header'>✨ 아주 친절하고 자세한 포르투갈 관광 가이드 🇵🇹</h1>", unsafe_allow_html=True)
st.write("---")

st.markdown("""
<p style="font-size:1.2em; text-align:center;">
아름다운 해안선, 풍부한 역사, 맛있는 음식, 그리고 따뜻한 사람들의 나라, 포르투갈에 오신 것을 환영합니다!
이 가이드는 여러분의 포르투갈 여행을 더욱 특별하게 만들어 줄 핵심 정보를 제공합니다.
</p>
""", unsafe_allow_html=True)

st.write("---")

# --- Table of Contents / Navigation ---
st.sidebar.title("목차")
page = st.sidebar.radio("원하는 섹션을 선택하세요:", [
    "✨ 첫 포르투갈 여행자를 위한 특별 가이드",
    "🗺️ 포르투갈 주요 관광지 지도",
    "✨ 포르투갈의 미식과 문화",
    "🗓️ 나만의 추천 일정 만들기" # New section
])

# --- Attraction Data (Detailed) ---
# This data structure will hold all information for each city/attraction
attraction_data = {
    "리스본": {
        "coords": [38.7223, -9.1393],
        "description": "포르투갈의 활기찬 수도 리스본은 일곱 언덕 위에 자리 잡고 있으며, 다채로운 역사와 현대적인 매력이 조화를 이룹니다. 노란색 트램이 좁은 골목을 오가고, 파두 음악이 밤하늘을 채우는 이 도시는 여러분을 매료시킬 것입니다.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Lisbon_as_seen_from_Miradouro_de_Santa_Catarina.jpg/1200px-Lisbon_as_seen_from_Miradouro_de_Santa_Catarina.jpg",
        "attractions": [
            {"name": "벨렘 탑 (Belém Tower)", "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Torre_de_Bel%C3%A9m_%282012%29.jpg/800px-Torre_de_Bel%C3%A9m_%282012%29.jpg",
             "desc": "테주 강가에 서 있는 벨렘 탑은 16세기 초에 지어진 아름다운 요새이자 등대입니다. 포르투갈 대항해 시대의 상징이며, 유네스코 세계문화유산으로 등재되어 있습니다. 이곳에서 바다를 향한 포르투갈의 위대한 꿈을 엿볼 수 있습니다.",
             "why": "역사적인 중요성, 독특한 건축 양식, 아름다운 강변 풍경.",
             "tip": "내부를 방문하려면 미리 온라인으로 티켓을 예약하는 것이 좋습니다. 옆에 위치한 발견 기념비와 함께 방문하세요."},
            {"name": "제로니무스 수도원 (Jerónimos Monastery)", "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ef/Mosteiro_dos_Jer%C3%B3nimos_Exterior.jpg/1200px-Mosteiro_dos_Jer%C3%B3nimos_Exterior.jpg",
             "desc": "벨렘 탑과 함께 유네스코 세계문화유산인 제로니무스 수도원은 마누엘 양식의 걸작입니다. 바스코 다 가마의 무덤이 안치되어 있으며, 웅장한 규모와 섬세한 조각이 감탄을 자아냅니다.",
             "why": "포르투갈 건축의 정수, 역사적 인물들의 안식처.",
             "tip": "수도원 옆에 위치한 유명한 벨렘 에그 타르트(Pastéis de Belém)를 꼭 맛보세요!"},
            {"name": "상 조르제 성 (São Jorge Castle)", "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Castelo_de_S%C3%A3o_Jorge_Overview.jpg/1200px-Castelo_de_S%C3%A3o_Jorge_Overview.jpg",
             "desc": "리스본에서 가장 높은 언덕에 위치한 상 조르제 성은 도시 전체를 조망할 수 있는 최고의 장소입니다. 고대 로마 시대부터 요새가 있었던 곳으로, 리스본의 역사를 온전히 담고 있습니다.",
             "why": "리스본 최고의 전망, 역사적인 분위기, 공작새와 함께하는 산책.",
             "tip": "일몰 시간에 방문하면 더욱 아름다운 풍경을 감상할 수 있습니다. 성벽을 따라 걸으며 사진을 찍어보세요."},
            {"name": "알파마 지구 (Alfama District)", "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b3/Alfama_Lisbon_view.jpg/1200px-Alfama_Lisbon_view.jpg",
             "desc": "리스본에서 가장 오래된 지구인 알파마는 미로 같은 좁은 골목, 계단, 그리고 숨겨진 광장들로 가득합니다. 파두 음악의 본고장으로, 밤에는 작은 레스토랑에서 슬프고도 아름다운 파두 공연을 즐길 수 있습니다.",
             "why": "리스본의 진정한 매력을 느낄 수 있는 곳, 파두 음악 체험, 그림 같은 풍경.",
             "tip": "28번 트램을 타고 알파마 지구를 둘러보는 것은 리스본의 상징적인 경험입니다."},
            {"name": "신트라 (Sintra)", "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/02/Pena_Palace_Facade_%28cropped%29.jpg/1200px-Pena_Palace_Facade_%28cropped%29.jpg",
             "desc": "리스본에서 기차로 약 40분 거리에 위치한 신트라는 동화 속에 나올 법한 궁전과 성으로 가득한 유네스코 세계문화유산 마을입니다. 페나 궁전, 무어 성, 킨타 다 헤갈레이라 등이 주요 명소입니다.",
             "why": "아름다운 건축물, 신비로운 분위기, 리스본 근교 당일치기 여행으로 최고.",
             "tip": "신트라는 언덕이 많고 교통이 복잡할 수 있으니, 미리 동선을 계획하고 대중교통이나 투어 버스를 이용하는 것이 좋습니다. 특히 페나 궁전은 인기가 많으니 일찍 방문하세요."}
        ]
    },
    "포르투": {
        "coords": [41.1579, -8.6291],
        "description": "포르투갈 북부의 심장부인 포르투는 도루 강을 따라 펼쳐진 아름다운 도시입니다. 유서 깊은 와인 셀러, 매력적인 구시가지, 그리고 미식의 즐거움이 가득합니다.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f9/Porto_Portugal_-_Ribeira_and_Douro_River.jpg/1200px-Porto_Portugal_-_Ribeira_and_Douro_River.jpg",
        "attractions": [
            {"name": "포르투 리베이라 지구 (Ribeira District)", "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c1/Porto_Ribeira_at_sunset.jpg/1200px-Porto_Ribeira_at_sunset.jpg",
             "desc": "유네스코 세계문화유산인 리베이라 지구는 다채로운 색깔의 건물, 좁은 골목, 그리고 강변 레스토랑이 어우러져 활기찬 분위기를 자아냅니다. 도루 강변을 따라 산책하거나 보트 투어를 즐기기에 좋습니다.",
             "why": "포르투의 상징적인 풍경, 활기찬 분위기, 강변에서의 휴식.",
             "tip": "밤에는 다리 건너편 빌라 노바 드 가이아(Vila Nova de Gaia)에서 리베이라 지구의 야경을 감상하세요."},
            {"name": "동 루이스 1세 다리 (Dom Luís I Bridge)", "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b8/Porto_-_Ponte_Lu%C3%ADs_I_%287313019130%29.jpg/1200px-Porto_-_Ponte_Lu%C3%ADs_I_%287313019130%29.jpg",
             "desc": "에펠탑을 설계한 에펠의 제자가 설계한 이 거대한 철골 다리는 포르투와 빌라 노바 드 가이아를 연결합니다. 다리 위를 걷거나 트램을 타고 강 양쪽의 멋진 전경을 감상할 수 있습니다.",
             "why": "인상적인 건축물, 도루 강과 도시의 파노라마 전망.",
             "tip": "다리의 상층부는 지하철과 보행자 전용이고, 하층부는 차량과 보행자 모두 이용 가능합니다. 특히 상층부에서 보는 야경이 일품입니다."},
            {"name": "렐루 서점 (Livraria Lello)", "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Livraria_Lello_at_night.jpg/800px-Livraria_Lello_at_night.jpg",
             "desc": "세계에서 가장 아름다운 서점 중 하나로 꼽히는 렐루 서점은 해리 포터 시리즈의 영감을 준 곳으로도 유명합니다. 환상적인 계단과 스테인드글라스 천장이 인상적입니다.",
             "why": "동화 같은 건축물, 해리 포터 팬들에게는 성지 같은 곳.",
             "tip": "입장하려면 티켓을 구매해야 하며, 긴 줄을 피하려면 아침 일찍 방문하거나 온라인으로 미리 예약하는 것이 좋습니다."},
            {"name": "도루 밸리 (Douro Valley)", "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ef/Douro_Valley_view.jpg/1200px-Douro_Valley_view.jpg",
             "desc": "포르투에서 동쪽으로 약 100km 떨어진 도루 밸리는 포트 와인의 본고장으로 유네스코 세계문화유산에 등재되어 있습니다. 계단식 포도밭이 강을 따라 그림처럼 펼쳐져 있으며, 와이너리 투어와 강 크루즈를 즐길 수 있습니다.",
             "why": "세계적인 와인 산지, stunning한 자연경관, 와인 시음 체험.",
             "tip": "포르투에서 당일치기 투어나 1박 2일 일정으로 방문하는 것을 추천합니다. 와인 투어와 함께 강 크루즈를 즐겨보세요."}
        ]
    },
    "알가르베": {
        "coords": [37.0194, -7.9304],
        "description": "포르투갈 남부의 알가르베는 황금빛 해변, 드라마틱한 절벽, 에메랄드빛 바다가 어우러진 최고의 휴양지입니다. 일광욕, 수상 스포츠, 골프 등을 즐기기에 이상적인 곳입니다.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b3/Praia_da_Marinha_Algarve_Portugal.jpg/1200px-Praia_da_Marinha_Algarve_Portugal.jpg",
        "attractions": [
            {"name": "라고스 (Lagos)", "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Lagos_coastline_Portugal.jpg/1200px-Lagos_coastline_Portugal.jpg",
             "desc": "알가르베 서부에 위치한 라고스는 아름다운 해변과 독특한 해안 절벽, 그리고 역사적인 구시가지가 조화를 이룹니다. 폰타 다 피에다드(Ponta da Piedade)의 동굴과 기암괴석은 꼭 방문해야 할 명소입니다.",
             "why": "숨 막히는 해안 절경, 보트 투어, 매력적인 마을 분위기.",
             "tip": "폰타 다 피에다드에서는 보트 투어를 통해 절벽 사이의 동굴을 탐험하거나, 카약이나 SUP를 대여하여 직접 즐길 수 있습니다."},
            {"name": "파루 (Faro)", "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f6/Faro_Old_Town_and_Marina.jpg/1200px-Faro_Old_Town_and_Marina.jpg",
             "desc": "알가르베 지방의 주도인 파루는 국제 공항이 있어 많은 여행객들이 처음으로 도착하는 곳입니다. 매력적인 구시가지, 아름다운 대성당, 그리고 리아 포르모사 자연 공원(Parque Natural da Ria Formosa)이 유명합니다.",
             "why": "평화로운 분위기, 아름다운 자연 보호 구역, 접근성.",
             "tip": "리아 포르모사 자연 공원은 보트 투어를 통해 방문할 수 있으며, 다양한 조류와 독특한 생태계를 관찰할 수 있습니다."},
            {"name": "베나길 동굴 (Benagil Cave)", "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Benagil_Cave.jpg/1200px-Benagil_Cave.jpg",
             "desc": "아름다운 해안선에 숨겨진 베나길 동굴은 동굴 천장에 구멍이 뚫려 있어 햇빛이 쏟아져 들어오는 신비로운 공간입니다. 보트, 카약, 또는 SUP를 이용하여 접근할 수 있습니다.",
             "why": "자연이 만들어낸 경이로운 풍경, 잊을 수 없는 경험.",
             "tip": "동굴 안으로 들어가려면 보트 투어를 이용하거나, 직접 카약이나 SUP를 타고 가는 방법이 있습니다. 파도가 높으면 접근이 어려울 수 있으니 날씨를 확인하세요."}
        ]
    },
    "코임브라": {
        "coords": [40.2056, -8.4196],
        "description": "포르투갈에서 가장 오래된 대학이 있는 코임브라는 유서 깊은 대학 도시입니다. 조아니나 도서관은 세계에서 가장 아름다운 도서관 중 하나로 꼽힙니다.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/14/Coimbra_University_Library.jpg/1200px-Coimbra_University_Library.jpg",
        "attractions": [
            {"name": "코임브라 대학교 (University of Coimbra)", "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b5/Universidade_de_Coimbra_%281%29.jpg/1200px-Universidade_de_Coimbra_%281%29.jpg",
             "desc": "포르투갈에서 가장 오래되고 권위 있는 대학입니다. 유네스코 세계문화유산으로 지정되어 있으며, 특히 바로크 양식의 조아니나 도서관(Biblioteca Joanina)은 필수로 방문해야 할 곳입니다.",
             "why": "유서 깊은 대학 분위기, 세계적으로 아름다운 도서관.",
             "tip": "조아니나 도서관은 입장 시간이 제한적이며, 사전 예약이 필수일 수 있습니다. 학생들의 전통 복장을 찾아보고 사진을 찍어보세요."},
            {"name": "산타 크루즈 수도원 (Santa Cruz Monastery)", "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/fb/Coimbra_-_Mosteiro_de_Santa_Cruz_-_20150917.jpg/1200px-Mosteiro_de_Santa_Cruz_-_20150917.jpg",
             "desc": "코임브라의 중요한 역사적 종교 건축물로, 포르투갈의 첫 두 국왕이 안치되어 있습니다. 아름다운 예배당과 회랑을 감상할 수 있습니다.",
             "why": "포르투갈 초기 역사와 종교 예술의 정수.",
             "tip": "대학과 함께 구시가지 내에 있어 도보로 둘러보기 좋습니다. 파두 공연을 하는 곳도 인근에 있습니다."}
        ]
    },
    "에보라": {
        "coords": [38.5667, -7.9083],
        "description": "유네스코 세계문화유산 도시인 에보라는 고대 로마 시대의 유적과 중세 시대의 건축물들이 잘 보존되어 있습니다.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e6/Roman_Temple_of_Évora.jpg/1200px-Roman_Temple_of_Évora.jpg",
        "attractions": [
            {"name": "로마 신전 (Roman Temple of Évora)", "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e6/Roman_Temple_of_Évora.jpg/1200px-Roman_Temple_of_Évora.jpg",
             "desc": "에보라의 상징 중 하나인 고대 로마 신전입니다. 포르투갈에서 가장 잘 보존된 로마 유적 중 하나로, 과거의 번성했던 시대를 엿볼 수 있습니다.",
             "why": "2천 년 전 로마의 숨결을 느낄 수 있는 역사 유적.",
             "tip": "신전 주변에 공원이 있어 잠시 쉬어가기 좋습니다. 밤에는 조명이 켜져 또 다른 매력을 뽐냅니다."},
            {"name": "해골 예배당 (Capela dos Ossos)", "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/Chapel_of_Bones%2C_Evora.jpg/1200px-Chapel_of_Bones%2C_Evora.jpg",
             "desc": "'우리의 뼈는 너희가 될 뼈보다 낫다'라는 문구가 인상적인 독특한 예배당입니다. 수천 명의 수도사 해골과 뼈로 장식되어 있습니다.",
             "why": "독특하고 섬뜩하지만 잊을 수 없는 경험.",
             "tip": "사진 촬영은 가능하지만, 경건한 마음으로 관람하는 것이 좋습니다. 다소 충격적일 수 있으니 마음의 준비를 하세요."},
            {"name": "에보라 대성당 (Évora Cathedral)", "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/30/Cathedral_of_%C3%89vora_-_Portugal.jpg/1200px-Cathedral_of_%C3%89vora_-_Portugal.jpg",
             "desc": "에보라의 가장 높은 곳에 위치한 중세 시대의 대성당입니다. 다양한 건축 양식이 혼합되어 있으며, 지붕 위로 올라가면 에보라 시내를 한눈에 조망할 수 있습니다.",
             "why": "에보라의 랜드마크, 아름다운 건축물, 멋진 전망.",
             "tip": "대성당의 박물관과 지붕 투어를 함께 즐기는 것을 추천합니다."}
        ]
    },
    "오비두스": {
        "coords": [39.3624, -9.1578],
        "description": "성벽으로 둘러싸인 그림 같은 중세 마을 오비두스는 포르투갈의 가장 아름다운 마을 중 하나로 꼽힙니다.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Obidos_Castle.jpg/1200px-Obidos_Castle.jpg",
        "attractions": [
            {"name": "오비두스 성벽 (Óbidos Castle Walls)", "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Obidos_Castle.jpg/1200px-Obidos_Castle.jpg",
             "desc": "마을을 둘러싸고 있는 견고한 중세 성벽 위를 걸으며 마을 전체와 주변 전경을 감상할 수 있습니다.",
             "why": "동화 같은 마을 전경 감상, 독특한 경험.",
             "tip": "성벽 위는 난간이 없는 구간이 있으니 안전에 유의해야 합니다. 한 바퀴 도는 데 약 1시간 정도 걸립니다."},
            {"name": "오비두스 마을 (Óbidos Village)", "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/36/Rua_Direita_Obidos_Portugal.jpg/1200px-Rua_Direita_Obidos_Portugal.jpg",
             "desc": "하얀 벽에 파란색, 노란색 테두리가 칠해진 아기자기한 집들과 꽃으로 장식된 골목길이 매력적인 마을입니다. 작은 상점과 카페, 교회 등이 아기자기하게 모여 있습니다.",
             "why": "낭만적인 중세 분위기, 예쁜 사진 스팟.",
             "tip": "오비두스 특산품인 체리 리큐어 '진자(Ginja)'를 초콜릿 컵에 담아 마셔보세요. 곳곳의 상점에서 판매합니다."}
        ]
    },
    "아베이루": {
        "coords": [40.6405, -8.6538],
        "description": "'포르투갈의 베니스'라고 불리는 아베이루는 다채로운 색깔의 전통 보트 '몰리세이루(Moliceiro)'가 운하를 따라 오가는 모습이 인상적입니다.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/18/Aveiro_Canal.jpg/1200px-Aveiro_Canal.jpg",
        "attractions": [
            {"name": "몰리세이루 보트 투어 (Moliceiro Boat Tour)", "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Moliceiro_boats_in_Aveiro.jpg/1200px-Moliceiro_boats_in_Aveiro.jpg",
             "desc": "화려한 색깔의 전통 보트 몰리세이루를 타고 아베이루의 운하를 따라 도시를 둘러보는 것은 필수적인 경험입니다.",
             "why": "아베이루의 상징적인 경험, 아름다운 운하 풍경.",
             "tip": "다양한 투어 업체가 있으며, 보통 45분 정도 소요됩니다. 보트 위에서 사진 찍기 좋아요."},
            {"name": "코스타 노바 (Costa Nova)", "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Costa_Nova_Beach%2C_Portugal.jpg/1200px-Costa_Nova_Beach%2C_Portugal.jpg",
             "desc": "아베이루에서 가까운 해변 마을로, 줄무늬 패턴의 형형색색의 집들이 늘어서 있어 이국적인 풍경을 자랑합니다.",
             "why": "독특한 건축 양식의 아름다운 해변 마을, 사진 스팟.",
             "tip": "아베이루 시내에서 버스로 쉽게 이동할 수 있습니다. 여름에는 해변에서 휴식을 취하기 좋습니다."},
            {"name": "오보스 몰레스 (Ovos Moles)", "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/90/OvosMoles.jpg/800px-OvosMoles.jpg",
             "desc": "아베이루의 대표적인 전통 디저트로, 달걀 노른자와 설탕으로 만든 달콤한 소를 얇은 쌀 웨이퍼로 감싼 과자입니다. 조개껍데기, 생선 등 다양한 모양이 있습니다.",
             "why": "아베이루에서만 맛볼 수 있는 특별한 간식.",
             "tip": "운하 주변의 제과점이나 기념품 가게에서 쉽게 찾을 수 있습니다. 선물용으로도 좋습니다."}
        ]
    }
}


# --- Itinerary Recommendation Logic (New) ---
def recommend_itinerary(city, companion, duration):
    itineraries = {
        "리스본": {
            "혼자": {
                "3-4일": """
                <h4>✔️ 리스본 집중 혼자 여행 3박 4일 코스 (자유로운 탐험)</h4>
                <ul>
                    <li><b>1일차:</b> 리스본 도착, 숙소 체크인. 오후: 알파마 지구 (좁은 골목길, 전망대) 자유롭게 탐험, 길거리 파두 음악 감상, 혼밥 즐기기.</li>
                    <li><b>2일차:</b> 벨렘 지구 (제로니무스 수도원, 벨렘 탑, 발견 기념비). Pastéis de Belém에서 에그 타르트 맛보기. 오후: 바이샤-시아두 지구에서 쇼핑 및 카페에서 여유 즐기기.</li>
                    <li><b>3일차:</b> 신트라 당일치기 (페나 궁전, 킨타 다 헤갈레이라). 리스본으로 돌아와 타임아웃 마켓 등에서 다양한 음식 시도.</li>
                    <li><b>4일차:</b> 자유 시간 (박물관, 거리 예술 탐방) 및 출국.</li>
                </ul>
                <p>💡 <b>팁:</b> 리스본은 혼자 여행하기에 매우 안전하고 편안한 도시입니다. 대중교통이 잘 되어 있어 자유롭게 이동하며 도시의 매력을 느낄 수 있습니다. 걷는 것을 즐긴다면 더 많은 것을 발견할 수 있어요.</p>
                """,
                "5-7일": """
                <h4>✔️ 리스본 & 근교 혼자 여행 5박 7일 코스 (깊이 있는 경험)</h4>
                <ul>
                    <li><b>1-3일차:</b> 위 리스본 3-4일 코스와 동일.</li>
                    <li><b>4일차:</b> 카스카이스 & 에스토릴 해안가 당일치기. 자전거 대여하여 해안가를 따라 달리거나, 여유롭게 해변에서 휴식.</li>
                    <li><b>5일차:</b> 파두 박물관 방문 및 리스본 시내의 숨겨진 골목길 탐방. 저녁: 현지인들이 가는 작은 레스토랑에서 진정한 포르투갈 음식 경험.</li>
                    <li><b>6일차:</b> 몬산토 파노라마 시티 공원 (Parque Florestal de Monsanto)에서 자연 즐기기 또는 리스본 근교의 작은 마을 방문.</li>
                    <li><b>7일차:</b> 자유 시간 (쇼핑, 기념품 구매) 및 출국.</li>
                </ul>
                <p>💡 <b>팁:</b> 여유롭게 5-7일을 보내면 리스본의 다양한 면모를 경험할 수 있습니다. 근교로의 당일치기 여행은 색다른 풍경을 제공하며, 혼자만의 시간을 가지기 좋습니다.</p>
                """
            },
            "연인": {
                "3-4일": """
                <h4>✔️ 리스본 연인과 함께하는 3박 4일 로맨틱 코스</h4>
                <ul>
                    <li><b>1일차:</b> 리스본 도착, 로맨틱한 호텔 체크인. 오후: 알파마 지구에서 함께 산책하며 리스본의 정취 만끽, 상 조르제 성에서 아름다운 일몰 감상. 저녁: 파두 공연과 함께하는 로맨틱 디너.</li>
                    <li><b>2일차:</b> 벨렘 지구 (제로니무스 수도원, 벨렘 탑) 방문 후 오리지널 에그 타르트 맛보기. 오후: 리스본 시내 (바이샤-시아두)에서 커플 쇼핑 및 트램 28번 탑승.</li>
                    <li><b>3일차:</b> 신트라 당일치기 (페나 궁전, 킨타 다 헤갈레이라). 동화 같은 분위기에서 함께 사진 찍기. 저녁: 리스본의 루프탑 바에서 야경과 칵테일 즐기기.</li>
                    <li><b>4일차:</b> 여유로운 아침, 카페에서 브런치. 공항으로 이동 및 출국.</li>
                </ul>
                <p>💡 <b>팁:</b> 리스본의 언덕길과 아름다운 전망대는 연인에게 잊지 못할 추억을 선사합니다. 미리 파두 공연이나 인기 레스토랑을 예약하는 것이 좋습니다.</p>
                """,
                "5-7일": """
                <h4>✔️ 리스본 & 근교 연인과 함께하는 5박 7일 특별 코스</h4>
                <ul>
                    <li><b>1-3일차:</b> 위 연인 3-4일 코스와 동일.</li>
                    <li><b>4일차:</b> 포르투갈 최서단 '카보 다 로카(Cabo da Roca)' 방문 후 신트라 근처 에스토릴이나 카스카이스 해변에서 로맨틱한 오후 보내기.</li>
                    <li><b>5일차:</b> 리스본 현대 미술관 또는 국립 타일 박물관 방문. 테주 강변에서 자전거 데이트 또는 강 크루즈. 저녁: 미슐랭 스타 레스토랑 또는 고급 해산물 식당 방문.</li>
                    <li><b>6일차:</b> 세투발(Setúbal) 또는 아라비다 자연 공원(Arrábida Natural Park)으로 당일치기 여행. 아름다운 해변에서 수영 또는 돌고래 관찰 투어.</li>
                    <li><b>7일차:</b> 리스본 재래시장(Feira da Ladra) 구경 후 공항으로 이동 및 출국.</li>
                </ul>
                <p>💡 <b>팁:</b> 리스본 근교는 아름다운 자연과 해변이 많아 연인과 함께 여유롭고 특별한 시간을 보내기 좋습니다. 프라이빗 투어나 고급 레스토랑을 예약하여 더 특별한 추억을 만들어보세요.</p>
                """
            },
            "친구": {
                "3-4일": """
                <h4>✔️ 리스본 친구들과 함께하는 3박 4일 활기찬 코스</h4>
                <ul>
                    <li><b>1일차:</b> 리스본 도착, 숙소 체크인. 오후: 바이샤-시아두 지구에서 쇼핑 및 거리 공연 감상. 저녁: 바비큐(Frango Piri-Piri)와 함께 현지 맥주 즐기기, Bairro Alto에서 밤문화 즐기기.</li>
                    <li><b>2일차:</b> 벨렘 지구 (제로니무스 수도원, 벨렘 탑) 방문. 리스본의 트렌디한 타임아웃 마켓(Time Out Market)에서 다양한 음식 맛보기.</li>
                    <li><b>3일차:</b> 신트라 당일치기 (페나 궁전, 무어 성). 리스본으로 돌아와 LX 팩토리에서 젊은 감성 느끼기.</li>
                    <li><b>4일차:</b> 자유 시간 (스트릿 아트 투어, 기념품 쇼핑) 및 출국.</li>
                </ul>
                <p>💡 <b>팁:</b> 리스본은 친구들과 함께 즐길 거리가 많습니다. 대중교통을 이용해 돌아다니고, 밤에는 활기찬 분위기를 만끽해보세요.</p>
                """,
                "5-7일": """
                <h4>✔️ 리스본 & 근교 친구들과 함께하는 5박 7일 어드벤처 코스</h4>
                <ul>
                    <li><b>1-3일차:</b> 위 친구 3-4일 코스와 동일.</li>
                    <li><b>4일차:</b> 서핑으로 유명한 에리세이라(Ericeira) 또는 페니셰(Peniche) 당일치기. 서핑 체험 또는 해변에서 파티 즐기기.</li>
                    <li><b>5일차:</b> 리스본의 현대적이고 활기찬 파르크 다스 나소에스(Parque das Nações) 지구 방문. 리스본 해양 수족관(Oceanário de Lisboa) 방문.</li>
                    <li><b>6일차:</b> 포르투갈 전통 음식 쿠킹 클래스 참여 또는 푸드 투어. 오후: 리스본 전망대 투어 (미라두루 다스 포르타스 두 솔, 미라두루 다 그라사).</li>
                    <li><b>7일차:</b> 자유 시간 및 출국.</li>
                </ul>
                <p>💡 <b>팁:</b> 액티비티를 좋아하는 친구들이라면 서핑, 해변 파티 등을 추가하여 즐거움을 더할 수 있습니다. 현지 투어를 예약하거나 직접 차를 렌트하여 자유로운 여행을 계획해 보세요.</p>
                """
            },
            "가족": {
                "3-4일": """
                <h4>✔️ 리스본 가족과 함께하는 3박 4일 편안한 코스</h4>
                <ul>
                    <li><b>1일차:</b> 리스본 도착, 가족 숙소 체크인. 오후: 리스본 대성당, 코메르시우 광장 등 평지 위주로 관광. 강변에서 여유로운 시간.</li>
                    <li><b>2일차:</b> 벨렘 지구 (제로니무스 수도원 외관, 벨렘 탑 외관). 넓은 공원에서 아이들과 휴식. 파스텔 드 나타 맛보기. 오후: 리스본 해양 수족관(Oceanário de Lisboa) 방문 (아이들이 좋아할 만한 곳).</li>
                    <li><b>3일차:</b> 신트라 (페나 궁전, 무어 성) 방문 시 버스나 택시 이용 권장. 무리하지 않고 가족의 컨디션에 맞춰 관광.</li>
                    <li><b>4일차:</b> 자유 시간 (아이들을 위한 공원, 놀이 공간) 및 출국.</li>
                </ul>
                <p>💡 <b>팁:</b> 리스본은 언덕이 많으므로 유모차나 어린아이를 동반한 가족이라면 대중교통 이용 시 동선을 잘 계획하는 것이 좋습니다. 해양 수족관은 아이들이 정말 좋아할 만한 장소입니다.</p>
                """,
                "5-7일": """
                <h4>✔️ 리스본 & 근교 가족과 함께하는 5박 7일 맞춤형 코스</h4>
                <ul>
                    <li><b>1-3일차:</b> 위 가족 3-4일 코스와 동일.</li>
                    <li><b>4일차:</b> 리스본 근교 해변 (카스카이스, 에스토릴) 방문. 모래놀이, 해변 레스토랑에서 신선한 해산물 식사.</li>
                    <li><b>5일차:</b> 셋째 날 방문하지 못한 리스본 내 명소 방문 (국립 타일 박물관 등). 리스본 동물원(Jardim Zoológico de Lisboa) 방문.</li>
                    <li><b>6일차:</b> 에보라 당일치기 (로마 신전, 대성당). 해골 예배당은 가족 구성원에 따라 고려.</li>
                    <li><b>7일차:</b> 자유 시간 (아이들과 함께 재래시장 방문, 현지 베이커리 체험) 및 출국.</li>
                </ul>
                <p>💡 <b>팁:</b> 가족 여행은 여유롭고 유연한 일정이 중요합니다. 아이들의 흥미를 끌 만한 장소를 적절히 배치하고, 쉬는 시간을 충분히 확보하는 것이 좋습니다.</p>
                """
            }
        },
        "포르투": {
            "혼자": {
                "3-4일": """
                <h4>✔️ 포르투 집중 혼자 여행 3박 4일 코스 (와인 & 문화 탐험)</h4>
                <ul>
                    <li><b>1일차:</b> 포르투 도착, 숙소 체크인. 오후: 리베이라 지구 자유롭게 탐험, 동 루이스 1세 다리 상층부 걷기. 저녁: 현지 맛집에서 혼밥, 강변의 야경 감상.</li>
                    <li><b>2일차:</b> 빌라 노바 드 가이아로 이동하여 포트 와인 셀러 투어 및 시음. 렐루 서점, 클레리구스 탑 방문.</li>
                    <li><b>3일차:</b> 도루 밸리 당일치기 투어 (포도밭 풍경 감상, 와이너리 방문 및 시음).</li>
                    <li><b>4일차:</b> 자유 시간 (볼량 시장 구경, 아줄레주 건축물 감상) 및 출국.</li>
                </ul>
                <p>💡 <b>팁:</b> 포르투는 혼자 여행하며 와인과 문화를 깊이 있게 경험하기 좋은 도시입니다. 도보로 충분히 둘러볼 수 있어 편리합니다.</p>
                """,
                "5-7일": """
                <h4>✔️ 포르투 & 북부 혼자 여행 5박 7일 코스 (북부 심층 탐험)</h4>
                <ul>
                    <li><b>1-3일차:</b> 위 포르투 3-4일 코스와 동일.</li>
                    <li><b>4일차:</b> 브라가(Braga) & 기마랑이스(Guimarães) 당일치기. 포르투갈의 역사와 종교 중심지 탐방.</li>
                    <li><b>5일차:</b> 포르투 미술관 또는 현대 미술관 방문. 리스본과 다른 포르투만의 파두 공연 관람.</li>
                    <li><b>6일차:</b> 북부 해안 도시 (예: 비아나 두 카스텔루 Viana do Castelo) 방문하여 해변 풍경 감상 및 해산물 요리 즐기기.</li>
                    <li><b>7일차:</b> 자유 시간 및 출국.</li>
                </ul>
                <p>💡 <b>팁:</b> 포르투갈 북부는 역사적인 도시와 아름다운 자연이 많아 혼자서 여유롭게 탐험하기 좋습니다. 기차나 버스를 이용한 당일치기 여행이 편리합니다.</p>
                """
            },
            "연인": {
                "3-4일": """
                <h4>✔️ 포르투 연인과 함께하는 3박 4일 로맨틱 와인 코스</h4>
                <ul>
                    <li><b>1일차:</b> 포르투 도착, 숙소 체크인. 오후: 리베이라 지구 산책, 도루 강변 레스토랑에서 로맨틱 디너. 밤: 동 루이스 1세 다리에서 야경 감상.</li>
                    <li><b>2일차:</b> 빌라 노바 드 가이아의 포트 와인 셀러 투어 및 프라이빗 시음. 오후: 렐루 서점 방문, 클레리구스 탑에서 함께 포르투 전경 감상.</li>
                    <li><b>3일차:</b> 도루 밸리 와이너리 투어 (전용 차량 또는 소그룹 투어 추천) 및 와인 테이스팅. 강 크루즈를 하며 로맨틱한 시간.</li>
                    <li><b>4일차:</b> 포르투 자유 시간 (강변 카페에서 브런치) 및 출국.</li>
                </ul>
                <p>💡 <b>팁:</b> 포르투는 와인과 함께 로맨틱한 분위기를 만끽하기 좋습니다. 도루 밸리 투어는 꼭 연인과 함께해보세요.</p>
                """,
                "5-7일": """
                <h4>✔️ 포르투 & 북부 연인과 함께하는 5박 7일 프리미엄 코스</h4>
                <ul>
                    <li><b>1-3일차:</b> 위 연인 3-4일 코스와 동일.</li>
                    <li><b>4일차:</b> 아베이루(Aveiro) 당일치기. 몰리세이루 보트 투어와 스트라이프 하우스(코스타 노바)에서 예쁜 사진 남기기.</li>
                    <li><b>5일차:</b> 북부의 숨겨진 보석 같은 마을 탐방 (예: 브라가 봉 제수 do 몬테 - Bom Jesus do Monte). 조용한 곳에서 둘만의 시간.</li>
                    <li><b>6일차:</b> 포르투 도심에서 스파 또는 마사지. 저녁: 고급 해산물 레스토랑 또는 미슐랭 식당 방문.</li>
                    <li><b>7일차:</b> 자유 시간 및 출국.</li>
                </ul>
                <p>💡 <b>팁:</b> 다양한 테마의 도시를 함께 방문하며 색다른 경험을 할 수 있습니다. 연인과 함께 휴식과 미식을 즐기는 데 초점을 맞춰보세요.</p>
                """
            },
            "친구": {
                "3-4일": """
                <h4>✔️ 포르투 친구들과 함께하는 3박 4일 즐거운 코스</h4>
                <ul>
                    <li><b>1일차:</b> 포르투 도착, 숙소 체크인. 오후: 리베이라 지구 탐험, 동 루이스 1세 다리 위에서 사진 찍기. 저녁: 강변의 펍이나 바에서 현지 맥주 즐기기.</li>
                    <li><b>2일차:</b> 포트 와인 셀러 투어 (여러 와이너리 방문) 및 비교 시음. 렐루 서점, 클레리구스 탑.</li>
                    <li><b>3일차:</b> 도루 밸리 와인 투어 (활동적인 투어, 카누 또는 카약 체험 포함).</li>
                    <li><b>4일차:</b> 자유 시간 (볼량 시장에서 현지 음식 탐험) 및 출국.</li>
                </ul>
                <p>💡 <b>팁:</b> 와인을 좋아하는 친구들과 함께라면 포르투와 도루 밸리는 최고의 선택입니다. 활기찬 밤문화도 놓치지 마세요.</p>
                """,
                "5-7일": """
                <h4>✔️ 포르투 & 북부 친구들과 함께하는 5박 7일 익사이팅 코스</h4>
                <ul>
                    <li><b>1-3일차:</b> 위 친구 3-4일 코스와 동일.</li>
                    <li><b>4일차:</b> 게레스 국립공원(Parque Nacional da Peneda-Gerês)에서 하이킹, 폭포 수영 등 액티비티 즐기기.</li>
                    <li><b>5일차:</b> 비아나 두 카스텔루(Viana do Castelo) 방문하여 해변 스포츠 체험 또는 서핑 배우기.</li>
                    <li><b>6일차:</b> 포르투 시내에서 쿠킹 클래스 참여 또는 푸드 투어. 저녁: 현지 라이브 음악 공연 감상.</li>
                    <li><b>7일차:</b> 자유 시간 및 출국.</li>
                </ul>
                <p>💡 <b>팁:</b> 포르투갈 북부의 자연은 친구들과 함께 액티브한 활동을 즐기기에 좋습니다. 다양한 액티비티를 통해 잊지 못할 추억을 만들어보세요.</p>
                """
            },
            "가족": {
                "3-4일": """
                <h4>✔️ 포르투 가족과 함께하는 3박 4일 편안한 코스</h4>
                <ul>
                    <li><b>1일차:</b> 포르투 도착, 가족 숙소 체크인. 오후: 리베이라 지구 산책, 동 루이스 1세 다리 하층부 건너기. 아이들을 위한 강변 아이스크림 가게 방문.</li>
                    <li><b>2일차:</b> 빌라 노바 드 가이아의 포트 와인 셀러 중 아이들이 참여할 수 있는 곳 방문 (일부 셀러는 주스 시음도 가능). 오후: 렐루 서점 (오픈 시간 확인 후 방문), 클레리구스 탑 (어린아이 동반 시 고려).</li>
                    <li><b>3일차:</b> 도루 밸리 당일치기 (여유로운 기차 이동 또는 프라이빗 투어 추천). 유람선 탑승하여 강변 풍경 즐기기.</li>
                    <li><b>4일차:</b> 자유 시간 (볼량 시장 등에서 아이들과 함께 즐길 수 있는 것 찾기) 및 출국.</li>
                </ul>
                <p>💡 <b>팁:</b> 포르투는 언덕이 많지만, 강변이나 평지 위주로 다니면 가족 여행객도 편리합니다. 아이들과 함께 즐길 수 있는 와이너리나 크루즈를 선택하세요.</p>
                """,
                "5-7일": """
                <h4>✔️ 포르투 & 근교 가족과 함께하는 5박 7일 맞춤형 코스</h4>
                <ul>
                    <li><b>1-3일차:</b> 위 가족 3-4일 코스와 동일.</li>
                    <li><b>4일차:</b> 아베이루(Aveiro) 당일치기. 몰리세이루 보트 투어와 코스타 노바의 줄무늬 집들 구경은 아이들도 좋아할 만합니다. 오보스 몰레스 맛보기.</li>
                    <li><b>5일차:</b> 포르투 시내의 보태니컬 가든(Jardim Botânico do Porto)이나 크리스탈 팰리스 정원(Jardins do Palácio de Cristal)에서 피크닉.</li>
                    <li><b>6일차:</b> 비아나 두 카스텔루(Viana do Castelo) 또는 인근 해변 마을에서 해변에서 시간 보내기.</li>
                    <li><b>7일차:</b> 자유 시간 및 출국.</li>
                </ul>
                <p>💡 <b>팁:</b> 포르투 근교 여행은 가족 단위로도 좋습니다. 아베이루의 보트 투어는 특히 아이들에게 인기 만점입니다. 해변에서 쉬는 시간도 충분히 넣어주세요.</p>
                """
            }
        },
        "알가르베": {
            "혼자": {
                "3-4일": """
                <h4>✔️ 알가르베 집중 혼자 여행 3박 4일 코스 (자연 & 휴식)</h4>
                <ul>
                    <li><b>1일차:</b> 파루 도착 후 라고스 이동. 숙소 체크인. 오후: 라고스 해변 (Praia Dona Ana, Praia do Camilo)에서 휴식, 혼자만의 시간.</li>
                    <li><b>2일차:</b> 폰타 다 피에다드(Ponta da Piedade) 카약 또는 SUP 투어 (혼자서 즐기기 좋음). 오후: 라고스 구시가지 탐험, 현지 시장 구경.</li>
                    <li><b>3일차:</b> 베나길 동굴 보트 투어. 이후 인근의 한적한 해변에서 여유롭게 일광욕 즐기기.</li>
                    <li><b>4일차:</b> 자유 시간 (해변 산책, 카페에서 독서) 및 출국.</li>
                </ul>
                <p>💡 <b>팁:</b> 알가르베는 혼자서도 안전하고 평화롭게 휴식을 취하기 좋은 곳입니다. 해변에서 여유를 만끽하거나, 액티비티를 즐기며 자유로운 시간을 보내세요.</p>
                """,
                "5-7일": """
                <h4>✔️ 알가르베 & 근교 혼자 여행 5박 7일 코스 (다채로운 경험)</h4>
                <ul>
                    <li><b>1-3일차:</b> 위 혼자 여행 3-4일 코스와 동일.</li>
                    <li><b>4일차:</b> 파루(Faro)로 이동하여 리아 포르모사 자연 공원 보트 투어. 파루 구시가지 탐험.</li>
                    <li><b>5일차:</b> 실베스(Silves) 방문. 이슬람 시대의 성과 대성당 구경. 이후 모나치케(Monchique) 산에서 하이킹 또는 온천 방문.</li>
                    <li><b>6일차:</b> 타비라(Tavira) 또는 오량(Olhão)과 같은 동부 알가르베의 매력적인 마을 탐방. 현지 어촌의 분위기 느끼기.</li>
                    <li><b>7일차:</b> 자유 시간 및 출국.</li>
                </ul>
                <p>💡 <b>팁:</b> 알가르베는 다양한 해변과 역사적인 마을, 그리고 자연 보호 구역이 있어 혼자서도 다채로운 경험을 할 수 있습니다. 차 렌트를 고려하면 이동이 더욱 편리합니다.</p>
                """
            },
            "연인": {
                "3-4일": """
                <h4>✔️ 알가르베 연인과 함께하는 3박 4일 로맨틱 해변 코스</h4>
                <ul>
                    <li><b>1일차:</b> 파루 도착 후 라고스 이동. 숙소 체크인. 오후: 라고스 해변에서 로맨틱한 일몰 감상. 저녁: 해변가 레스토랑에서 신선한 해산물 디너.</li>
                    <li><b>2일차:</b> 폰타 다 피에다드 보트 투어 또는 전용 카약 투어. 베나길 동굴 방문. 아름다운 해변에서 커플 사진 찍기.</li>
                    <li><b>3일차:</b> 카르보에이루(Carvoeiro) 또는 알부페이라(Albufeira) 등 다른 해변 마을 탐방. 해변에서 여유롭게 휴식 또는 패들 보트 즐기기.</li>
                    <li><b>4일차:</b> 자유 시간 및 출국.</li>
                </ul>
                <p>💡 <b>팁:</b> 알가르베의 아름다운 해변과 동굴은 연인에게 최고의 로맨틱 배경을 제공합니다. 해변에서 함께 여유로운 시간을 보내고, 맛있는 해산물을 즐기세요.</p>
                """,
                "5-7일": """
                <h4>✔️ 알가르베 연인과 함께하는 5박 7일 프리미엄 휴양 코스</h4>
                <ul>
                    <li><b>1-3일차:</b> 위 연인 3-4일 코스와 동일.</li>
                    <li><b>4일차:</b> 파루(Faro) 또는 타비라(Tavira)로 이동하여 숙소 변경. 리아 포르모사 자연 공원 보트 투어 또는 프라이빗 아일랜드 투어.</li>
                    <li><b>5일차:</b> 고급 스파 또는 마사지. 골프를 좋아한다면 골프 코스 방문. 저녁: 와인 페어링이 있는 고급 레스토랑 방문.</li>
                    <li><b>6일차:</b> 알가르베 내 숨겨진 로맨틱 해변 탐방 (예: Praia do Barranco, Praia da Ursa). 와이너리 투어 및 시음.</li>
                    <li><b>7일차:</b> 자유 시간 및 출국.</li>
                </ul>
                <p>💡 <b>팁:</b> 알가르베는 다양한 고급 리조트와 스파가 많아 연인과 함께 편안하고 럭셔리한 휴가를 보내기에 적합합니다. 렌터카를 이용하면 더욱 편리하게 이동할 수 있습니다.</p>
                """
            },
            "친구": {
                "3-4일": """
                <h4>✔️ 알가르베 친구들과 함께하는 3박 4일 액티브 코스</h4>
                <ul>
                    <li><b>1일차:</b> 파루 도착 후 라고스 이동. 숙소 체크인. 오후: 라고스 해변에서 물놀이 또는 서핑 레슨. 저녁: 해변 바에서 파티 즐기기.</li>
                    <li><b>2일차:</b> 폰타 다 피에다드 보트 투어 또는 카약 체험. 베나길 동굴 방문. 해변에서 비치 발리볼 등 액티비티.</li>
                    <li><b>3일차:</b> 알부페이라(Albufeira) 또는 빌라모우라(Vilamoura) 방문. 수상 스포츠 (제트스키, 패러세일링 등) 즐기기. 밤: 활기찬 나이트라이프 경험.</li>
                    <li><b>4일차:</b> 자유 시간 및 출국.</li>
                </ul>
                <p>💡 <b>팁:</b> 알가르베는 친구들과 함께 다양한 수상 스포츠와 활기찬 밤문화를 즐기기에 좋습니다. 여러 명이 함께 할 수 있는 투어를 알아보세요.</p>
                """,
                "5-7일": """
                <h4>✔️ 알가르베 친구들과 함께하는 5박 7일 익스트림 & 즐거움 코스</h4>
                <ul>
                    <li><b>1-3일차:</b> 위 친구 3-4일 코스와 동일.</li>
                    <li><b>4일차:</b> 모나치케(Monchique) 산에서 하이킹 또는 짚라인 체험. 스파에서 휴식.</li>
                    <li><b>5일차:</b> 세비야(Seville, 스페인) 당일치기 여행. 고속 기차 또는 버스를 이용해 이웃 나라 문화 체험.</li>
                    <li><b>6일차:</b> 보트 파티 또는 돌고래 관찰 투어. 저녁: 라이브 음악이 있는 해변 레스토랑 방문.</li>
                    <li><b>7일차:</b> 자유 시간 및 출국.</li>
                </ul>
                <p>💡 <b>팁:</b> 알가르베는 스페인과 가까워 국제적인 경험도 가능합니다. 친구들과 함께라면 익스트림 스포츠나 색다른 투어를 시도해 보는 것도 좋습니다.</p>
                """
            },
            "가족": {
                "3-4일": """
                <h4>✔️ 알가르베 가족과 함께하는 3박 4일 즐거운 휴양 코스</h4>
                <ul>
                    <li><b>1일차:</b> 파루 도착 후 숙소 체크인. 숙소 근처 해변에서 아이들과 모래놀이 및 휴식.</li>
                    <li><b>2일차:</b> 베나길 동굴 보트 투어 (안전한 보트 투어 선택). 오후: 대형 워터파크 또는 테마파크 방문 (예: Zoomarine).</li>
                    <li><b>3일차:</b> 라고스(Lagos) 또는 알부페이라(Albufeira) 방문. 해변에서 여유로운 시간, 아이들을 위한 놀이시설 이용.</li>
                    <li><b>4일차:</b> 자유 시간 (아이들과 함께 기념품 쇼핑) 및 출국.</li>
                </ul>
                <p>💡 <b>팁:</b> 알가르베는 가족 친화적인 리조트와 다양한 워터파크가 많아 아이들과 함께 즐거운 시간을 보내기 좋습니다. 안전에 항상 유의하세요.</p>
                """,
                "5-7일": """
                <h4>✔️ 알가르베 가족과 함께하는 5박 7일 풀패키지 휴양 코스</h4>
                <ul>
                    <li><b>1-3일차:</b> 위 가족 3-4일 코스와 동일.</li>
                    <li><b>4일차:</b> 리아 포르모사 자연 공원 보트 투어 (야생 동물 관찰, 한적한 섬 방문).</li>
                    <li><b>5일차:</b> 동부 알가르베의 타비라(Tavira) 방문. 평화로운 분위기에서 역사 지구 탐험 및 해변에서 휴식.</li>
                    <li><b>6일차:</b> 돌고래 관찰 투어 또는 해적선 테마 보트 투어 (아이들에게 인기). 저녁: 가족과 함께 바비큐 파티 즐기기.</li>
                    <li><b>7일차:</b> 자유 시간 (해변에서 마지막 휴식) 및 출국.</li>
                </ul>
                <p>💡 <b>팁:</b> 긴 일정을 잡는다면 알가르베 동부의 한적한 해변과 자연 보호 구역을 방문하는 것도 좋습니다. 아이들의 연령과 흥미에 맞춰 다양한 액티비티를 조합해 보세요.</p>
                """
            }
        }
    }
    return itineraries.get(city, {}).get(companion, {}).get(duration, "선택하신 조건에 맞는 추천 일정이 없습니다. 다른 조합을 시도해 보세요.")


# --- Content Sections ---

if page == "✨ 첫 포르투갈 여행자를 위한 특별 가이드":
    st.markdown("<h2 class='sub-header'>✨ 첫 포르투갈 여행자를 위한 특별 가이드</h2>", unsafe_allow_html=True)
    st.markdown("""
    <p style="font-size:1.2em; text-align:center; background-color:#FFFACD; padding:15px; border-radius:10px; border:2px dashed #FFD700;">
    <b>🎉 포르투갈에 처음 오신 여러분을 진심으로 환영합니다! 🎉</b><br>
    이 가이드는 여러분의 첫 포르투갈 여행을 위한 모든 궁금증을 풀어드리고, 잊지 못할 추억을 만드는 데 필요한 핵심 정보를 담고 있습니다.<br>
    아래 내용을 꼼꼼히 확인하고 즐거운 여행을 준비해 보세요!
    </p>
    """, unsafe_allow_html=True)

    st.markdown("<h3 class='section-header'>🇵🇹 왜 포르투갈인가요? (초보 여행자를 위한 매력)</h3>", unsafe_allow_html=True)
    st.markdown("""
    <ul>
        <li><b>🧡 안전하고 친절한 나라:</b> 포르투갈은 유럽에서 손꼽히는 안전한 국가 중 하나입니다. 현지인들은 여행객에게 매우 친절하고 환대가 넘칩니다. 길을 묻거나 도움을 요청할 때 망설이지 마세요!</li>
        <li><b>💰 합리적인 물가:</b> 서유럽의 다른 인기 여행지에 비해 물가가 저렴한 편이라, 숙박, 식사, 교통 등 전반적인 여행 경비 부담이 적습니다. 여유로운 여행을 즐길 수 있죠.</li>
        <li><b>🌈 다채로운 경험:</b> 짧은 거리 안에 활기찬 수도 리스본, 역사적인 포르투, 동화 같은 신트라, 황금빛 해변의 알가르베 등 다양한 매력을 가진 도시와 자연이 조화롭게 펼쳐져 있습니다. 모든 취향의 여행객을 만족시킬 수 있을 거예요.</li>
        <li><b>☀️ 온화한 기후:</b> 연중 온화한 지중해성 기후로 언제 방문해도 쾌적하게 여행할 수 있습니다. 특히 봄과 가을은 '날씨 맛집'으로 불릴 만큼 완벽해요!</li>
    </ul>
    """, unsafe_allow_html=True)

    st.markdown("<h3 class='section-header'>✈️ 포르투갈 여행, 이것만은 꼭 알아두세요! (필수 팁)</h3>", unsafe_allow_html=True)
    st.markdown("""
    <div class="info-box">
        <p><b>👟 편한 신발은 필수!</b> 리스본과 포르투 같은 주요 도시는 언덕과 오래된 돌길이 많아 발이 편한 신발은 선택이 아닌 필수입니다. 굽 높은 신발은 잠시 접어두세요!</p>
        <p><b>🔌 유럽형 2핀 어댑터 준비:</b> 전압은 230V, 50Hz이며, 유럽식 2핀 플러그(Type F)를 사용합니다. 한국에서 미리 준비해 가는 것이 편리해요.</p>
        <p><b>☀️ 햇볕 조심:</b> 포르투갈은 햇볕이 강한 날이 많습니다. 선크림, 모자, 선글라스를 꼭 챙겨 피부와 눈을 보호해주세요.</p>
        <p><b>🧥 가벼운 겉옷:</b> 한여름에도 저녁에는 쌀쌀해질 수 있으니, 가벼운 가디건이나 재킷을 챙기면 유용합니다.</p>
        <p><b>💰 식전 빵 (Couvert) 문화:</b> 식당에서 처음에 빵, 올리브 등이 나오는 경우가 많습니다. 이는 무료가 아니며, 원치 않으면 정중히 "Não, obrigado/a (노, 오브리가두/오브리가다 - 아니요, 괜찮습니다)"라고 말하며 거절할 수 있습니다.</p>
        <p><b>💶 팁 문화:</b> 의무는 아니지만, 서비스가 만족스러웠다면 전체 금액의 5~10% 정도를 팁으로 남기는 것이 일반적임을 알려줍니다.</p>
        <p><b>🚨 소매치기 주의:</b> 포르투갈은 안전한 나라지만, 관광객이 많은 번화가나 트램 안에서는 소매치기를 조심해야 합니다. 가방은 항상 몸 앞쪽에 메고 귀중품은 잘 보관하세요.</p>
        <p><b>💧 수돗물 음용:</b> 포르투갈의 수돗물은 대체로 안전하고 마실 수 있지만, 개인차가 있으니 불안하다면 생수를 구매하는 것이 좋습니다.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<h3 class='section-header'>🚎 포르투갈 대중교통 이용 가이드</h3>", unsafe_allow_html=True)
    st.markdown("""
    <div class="info-box">
        <p><b><span style="color:#0047AB;">리스본 (Lisbon)</span>:</b><br>
        <b>🔹 비바 비아젬 (Viva Viagem) 카드:</b> 리스본 대중교통의 필수품입니다. 지하철역에서 구매(카드 보증금 0.5유로)하고 원하는 금액만큼 충전(Zapping 모드)하여 사용합니다. 지하철, 버스, 트램, 푸니쿨라, 엘리베이터 등 대부분의 대중교통에 사용할 수 있어 매우 편리해요.<br>
        <b>🔸 28번 트램:</b> 리스본의 상징이자 명물입니다. 주요 관광지를 지나가지만, 항상 사람이 많으니 소매치기에 주의하고, 여유롭게 즐기려면 아침 일찍 타는 것을 추천합니다.</p>
        <p><b><span style="color:#0047AB;">포르투 (Porto)</span>:</b><br>
        <b>🔹 안단테 (Andante) 카드:</b> 포르투 대중교통의 핵심 카드입니다. 지하철역에서 구매(카드 보증금 0.6유로)하고 이동할 존(Zone)에 따라 충전하여 사용합니다. 지하철, 버스 등 포르투의 주요 대중교통을 이용할 수 있어요.</p>
        <p><b><span style="color:#0047AB;">도시 간 이동 (기차/버스)</span>:</b><br>
        <b>🔹 기차:</b> 리스본-포르투, 리스본-코임브라 등 주요 도시 간 이동에 편리합니다. 포르투갈 철도청(CP - Comboios de Portugal) 웹사이트에서 미리 예약하면 더 저렴하게 구매할 수 있습니다.<br>
        <b>🔹 버스:</b> 기차가 닿지 않는 지역이나 더 저렴한 옵션을 찾을 때 유용합니다. Rede Expressos와 같은 버스 회사 웹사이트를 확인하세요.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<h3 class='section-header'>🗣️ 간단 포르투갈어 회화 (알아두면 좋아요!)</h3>", unsafe_allow_html=True)
    st.markdown("""
    <div class="info-box">
        <table style="width:100%; border-collapse: collapse;">
            <tr style="background-color:#ADD8E6;">
                <th style="padding: 8px; border: 1px solid #ddd; text-align: left;">포르투갈어</th>
                <th style="padding: 8px; border: 1px solid #ddd; text-align: left;">발음 (근사치)</th>
                <th style="padding: 8px; border: 1px solid #ddd; text-align: left;">의미</th>
            </tr>
            <tr>
                <td style="padding: 8px; border: 1px solid #ddd;">Olá</td>
                <td style="padding: 8px; border: 1px solid #ddd;">올라</td>
                <td style="padding: 8px; border: 1px solid #ddd;">안녕하세요</td>
            </tr>
            <tr>
                <td style="padding: 8px; border: 1px solid #ddd;">Obrigado / Obrigada</td>
                <td style="padding: 8px; border: 1px solid #ddd;">오브리가두 (남성) / 오브리가다 (여성)</td>
                <td style="padding: 8px; border: 1px solid #ddd;">감사합니다</td>
            </tr>
            <tr>
                <td style="padding: 8px; border: 1px solid #ddd;">Por favor</td>
                <td style="padding: 8px; border: 1px solid #ddd;">포르 파보르</td>
                <td style="padding: 8px; border: 1px solid #ddd;">부탁합니다 / 제발</td>
            </tr>
            <tr>
                <td style="padding: 8px; border: 1px solid #ddd;">Desculpe</td>
                <td style="padding: 8px; border: 1px solid #ddd;">데스쿨프</td>
                <td style="padding: 8px; border: 1px solid #ddd;">죄송합니다</td>
            </tr>
            <tr>
                <td style="padding: 8px; border: 1px solid #ddd;">Sim</td>
                <td style="padding: 8px; border: 1px solid #ddd;">싱</td>
                <td style="padding: 8px; border: 1px solid #ddd;">네</td>
            </tr>
            <tr>
                <td style="padding: 8px; border: 1px solid #ddd;">Não</td>
                <td style="padding: 8px; border: 1px solid #ddd;">나웅</td>
                <td style="padding: 8px; border: 1px solid #ddd;">아니오</td>
            </tr>
            <tr>
                <td style="padding: 8px; border: 1px solid #ddd;">Quanto custa?</td>
                <td style="padding: 8px; border: 1px solid #ddd;">콴투 쿠스타?</td>
                <td style="padding: 8px; border: 1px solid #ddd;">얼마예요?</td>
            </tr>
            <tr>
                <td style="padding: 8px; border: 1px solid #ddd;">Adeus</td>
                <td style="padding: 8px; border: 1px solid #ddd;">아데우스</td>
                <td style="padding: 8px; border: 1px solid #ddd;">안녕히 계세요 (헤어질 때)</td>
            </tr>
        </table>
        <p style="margin-top:10px;">현지에서 이 몇 마디만 건네도 포르투갈 사람들이 더 환영해 줄 거예요! 😊</p>
    </div>
    """, unsafe_allow_html=True)


elif page == "🗺️ 포르투갈 주요 관광지 지도":
    st.markdown("<h2 class='sub-header'>🗺️ 포르투갈 주요 관광지 지도</h2>", unsafe_allow_html=True)
    st.markdown("""
    <p>아래 지도에서 포르투갈의 주요 관광지들을 한눈에 확인하세요. 각 도시에 해당하는 마커를 클릭하거나, 아래 드롭다운 메뉴에서 도시를 선택하면 해당 도시의 상세 정보를 확인할 수 있습니다.</p>
    """, unsafe_allow_html=True)

    # Create a Folium map centered on Portugal
    m = folium.Map(location=[39.5, -8.0], zoom_start=7, control_scale=True)

    # Add markers for each attraction
    for name, data in attraction_data.items():
        folium.Marker(
            location=data["coords"],
            popup=f"<b>{name}</b><br>{data['description'].split('.')[0]}...",
            tooltip=name,
            icon=folium.Icon(color="blue", icon="info-sign")
        ).add_to(m)

    # Display the map
    folium_static(m, width=1000, height=600)

    st.markdown("---")
    st.markdown("<h3 class='section-header'>📍 도시 선택 후 상세 정보 확인</h3>", unsafe_allow_html=True)

    # Dropdown to select a city
    selected_city = st.selectbox("상세 정보를 보고 싶은 도시를 선택하세요:", list(attraction_data.keys()))

    if selected_city:
        city_info = attraction_data[selected_city]
        st.markdown(f"<h3 class='attraction-title'>{selected_city}</h3>", unsafe_allow_html=True)
        st.image(city_info["image"], caption=f"{selected_city} 전경", use_column_width=True)
        st.markdown(f"<p>{city_info['description']}</p>", unsafe_allow_html=True)

        st.markdown("<h4 class='section-header'>주요 명소</h4>", unsafe_allow_html=True)
        for attr in city_info["attractions"]:
            st.markdown(f"<h5 class='attraction-title'>{attr['name']}</h5>", unsafe_allow_html=True)
            st.image(attr["image"], caption=attr["name"], use_column_width=True)
            st.markdown(f"<p>{attr['desc']}</p>", unsafe_allow_html=True)
            st.markdown(f"""
            <div class="info-box">
                <p><strong>✨ 왜 방문해야 할까요?</strong> {attr['why']}</p>
                <p><strong>💡 팁:</strong> {attr['tip']}</p>
            </div>
            """, unsafe_allow_html=True)


elif page == "✨ 포르투갈의 미식과 문화":
    st.markdown("<h2 class='sub-header'>✨ 포르투갈의 미식과 문화</h2>", unsafe_allow_html=True)
    st.markdown("""
    <p>포르투갈 여행은 단순히 관광지를 둘러보는 것을 넘어, 풍부한 미식과 독특한 문화를 경험하는 것입니다.</p>
    """, unsafe_allow_html=True)

    st.markdown("<h3 class='section-header'>😋 포르투갈 미식</h3>", unsafe_allow_html=True)
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Pasteis_de_nata.jpg/1200px-Pasteis_de_nata.jpg", caption="달콤한 파스텔 드 나타")
    st.markdown("""
    <ul>
        <li><b>바칼라우 (Bacalhau):</b> 대구는 포르투갈의 국민 음식입니다. '천 가지 조리법'이 있다고 할 정도로 다양한 방식으로 요리됩니다.</li>
        <li><b>파스텔 드 나타 (Pastel de Nata):</b> 달콤하고 바삭한 포르투갈식 에그 타르트. 따뜻할 때 시나몬 가루를 뿌려 먹으면 더욱 맛있습니다.</li>
        <li><b>해산물 요리:</b> 대서양을 접하고 있는 만큼 신선한 해산물이 풍부합니다. 문어, 정어리, 조개 등을 이용한 요리가 많습니다.</li>
        <li><b>포트 와인 (Port Wine):</b> 포르투를 대표하는 주정강화 와인으로, 식전주나 디저트 와인으로 즐겨 마십니다.</li>
        <li><b>그린 와인 (Vinho Verde):</b> 신선하고 가벼운 화이트 와인으로, 특히 여름에 즐기기 좋습니다.</li>
        <li><b>진자 (Ginja):</b> 체리로 만든 달콤한 리큐어로, 오비두스 지역의 특산품입니다. 초콜릿 컵에 담아 마시는 것이 전통입니다.</li>
    </ul>
    """, unsafe_allow_html=True)

    st.markdown("<h3 class='section-header'>🎶 포르투갈 문화</h3>", unsafe_allow_html=True)
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Fado_Performance_Lisbon_Portugal.jpg/1200px-Fado_Performance_Lisbon_Portugal.jpg", caption="리스본의 파두 공연")
    st.markdown("""
    <ul>
        <li><b>파두 (Fado):</b> 포르투갈의 전통 음악으로, 슬픔과 그리움, 운명을 노래합니다. 유네스코 무형문화유산으로 지정되어 있습니다. 리스본의 알파마 지구와 포르투의 작은 레스토랑에서 라이브 공연을 즐길 수 있습니다.</li>
        <li><b>아줄레주 (Azulejos):</b> 화려한 색상의 타일 예술로, 건물 외벽, 교회, 지하철역 등 포르투갈 곳곳에서 볼 수 있습니다. 각 타일에는 역사적 사건이나 이야기가 담겨 있습니다.</li>
        <li><b>대항해 시대의 유산:</b> 포르투갈은 15세기에 세계를 탐험하며 강력한 해양 국가였습니다. 이 시기의 건축물과 박물관에서 그 영광스러운 역사를 느낄 수 있습니다.</li>
        <li><b>친절한 사람들:</b> 포르투갈 사람들은 매우 친절하고 따뜻하여 여행객들에게 잊지 못할 환대를 제공합니다.</li>
    </ul>
    """, unsafe_allow_html=True)

    st.markdown("<h3 class='section-header'>✈️ 일반 여행 팁</h3>", unsafe_allow_html=True)
    st.markdown("""
    <div class="info-box">
        <p><b>💰 통화:</b> 유로 (EUR). 카드 사용이 보편적이지만, 작은 상점이나 카페에서는 현금을 준비하는 것이 좋습니다.</p>
        <p><b>🗣️ 언어:</b> 포르투갈어. 관광지에서는 영어가 잘 통하지만, 간단한 포르투갈어 표현을 익혀두면 현지인들과 더 가깝게 소통할 수 있습니다. (예: Olá - 안녕하세요, Obrigado/a - 감사합니다)</p>
        <p><b>⌚ 시차:</b> 한국보다 8시간 느립니다. (서머타임 적용 시 7시간 느림)</p>
        <p><b>🗓️ 최적의 방문 시기:</b> 봄(4~6월)과 가을(9~10월)은 날씨가 온화하고 관광객이 너무 많지 않아 여행하기 가장 좋습니다. 여름(7~8월)은 날씨가 덥고 관광객이 많지만, 해변 휴양을 즐기기에 좋습니다.</p>
    </div>
    """, unsafe_allow_html=True)

elif page == "🗓️ 나만의 추천 일정 만들기": # New page for custom itineraries
    st.markdown("<h2 class='sub-header'>🗓️ 나만의 추천 일정 만들기</h2>", unsafe_allow_html=True)
    st.markdown("""
    <p>여러분의 취향에 맞는 포르투갈 여행 일정을 추천해 드릴게요. 몇 가지 질문에 답해주세요!</p>
    """, unsafe_allow_html=True)

    # User inputs for itinerary recommendation
    cities_available = list(attraction_data.keys())
    selected_city_for_itinerary = st.selectbox("가고 싶은 도시를 선택하세요:", cities_available)

    companion_type = st.radio("누구와 함께 여행하시나요?", ["혼자", "연인", "친구", "가족"])

    duration_type = st.radio("여행 기간은 어느 정도이신가요?", ["3-4일", "5-7일"])

    if st.button("추천 일정 보기"):
        recommended_plan = recommend_itinerary(selected_city_for_itinerary, companion_type, duration_type)
        st.markdown("<h3 class='section-header'>✨ 추천 드리는 나만의 여행 일정</h3>", unsafe_allow_html=True)
        st.markdown(f"<div class='info-box'>{recommended_plan}</div>", unsafe_allow_html=True)
        st.info("💡 **팁:** 위 추천 일정은 예시이며, 여러분의 관심사와 컨디션에 따라 자유롭게 조절하여 더욱 완벽한 여행을 만드세요!")

st.write("---")
st.markdown("<p style='font-size:1.5em; text-align:center; color:#0047AB;'><b>Boa Viagem! (즐거운 여행 되세요!)</b></p>", unsafe_allow_html=True)
st.balloons()
