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
    "🎉 포르투갈 여행 시작",
    "✨ 첫 포르투갈 여행자를 위한 특별 가이드", # New section
    "🗺️ 포르투갈 주요 관광지 지도",
    "🏛️ 리스본 (Lisbon)",
    "🍷 포르투 & 북부 (Porto & North)",
    "🏖️ 알가르베 (Algarve)",
    "🏰 중부 포르투갈 (Central Portugal)",
    "✨ 포르투갈의 미식과 문화",
    "✈️ 여행 팁",
    "💌 마치며"
])

# --- Content Sections ---

if page == "🎉 포르투갈 여행 시작":
    st.markdown("<h2 class='sub-header'>🎉 포르투갈 여행 시작</h2>", unsafe_allow_html=True)
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Panorama_of_Lisbon_from_Miradouro_de_São_Pedro_de_Alcântara.jpg/1200px-Panorama_of_Lisbon_from_Miradouro_de_São_Pedro_de_Alcântara.jpg", caption="리스본 전경")
    st.markdown("""
    <p>포르투갈은 서유럽의 숨겨진 보석으로, 그 매력은 끝이 없습니다.
    활기찬 도시, 중세 시대의 성, 황금빛 해변, 그리고 맛있는 해산물 요리가 여러분을 기다리고 있습니다.
    작지만 다채로운 이 나라는 모든 종류의 여행객에게 잊을 수 없는 경험을 선사할 것입니다.
    역사 애호가, 자연 탐험가, 미식가, 혹은 단순히 휴식을 원하는 분이든, 포르투갈은 여러분의 기대를 뛰어넘을 것입니다.
    </p>
    """, unsafe_allow_html=True)
    st.info("💡 **팁:** 포르투갈은 연중 온화한 기후를 자랑하지만, 방문 시기에 따라 다른 매력을 느낄 수 있습니다. 봄과 가을은 날씨가 쾌적하고 관광객이 비교적 적어 여행하기 가장 좋습니다.")

