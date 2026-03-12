import streamlit as st

# 페이지 설정
st.set_page_config(page_title="디아2 레벨 가이드", page_icon="⚔️")

st.title("⚔️ 디아블로 2 레벨별 사냥터 가이드")
st.write("캐릭터 레벨에 맞는 최적의 경험치 구간을 확인하세요.")

# 입력창
char_level = st.number_input("현재 캐릭터 레벨을 입력하세요", min_value=1, max_value=99, value=1)

# 데이터
recommendations = [
    ("노말", "액트 1", 1, 11), ("노말", "액트 2", 12, 18), ("노말", "액트 3", 19, 23),
    ("노말", "액트 4", 24, 31), ("노말", "액트 5", 32, 36),
    ("악몽", "액트 1", 37, 43), ("악몽", "액트 2", 44, 48), ("악몽", "액트 3", 49, 52),
    ("악몽", "액트 4", 53, 62), ("악몽", "액트 5", 63, 65),
    ("지옥", "액트 1", 66, 73), ("지옥", "액트 2", 74, 80), ("지옥", "액트 3", 81, 83),
    ("지옥", "액트 4", 84, 94), ("지옥", "액트 5", 95, 99)
]

if st.button("추천 사냥터 보기"):
    found = False
    for diff, act, min_l, max_l in recommendations:
        if min_l <= char_level <= max_l:
            st.success(f"### ✅ 추천: [{diff}] {act}")
            st.info(f"💡 권장 레벨 범위: {min_l} ~ {max_l}")
            found = True
            break
    
    if not found:
        st.warning("만렙이시거나 범위를 벗어났습니다. 헬 바알런을 추천합니다!")