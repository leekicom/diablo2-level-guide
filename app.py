import streamlit as st
import math
import pandas as pd
from datetime import datetime

# 1. 페이지 설정
st.set_page_config(page_title="멀티 가이드 앱", page_icon="📱", layout="wide")

# 2. 사이드바 메뉴 만들기
st.sidebar.title("🌟 메뉴 선택")
menu = st.sidebar.radio("가고 싶은 페이지를 선택하세요", ["디아2 레벨 가이드", "삼성 라이온즈 일정","원둘레 계산"])

# --- 페이지 1: 디아블로 2 가이드 ---
if menu == "디아2 레벨 가이드":
    st.title("⚔️ 디아블로 2 레벨별 사냥터 가이드")
    
    if 'level' not in st.session_state:
        st.session_state.level = 1

    def add_level():
        if st.session_state.level <= 89:
            st.session_state.level += 10
        else:
            st.session_state.level = 99

    col1, col2 = st.columns([3, 1])
    with col1:
        st.number_input("현재 캐릭터 레벨", min_value=1, max_value=99, key="level")
    with col2:
        st.write("") 
        st.button("+10 레벨", on_click=add_level)

    recommendations = [
        ("노말", "액트 1", 1, 11), ("노말", "액트 2", 12, 18), ("노말", "액트 3", 19, 23),
        ("노말", "액트 4", 24, 31), ("노말", "액트 5", 32, 36),
        ("악몽", "액트 1", 37, 43), ("악몽", "액트 2", 44, 48), ("악몽", "액트 3", 49, 52),
        ("악몽", "액트 4", 53, 62), ("악몽", "액트 5", 63, 65),
        ("지옥", "액트 1", 66, 73), ("지옥", "액트 2", 74, 80), ("지옥", "액트 3", 81, 83),
        ("지옥", "액트 4", 84, 94), ("지옥", "액트 5", 95, 99)
    ]

    st.divider()
    char_level = st.session_state.level
    for diff, act, min_l, max_l in recommendations:
        if min_l <= char_level <= max_l:
            st.success(f"### ✅ 추천 사냥터: [{diff}] {act}")
            break

# --- 페이지 2: 삼성 라이온즈 일정 (2026 시범경기 가상 데이터) ---
elif menu == "삼성 라이온즈 일정":
    st.set_page_config(page_title="2026 삼성라이온즈 일정", page_icon="🦁", layout="wide")

    # 일정 데이터 (표 형식)
# 2. 데이터 준비 (2026년 전체 일정 예시 데이터)
# 실제 일정이 나오면 이 리스트만 업데이트하면 됩니다.
    raw_data = [
        {"날짜": "2026-03-24", "상대": "SSG", "장소": "문학", "시간": "18:30", "비고": "개막전"},
        {"날짜": "2026-03-25", "상대": "SSG", "장소": "문학", "시간": "18:30", "비고": "-"},
        {"날짜": "2026-03-27", "상대": "두산", "장소": "대구", "시간": "18:30", "비고": "홈개막"},
        {"날짜": "2026-03-28", "상대": "두산", "장소": "대구", "시간": "17:00", "비고": "-"},
        {"날짜": "2026-04-01", "상대": "LG", "장소": "잠실", "시간": "18:30", "비고": "-"},
        {"날짜": "2026-04-07", "상대": "롯데", "장소": "대구", "시간": "18:30", "비고": "클래식시리즈"},
        {"날짜": "2026-05-05", "상대": "NC", "장소": "대구", "시간": "14:00", "비고": "어린이날"},
    # ... 더 많은 데이터를 추가할 수 있습니다.
    ]

    df = pd.DataFrame(raw_data)
    df['날짜'] = pd.to_datetime(df['날짜'])
    df['월'] = df['날짜'].dt.month
    df['요일'] = df['날짜'].dt.day_name()

# 3. 사이드바 - 월 선택 및 필터
    st.sidebar.header("🦁 일정 필터")
    selected_month = st.sidebar.selectbox("월 선택", [3, 4, 5, 6, 7, 8, 9, 10], index=0)
    home_only = st.sidebar.checkbox("홈 경기(대구)만 보기")

# 필터링 적용
    filtered_df = df[df['월'] == selected_month]
    if home_only:
        filtered_df = filtered_df[filtered_df['장소'] == "대구"]