elif page == "✨ 첫 포르투갈 여행자를 위한 특별 가이드":
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
        <p><b>💶 팁 문화:</b> 의무는 아니지만, 서비스가 만족스러웠다면 전체 금액의 5~10% 정도를 팁으로 남기는 것이 일반적입니다.</p>
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

    st.markdown("<h3 class='section-header'>🗺️ 추천 여행 코스 (예시)</h3>", unsafe_allow_html=True)
    st.markdown("""
    <div class="info-box">
        <h4>✔️ 리스본 집중 3박 4일 코스</h4>
        <ul>
            <li><b>1일차:</b> 리스본 도착, 알파마 지구 탐험, 상 조르제 성에서 일몰 감상, 파두 공연 관람.</li>
            <li><b>2일차:</b> 벨렘 지구 (제로니무스 수도원, 벨렘 탑, 발견 기념비) 투어 후 에그 타르트 맛보기. 바이샤-시아두 지구에서 쇼핑 및 식사.</li>
            <li><b>3일차:</b> 신트라 당일치기 (페나 궁전, 무어 성, 킨타 다 헤갈레이라).</li>
            <li><b>4일차:</b> 리스본 자유 시간 (박물관, 쇼핑 등) 및 출국.</li>
        </ul>
        <h4>✔️ 포르투 & 도루 밸리 3박 4일 코스</h4>
        <ul>
            <li><b>1일차:</b> 포르투 도착, 리베이라 지구 탐험, 동 루이스 1세 다리 건너기, 포트 와인 셀러 투어 및 시음.</li>
            <li><b>2일차:</b> 렐루 서점 방문, 클레리구스 탑 오르기, 볼량 시장 구경.</li>
            <li><b>3일차:</b> 도루 밸리 와이너리 투어 및 강 크루즈 (포르투에서 당일치기 또는 1박).</li>
            <li><b>4일차:</b> 포르투 자유 시간 및 출국.</li>
        </ul>
        <p>💡 <b>팁:</b> 이 코스들은 예시이며, 여러분의 관심사와 일정에 맞춰 자유롭게 조정할 수 있습니다!</p>
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
    <p>아래 지도에서 포르투갈의 주요 관광지들을 한눈에 확인하세요. 각 마커를 클릭하면 간단한 정보를 볼 수 있으며,
    더 자세한 내용은 왼쪽 사이드바에서 해당 도시를 선택하여 확인하실 수 있습니다.</p>
    """, unsafe_allow_html=True)

    # Coordinates for major attractions
    attractions = {
        "리스본": {"lat": 38.7223, "lon": -9.1393, "desc": "포르투갈의 수도, 7개 언덕 위의 매력적인 도시", "region": "리스본"},
        "포르투": {"lat": 41.1579, "lon": -8.6291, "desc": "도루 강변의 와인 도시", "region": "포르투 & 북부"},
        "신트라": {"lat": 38.7997, "lon": -9.3905, "desc": "동화 같은 궁전과 성의 마을", "region": "리스본 근교"},
        "알가르베": {"lat": 37.0194, "lon": -7.9304, "desc": "황금빛 해변과 절벽이 아름다운 남부 휴양지", "region": "알가르베"},
        "코임브라": {"lat": 40.2056, "lon": -8.4196, "desc": "유서 깊은 대학 도시", "region": "중부 포르투갈"},
        "에보라": {"lat": 38.5667, "lon": -7.9083, "desc": "로마 유적과 중세 건축물이 가득한 유네스코 도시", "region": "중부 포르투갈"},
        "파루": {"lat": 37.0194, "lon": -7.9304, "desc": "알가르베의 주도, 아름다운 자연 공원", "region": "알가르베"},
        "두루 밸리": {"lat": 41.1718, "lon": -7.5701, "desc": "세계적인 포트 와인 생산지, 그림 같은 포도밭 풍경", "region": "포르투 & 북부"},
        "오비두스": {"lat": 39.3624, "lon": -9.1578, "desc": "성벽으로 둘러싸인 중세 마을", "region": "중부 포르투갈"},
        "아베이루": {"lat": 40.6405, "lon": -8.6538, "desc": "포르투갈의 베니스, 몰리세이루 보트", "region": "중부 포르투갈"},
    }

    # Create a Folium map centered on Portugal
    m = folium.Map(location=[39.5, -8.0], zoom_start=7, control_scale=True)

    # Add markers for each attraction
    for name, data in attractions.items():
        folium.Marker(
            location=[data["lat"], data["lon"]],
            popup=f"<b>{name}</b><br>{data['desc']}<br>지역: {data['region']}",
            tooltip=name,
            icon=folium.Icon(color="blue", icon="info-sign")
        ).add_to(m)

    # Display the map
    folium_static(m, width=1000, height=600)
    st.markdown("""
    <div class="info-box">
        <p>🗺️ <strong>지도 사용법:</strong> 마커를 클릭하여 정보를 확인하고, 지도를 확대/축소하여 주변 지역을 탐색하세요.</p>
    </div>
    """, unsafe_allow_html=True)


