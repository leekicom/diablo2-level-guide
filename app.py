import streamlit as st

st.set_page_config(page_title="디아2 레벨 가이드", page_icon="⚔️")
st.title("⚔️ 디아블로 2 레벨별 사냥터 가이드")

# 1. 세션 상태 초기화
if 'level' not in st.session_state:
    st.session_state.level = 1

# 2. 버튼 클릭 시 실행될 함수 (콜백 함수)
def add_level():
    if st.session_state.level <= 89:
        st.session_state.level += 10
    else:
        st.session_state.level = 99

# 3. UI 배치
col1, col2 = st.columns([3, 1])

with col1:
    # 위젯의 key를 session_state와 연결
    st.number_input("현재 캐릭터 레벨", min_value=1, max_value=99, key="level")

with col2:
    st.write("") # 간격 맞추기
    # 버튼을 누르면 add_level 함수가 실행된 후 화면이 다시 그려집니다.
    st.button("+10 레벨", on_click=add_level)

# 4. 데이터 및 결과 출력 (기존과 동일)
recommendations = [
    ("노말", "액트 1", 1, 11), ("노말", "액트 2", 12, 18), ("노말", "액트 3", 19, 23),
    ("노말", "액트 4", 24, 31), ("노말", "액트 5", 32, 36),
    ("악몽", "액트 1", 37, 43), ("악몽", "액트 2", 44, 48), ("악몽", "액트 3", 49, 52),
    ("악몽", "액트 4", 53, 62), ("악몽", "액트 5", 63, 65),
    ("지옥", "액트 1", 66, 73), ("지옥", "액트 2", 74, 80), ("지옥", "액트 3", 81, 83),
    ("지옥", "액트 4", 84, 94), ("지옥", "액트 5", 95, 99)
]

st.divider()
char_level = st.session_state.level # 현재 세션의 레벨 값 가져오기

found = False
for diff, act, min_l, max_l in recommendations:
    if min_l <= char_level <= max_l:
        st.success(f"### ✅ 추천 사냥터: [{diff}] {act}")
        st.info(f"💡 권장 레벨 범위: {min_l} ~ {max_l}")
        found = True
        break

if not found:
    st.warning("만렙이시거나 범위를 벗어났습니다. 헬 바알런을 추천합니다!")