# 4. 메인 화면 구성
    st.title(f"🦁 2026 삼성 라이온즈 {selected_month}월 경기 일정")

    if filtered_df.empty:
        st.warning(f"등록된 {selected_month}월 경기가 없습니다.")
    else:
    # 달력 그리드 레이아웃 (한 줄에 7일이 아닌 경기일 순으로 카드 배치)
        cols = st.columns(4) # 한 줄에 4경기씩 표시
    
    for idx, row in enumerate(filtered_df.itertuples()):
        with cols[idx % 4]:
            # 홈/원정 디자인 차별화
            is_home = row.장소 == "대구"
            card_color = "#0056b3" if is_home else "#ffffff" # 삼성 블루 vs 화이트
            text_color = "white" if is_home else "black"
            border = "none" if is_home else "1px solid #ddd"
            
            st.markdown(f"""
                <div style="background-color: {card_color}; color: {text_color}; padding: 20px; 
                            border-radius: 15px; border: {border}; margin-bottom: 20px;
                            box-shadow: 2px 2px 10px rgba(0,0,0,0.1); height: 180px;">
                    <div style="font-size: 1.2em; font-weight: bold;">{row.날짜.strftime('%m.%d')} ({row.요일[:3]})</div>
                    <hr style="margin: 10px 0; border-color: {text_color}; opacity: 0.3;">
                    <div style="font-size: 1.5em; font-weight: 800; text-align: center;">vs {row.상대}</div>
                    <div style="text-align: center; margin-top: 10px;">📍 {row.장소} | ⏰ {row.시간}</div>
                    <div style="text-align: right; font-size: 0.8em; margin-top: 5px; opacity: 0.8;">{row.비고}</div>
                </div>
            """, unsafe_allow_html=True)

# 5. 하단 전체 통계
    st.divider()
    st.subheader("📊 시즌 요약")
    col_stat1, col_stat2, col_stat3 = st.columns(3)
    col_stat1.metric("이번 달 경기 수", f"{len(filtered_df)}경기")
    col_stat2.metric("홈 경기", f"{len(filtered_df[filtered_df['장소'] == '대구'])}경기")
    col_stat3.metric("원정 경기", f"{len(filtered_df[filtered_df['장소'] != '대구'])}경기")






elif menu == "원둘레 계산":

    # 1. 페이지 설정
    st.set_page_config(page_title="도형 계산기 Pro", page_icon="📏", layout="centered")

    # 2. 타이틀 및 디자인
    st.title("📏 원형 도형 계산기")
    st.markdown("반지름을 입력하면 실시간으로 **둘레**와 **넓이**를 계산합니다.")
    st.divider()

    # 3. 입력창 (슬라이더와 입력창 병합)
    col_input, col_info = st.columns([2, 1])

    with col_input:
        r = st.number_input("반지름(r)을 입력하세요", min_value=0.0, value=10.0, step=0.5)
        st.info(f"선택된 반지름: **{r}**")

    # 4. 계산 로직
    pi = math.pi
    circumference = 2 * pi * r
    area = pi * (r ** 2)

    # 5. 결과 보여주기 (세련된 지표 카드 활용)
    st.subheader("📊 계산 결과")
    res_col1, res_col2 = st.columns(2)

    with res_col1:
        st.metric(label="원의 둘레 ($2\pi r$)", value=f"{circumference:.2f}")

    with res_col2:
        st.metric(label="원의 넓이 ($\pi r^2$)", value=f"{area:.2f}")

    # 6. 그래픽 요소 (간단한 시각화)
    st.divider()
    st.write("### 📍 시각적 가이드")

    # SVG를 이용해 입력값에 따라 커지는 원 그리기
    circle_size = min(r * 5, 200) # 화면 크기에 맞춰 조절
    st.write(f"""
    <div style="display: flex; justify-content: center; align-items: center; background-color: #f0f2f6; padding: 20px; border-radius: 10px;">
    <svg width="220" height="220">
        <circle cx="110" cy="110" r="{circle_size/2}" fill="#ff4b4b" opacity="0.6" stroke="#ff4b4b" stroke-width="2" />
        <line x1="110" y1="110" x2="{110 + circle_size/2}" y2="110" stroke="white" stroke-width="2" />
        <text x="115" y="105" fill="#31333F" font-weight="bold">r = {r}</text>
    </svg>
    </div>
    """, unsafe_allow_html=True)

    st.caption("입력하신 반지름의 크기에 비례하여 원의 크기가 변화합니다.")