elif page == "🏛️ 리스본 (Lisbon)":
    st.markdown("<h2 class='sub-header'>🏛️ 리스본 (Lisbon)</h2>", unsafe_allow_html=True)
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Lisbon_as_seen_from_Miradouro_de_Santa_Catarina.jpg/1200px-Lisbon_as_seen_from_Miradouro_de_Santa_Catarina.jpg", caption="테주 강 너머 리스본의 노을")
    st.markdown("""
    <p>포르투갈의 활기찬 수도 리스본은 일곱 언덕 위에 자리 잡고 있으며, 다채로운 역사와 현대적인 매력이 조화를 이룹니다.
    노란색 트램이 좁은 골목을 오가고, 파두 음악이 밤하늘을 채우는 이 도시는 여러분을 매료시킬 것입니다.</p>
    """, unsafe_allow_html=True)

    st.markdown("<h3 class='section-header'>주요 명소</h3>", unsafe_allow_html=True)

    st.markdown("<h4 class='attraction-title'>벨렘 탑 (Belém Tower)</h4>", unsafe_allow_html=True)
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Torre_de_Bel%C3%A9m_%282012%29.jpg/800px-Torre_de_Bel%C3%A9m_%282012%29.jpg", caption="테주 강변의 벨렘 탑")
    st.markdown("""
    <p>테주 강가에 서 있는 벨렘 탑은 16세기 초에 지어진 아름다운 요새이자 등대입니다.
    포르투갈 대항해 시대의 상징이며, 유네스코 세계문화유산으로 등재되어 있습니다.
    이곳에서 바다를 향한 포르투갈의 위대한 꿈을 엿볼 수 있습니다.</p>
    <div class="info-box">
        <p><strong>✨ 왜 방문해야 할까요?</strong> 역사적인 중요성, 독특한 건축 양식, 아름다운 강변 풍경.</p>
        <p><strong>💡 팁:</strong> 내부를 방문하려면 미리 온라인으로 티켓을 예약하는 것이 좋습니다. 옆에 위치한 발견 기념비와 함께 방문하세요.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<h4 class='attraction-title'>제로니무스 수도원 (Jerónimos Monastery)</h4>", unsafe_allow_html=True)
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/e/ef/Mosteiro_dos_Jer%C3%B3nimos_Exterior.jpg/1200px-Mosteiro_dos_Jer%C3%B3nimos_Exterior.jpg", caption="웅장한 제로니무스 수도원")
    st.markdown("""
    <p>벨렘 탑과 함께 유네스코 세계문화유산인 제로니무스 수도원은 마누엘 양식의 걸작입니다.
    바스코 다 가마의 무덤이 안치되어 있으며, 웅장한 규모와 섬세한 조각이 감탄을 자아냅니다.</p>
    <div class="info-box">
        <p><strong>✨ 왜 방문해야 할까요?</strong> 포르투갈 건축의 정수, 역사적 인물들의 안식처.</p>
        <p><strong>💡 팁:</strong> 수도원 옆에 위치한 유명한 벨렘 에그 타르트(Pastéis de Belém)를 꼭 맛보세요!</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<h4 class='attraction-title'>상 조르제 성 (São Jorge Castle)</h4>", unsafe_allow_html=True)
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Castelo_de_S%C3%A3o_Jorge_Overview.jpg/1200px-Castelo_de_S%C3%A3o_Jorge_Overview.jpg", caption="리스본을 내려다보는 상 조르제 성")
    st.markdown("""
    <p>리스본에서 가장 높은 언덕에 위치한 상 조르제 성은 도시 전체를 조망할 수 있는 최고의 장소입니다.
    고대 로마 시대부터 요새가 있었던 곳으로, 리스본의 역사를 온전히 담고 있습니다.</p>
    <div class="info-box">
        <p><strong>✨ 왜 방문해야 할까요?</strong> 리스본 최고의 전망, 역사적인 분위기, 공작새와 함께하는 산책.</p>
        <p><strong>💡 팁:</strong> 일몰 시간에 방문하면 더욱 아름다운 풍경을 감상할 수 있습니다. 성벽을 따라 걸으며 사진을 찍어보세요.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<h4 class='attraction-title'>알파마 지구 (Alfama District)</h4>", unsafe_allow_html=True)
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/b/b3/Alfama_Lisbon_view.jpg/1200px-Alfama_Lisbon_view.jpg", caption="리스본 알파마 지구의 좁은 골목길")
    st.markdown("""
    <p>리스본에서 가장 오래된 지구인 알파마는 미로 같은 좁은 골목, 계단, 그리고 숨겨진 광장들로 가득합니다.
    파두 음악의 본고장으로, 밤에는 작은 레스토랑에서 슬프고도 아름다운 파두 공연을 즐길 수 있습니다.</p>
    <div class="info-box">
        <p><strong>✨ 왜 방문해야 할까요?</strong> 리스본의 진정한 매력을 느낄 수 있는 곳, 파두 음악 체험, 그림 같은 풍경.</p>
        <p><strong>💡 팁:</strong> 28번 트램을 타고 알파마 지구를 둘러보는 것은 리스본의 상징적인 경험입니다.</p>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("<h4 class='attraction-title'>신트라 (Sintra)</h4>", unsafe_allow_html=True)
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/0/02/Pena_Palace_Facade_%28cropped%29.jpg/1200px-Pena_Palace_Facade_%28cropped%29.jpg", caption="동화 같은 페나 궁전")
    st.markdown("""
    <p>리스본에서 기차로 약 40분 거리에 위치한 신트라는 동화 속에 나올 법한 궁전과 성으로 가득한 유네스코 세계문화유산 마을입니다.
    페나 궁전, 무어 성, 킨타 다 헤갈레이라 등이 주요 명소입니다.</p>
    <div class="info-box">
        <p><strong>✨ 왜 방문해야 할까요?</strong> 아름다운 건축물, 신비로운 분위기, 리스본 근교 당일치기 여행으로 최고.</p>
        <p><strong>💡 팁:</strong> 신트라는 언덕이 많고 교통이 복잡할 수 있으니, 미리 동선을 계획하고 대중교통이나 투어 버스를 이용하는 것이 좋습니다. 특히 페나 궁전은 인기가 많으니 일찍 방문하세요.</p>
    </div>
    """, unsafe_allow_html=True)


elif page == "🍷 포르투 & 북부 (Porto & North)":
    st.markdown("<h2 class='sub-header'>🍷 포르투 & 북부 (Porto & North)</h2>", unsafe_allow_html=True)
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/f/f9/Porto_Portugal_-_Ribeira_and_Douro_River.jpg/1200px-Porto_Portugal_-_Ribeira_and_Douro_River.jpg", caption="도루 강변의 포르투 리베이라 지구")
    st.markdown("""
    <p>포르투갈 북부의 심장부인 포르투는 도루 강을 따라 펼쳐진 아름다운 도시입니다.
    유서 깊은 와인 셀러, 매력적인 구시가지, 그리고 미식의 즐거움이 가득합니다.</p>
    """, unsafe_allow_html=True)

    st.markdown("<h3 class='section-header'>주요 명소</h3>", unsafe_allow_html=True)

    st.markdown("<h4 class='attraction-title'>포르투 리베이라 지구 (Ribeira District)</h4>", unsafe_allow_html=True)
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/c/c1/Porto_Ribeira_at_sunset.jpg/1200px-Porto_Ribeira_at_sunset.jpg", caption="노을 진 리베이라 지구")
    st.markdown("""
    <p>유네스코 세계문화유산인 리베이라 지구는 다채로운 색깔의 건물, 좁은 골목, 그리고 강변 레스토랑이 어우러져 활기찬 분위기를 자아냅니다.
    도루 강변을 따라 산책하거나 보트 투어를 즐기기에 좋습니다.</p>
    <div class="info-box">
        <p><strong>✨ 왜 방문해야 할까요?</strong> 포르투의 상징적인 풍경, 활기찬 분위기, 강변에서의 휴식.</p>
        <p><strong>💡 팁:</strong> 밤에는 다리 건너편 빌라 노바 드 가이아(Vila Nova de Gaia)에서 리베이라 지구의 야경을 감상하세요.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<h4 class='attraction-title'>동 루이스 1세 다리 (Dom Luís I Bridge)</h4>", unsafe_allow_html=True)
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/b/b8/Porto_-_Ponte_Lu%C3%ADs_I_%287313019130%29.jpg/1200px-Porto_-_Ponte_Lu%C3%ADs_I_%287313019130%29.jpg", caption="웅장한 동 루이스 1세 다리")
    st.markdown("""
    <p>에펠탑을 설계한 에펠의 제자가 설계한 이 거대한 철골 다리는 포르투와 빌라 노바 드 가이아를 연결합니다.
    다리 위를 걷거나 트램을 타고 강 양쪽의 멋진 전경을 감상할 수 있습니다.</p>
    <div class="info-box">
        <p><strong>✨ 왜 방문해야 할까요?</strong> 인상적인 건축물, 도루 강과 도시의 파노라마 전망.</p>
        <p><strong>💡 팁:</strong> 다리의 상층부는 지하철과 보행자 전용이고, 하층부는 차량과 보행자 모두 이용 가능합니다. 특히 상층부에서 보는 야경이 일품입니다.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<h4 class='attraction-title'>렐루 서점 (Livraria Lello)</h4>", unsafe_allow_html=True)
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Livraria_Lello_at_night.jpg/800px-Livraria_Lello_at_night.jpg", caption="아름다운 렐루 서점 내부")
    st.markdown("""
    <p>세계에서 가장 아름다운 서점 중 하나로 꼽히는 렐루 서점은 해리 포터 시리즈의 영감을 준 곳으로도 유명합니다.
    환상적인 계단과 스테인드글라스 천장이 인상적입니다.</p>
    <div class="info-box">
        <p><strong>✨ 왜 방문해야 할까요?</strong> 동화 같은 건축물, 해리 포터 팬들에게는 성지 같은 곳.</p>
        <p><strong>💡 팁:</strong> 입장하려면 티켓을 구매해야 하며, 긴 줄을 피하려면 아침 일찍 방문하거나 온라인으로 미리 예약하는 것이 좋습니다.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<h4 class='attraction-title'>도루 밸리 (Douro Valley)</h4>", unsafe_allow_html=True)
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/e/ef/Douro_Valley_view.jpg/1200px-Douro_Valley_view.jpg", caption="아름다운 도루 밸리의 포도밭")
    st.markdown("""
    <p>포르투에서 동쪽으로 약 100km 떨어진 도루 밸리는 포트 와인의 본고장으로 유네스코 세계문화유산에 등재되어 있습니다.
    계단식 포도밭이 강을 따라 그림처럼 펼쳐져 있으며, 와이너리 투어와 강 크루즈를 즐길 수 있습니다.</p>
    <div class="info-box">
        <p><strong>✨ 왜 방문해야 할까요?</strong> 세계적인 와인 산지, stunning한 자연경관, 와인 시음 체험.</p>
        <p><strong>💡 팁:</strong> 포르투에서 당일치기 투어나 1박 2일 일정으로 방문하는 것을 추천합니다. 와인 투어와 함께 강 크루즈를 즐겨보세요.</p>
    </div>
    """, unsafe_allow_html=True)

elif page == "🏖️ 알가르베 (Algarve)":
    st.markdown("<h2 class='sub-header'>🏖️ 알가르베 (Algarve)</h2>", unsafe_allow_html=True)
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/b/b3/Praia_da_Marinha_Algarve_Portugal.jpg/1200px-Praia_da_Marinha_Algarve_Portugal.jpg", caption="아름다운 마리냐 해변")
    st.markdown("""
    <p>포르투갈 남부의 알가르베는 황금빛 해변, 드라마틱한 절벽, 에메랄드빛 바다가 어우러진 최고의 휴양지입니다.
    일광욕, 수상 스포츠, 골프 등을 즐기기에 이상적인 곳입니다.</p>
    """, unsafe_allow_html=True)

    st.markdown("<h3 class='section-header'>주요 명소</h3>", unsafe_allow_html=True)

    st.markdown("<h4 class='attraction-title'>라고스 (Lagos)</h4>", unsafe_allow_html=True)
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Lagos_coastline_Portugal.jpg/1200px-Lagos_coastline_Portugal.jpg", caption="라고스 해안선")
    st.markdown("""
    <p>알가르베 서부에 위치한 라고스는 아름다운 해변과 독특한 해안 절벽, 그리고 역사적인 구시가지가 조화를 이룹니다.
    폰타 다 피에다드(Ponta da Piedade)의 동굴과 기암괴석은 꼭 방문해야 할 명소입니다.</p>
    <div class="info-box">
        <p><strong>✨ 왜 방문해야 할까요?</strong> 숨 막히는 해안 절경, 보트 투어, 매력적인 마을 분위기.</p>
        <p><strong>💡 팁:</strong> 폰타 다 피에다드에서는 보트 투어를 통해 절벽 사이의 동굴을 탐험하거나, 카약이나 SUP를 대여하여 직접 즐길 수 있습니다.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<h4 class='attraction-title'>파루 (Faro)</h4>", unsafe_allow_html=True)
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/f/f6/Faro_Old_Town_and_Marina.jpg/1200px-Faro_Old_Town_and_Marina.jpg", caption="파루의 구시가지와 마리나")
    st.markdown("""
    <p>알가르베 지방의 주도인 파루는 국제 공항이 있어 많은 여행객들이 처음으로 도착하는 곳입니다.
    매력적인 구시가지, 아름다운 대성당, 그리고 리아 포르모사 자연 공원(Parque Natural da Ria Formosa)이 유명합니다.</p>
    <div class="info-box">
        <p><strong>✨ 왜 방문해야 할까요?</strong> 평화로운 분위기, 아름다운 자연 보호 구역, 접근성.</p>
        <p><strong>💡 팁:</strong> 리아 포르모사 자연 공원은 보트 투어를 통해 방문할 수 있으며, 다양한 조류와 독특한 생태계를 관찰할 수 있습니다.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<h4 class='attraction-title'>베나길 동굴 (Benagil Cave)</h4>", unsafe_allow_html=True)
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Benagil_Cave.jpg/1200px-Benagil_Cave.jpg", caption="환상적인 베나길 동굴")
    st.markdown("""
    <p>아름다운 해안선에 숨겨진 베나길 동굴은 동굴 천장에 구멍이 뚫려 있어 햇빛이 쏟아져 들어오는 신비로운 공간입니다.
    보트, 카약, 또는 SUP를 이용하여 접근할 수 있습니다.</p>
    <div class="info-box">
        <p><strong>✨ 왜 방문해야 할까요?</strong> 자연이 만들어낸 경이로운 풍경, 잊을 수 없는 경험.</p>
        <p><strong>💡 팁:</strong> 동굴 안으로 들어가려면 보트 투어를 이용하거나, 직접 카약이나 SUP를 타고 가는 방법이 있습니다. 파도가 높으면 접근이 어려울 수 있으니 날씨를 확인하세요.</p>
    </div>
    """, unsafe_allow_html=True)

elif page == "🏰 중부 포르투갈 (Central Portugal)":
    st.markdown("<h2 class='sub-header'>🏰 중부 포르투갈 (Central Portugal)</h2>", unsafe_allow_html=True)
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/1/14/Coimbra_University_Library.jpg/1200px-Coimbra_University_Library.jpg", caption="코임브라 대학교의 아름다운 도서관")
    st.markdown("""
    <p>포르투갈 중부는 오랜 역사와 전통을 간직한 도시들과 아름다운 자연 경관을 자랑합니다.
    고대 로마 유적부터 중세 성벽 마을까지 다양한 매력을 만날 수 있습니다.</p>
    """, unsafe_allow_html=True)

    st.markdown("<h3 class='section-header'>주요 명소</h3>", unsafe_allow_html=True)

    st.markdown("<h4 class='attraction-title'>코임브라 (Coimbra)</h4>", unsafe_allow_html=True)
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/7/7b/Coimbra_-_panoramica.jpg/1200px-Coimbra_-_panoramica.jpg", caption="코임브라 도시 전경")
    st.markdown("""
    <p>포르투갈에서 가장 오래된 대학이 있는 코임브라는 유서 깊은 대학 도시입니다.
    조아니나 도서관(Biblioteca Joanina)은 세계에서 가장 아름다운 도서관 중 하나로 꼽힙니다.
    전통적인 대학생들의 검은 망토를 입은 모습을 볼 수 있으며, 파두 음악의 또 다른 중심지이기도 합니다.</p>
    <div class="info-box">
        <p><strong>✨ 왜 방문해야 할까요?</strong> 유서 깊은 대학 분위기, 아름다운 도서관, 파두 공연 감상.</p>
        <p><strong>💡 팁:</strong> 대학 방문 시 학생들의 전통 복장을 찾아보고, 오후에는 코임브라 파두 공연을 관람하는 것을 추천합니다.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<h4 class='attraction-title'>에보라 (Évora)</h4>", unsafe_allow_html=True)
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/e/e6/Roman_Temple_of_Évora.jpg/1200px-Roman_Temple_of_Évora.jpg", caption="에보라의 로마 신전")
    st.markdown("""
    <p>유네스코 세계문화유산 도시인 에보라는 고대 로마 시대의 유적과 중세 시대의 건축물들이 잘 보존되어 있습니다.
    로마 신전, 해골 예배당(Capela dos Ossos), 대성당 등이 주요 명소입니다.</p>
    <div class="info-box">
        <p><strong>✨ 왜 방문해야 할까요?</strong> 살아있는 역사 박물관, 로마 유적과 중세 건축물.</p>
        <p><strong>💡 팁:</strong> 해골 예배당은 다소 섬뜩할 수 있지만 독특한 경험을 제공합니다. 에보라 주변의 와이너리 투어도 인기가 많습니다.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<h4 class='attraction-title'>오비두스 (Óbidos)</h4>", unsafe_allow_html=True)
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Obidos_Castle.jpg/1200px-Obidos_Castle.jpg", caption="성벽으로 둘러싸인 오비두스")
    st.markdown("""
    <p>성벽으로 둘러싸인 그림 같은 중세 마을 오비두스는 포르투갈의 가장 아름다운 마을 중 하나로 꼽힙니다.
    아기자기한 상점, 하얀 집들, 그리고 성벽 위를 걷는 경험이 특별합니다.</p>
    <div class="info-box">
        <p><strong>✨ 왜 방문해야 할까요?</strong> 동화 같은 중세 마을, 낭만적인 분위기, 진자(Ginja) 리큐어.</p>
        <p><strong>💡 팁:</strong> 오비두스 특산품인 체리 리큐어 '진자(Ginja)'를 초콜릿 컵에 담아 마셔보세요. 마을을 한 바퀴 도는 성벽 길을 걸어보는 것도 좋습니다.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<h4 class='attraction-title'>아베이루 (Aveiro)</h4>", unsafe_allow_html=True)
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/1/18/Aveiro_Canal.jpg/1200px-Aveiro_Canal.jpg", caption="아베이루의 몰리세이루 보트")
    st.markdown("""
    <p>'포르투갈의 베니스'라고 불리는 아베이루는 다채로운 색깔의 전통 보트 '몰리세이루(Moliceiro)'가 운하를 따라 오가는 모습이 인상적입니다.
    아름다운 해변과 독특한 건축물도 매력적입니다.</p>
    <div class="info-box">
        <p><strong>✨ 왜 방문해야 할까요?</strong> 아름다운 운하 풍경, 몰리세이루 보트 체험, 달콤한 오보스 몰레스(Ovos Moles).</p>
        <p><strong>💡 팁:</strong> 몰리세이루 보트 투어를 꼭 해보세요. 아베이루의 전통 과자인 '오보스 몰레스(Ovos Moles)'도 맛봐야 합니다.</p>
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

elif page == "✈️ 여행 팁":
    st.markdown("<h2 class='sub-header'>✈️ 여행 팁</h2>", unsafe_allow_html=True)
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/0/0e/Lisbon_Tram_28.jpg/1200px-Lisbon_Tram_28.jpg", caption="리스본의 상징 28번 트램")
    st.markdown("""
    <div class="info-box">
        <p><b>💰 통화:</b> 유로 (EUR). 카드 사용이 보편적이지만, 작은 상점이나 카페에서는 현금을 준비하는 것이 좋습니다.</p>
        <p><b>🗣️ 언어:</b> 포르투갈어. 관광지에서는 영어가 잘 통하지만, 간단한 포르투갈어 표현을 익혀두면 현지인들과 더 가깝게 소통할 수 있습니다. (예: Olá - 안녕하세요, Obrigado/a - 감사합니다)</p>
        <p><b>⌚ 시차:</b> 한국보다 8시간 느립니다. (서머타임 적용 시 7시간 느림)</p>
        <p><b>🗓️ 최적의 방문 시기:</b> 봄(4~6월)과 가을(9~10월)은 날씨가 온화하고 관광객이 너무 많지 않아 여행하기 가장 좋습니다. 여름(7~8월)은 날씨가 덥고 관광객이 많지만, 해변 휴양을 즐기기에 좋습니다.</p>
    </div>
    """, unsafe_allow_html=True)

elif page == "💌 마치며":
    st.markdown("<h2 class='sub-header'>💌 마치며</h2>", unsafe_allow_html=True)
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/1/10/Christ_the_King_Statue_in_Lisbon.jpg/1200px-Christ_the_King_Statue_in_Lisbon.jpg", caption="리스본의 그리스도 상")
    st.markdown("""
    <p>이 가이드가 여러분의 포르투갈 여행 계획에 도움이 되기를 바랍니다.
    포르투갈은 정말 매력적인 나라로, 방문하는 모든 이들에게 깊은 인상을 남길 것입니다.
    아름다운 풍경, 맛있는 음식, 그리고 따뜻한 사람들과 함께 잊지 못할 추억을 만드시길 바랍니다.</p>
    <br>
    <p style="font-size:1.5em; text-align:center; color:#0047AB;"><b>Boa Viagem! (즐거운 여행 되세요!)</b></p>
    """, unsafe_allow_html=True)
    st.balloons()
