import streamlit as st

# 1. 페이지 설정
st.set_page_config(page_title="멀티 가이드 앱", page_icon="📱", layout="wide")

# 2. 사이드바 메뉴 만들기
st.sidebar.title("🌟 메뉴 선택")
menu = st.sidebar.radio("가고 싶은 페이지를 선택하세요", ["디아2 레벨 가이드", "삼성 라이온즈 일정"])

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
    st.title("⚾ 2026 삼성 라이온즈 시범경기 일정")
    st.info("사자들의 승리를 기원합니다! (예시 일정입니다)")

    # 일정 데이터 (표 형식)
    schedule_data = [
        {"날짜": "2026-03-14", "상대": "LG 트윈스", "구장": "대구 삼성 라이온즈 파크", "시간": "13:00"},
        {"날짜": "2026-03-15", "상대": "LG 트윈스", "구장": "대구 삼성 라이온즈 파크", "시간": "13:00"},
        {"날짜": "2026-03-17", "상대": "KIA 타이거즈", "구장": "광주 챔피언스 필드", "시간": "13:00"},
        {"날짜": "2026-03-18", "상대": "KIA 타이거즈", "구장": "광주 챔피언스 필드", "시간": "13:00"},
        {"날짜": "2026-03-21", "상대": "두산 베어스", "구장": "대구 삼성 라이온즈 파크", "시간": "13:00"},
    ]

    # 데이터 프레임 형식으로 예쁘게 보여주기
    st.table(schedule_data)
    
    st.markdown("---")
    st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ") # 응원가 영상 등을 넣을 수 있어요!