from korail2 import Korail, KorailError
import time

def check_seat_availability(user_id, user_pw, dep='동대구', arr='서울', date='20260413', time_str='120000'):
    try:
        # 1. 로그인
        korail = Korail(user_id, user_pw)
        
        # 2. 열차 조회
        # date: YYYYMMDD, time_str: HHMMSS
        trains = korail.search_train(dep, arr, date, time_str)
        
        print(f"\n📢 {date} {dep} -> {arr} 열차 조회 결과:")
        print("-" * 50)
        
        for train in trains:
            # 좌석 상태 확인 (일반실 기준)
            # seat_status는 보통 '예약가능', '매진', '발매제외' 등으로 표시됩니다.
            status = train.general_seat_state
            
            print(f"[{train.train_name}] {train.dpt_time} 출발 | 상태: {status}")
            
            # 특정 열차만 찾고 싶다면 아래와 같이 조건문을 걸 수 있습니다.
            # if train.dpt_time == '143000':
            #     return "예약 가능" if "예약" in status else "매진"

    except KorailError as e:
        if "MACRO" in str(e):
            return "❌ 매크로 방지 로직에 의해 차단되었습니다. 잠시 후 시도하세요."
        else:
            return f"❌ 코레일 에러 발생: {e}"
    except Exception as e:
        return f"❌ 알 수 없는 오류: {e}"

# 사용 예시 (본인의 멤버십 번호와 비밀번호 입력)
result = check_seat_availability('0651260178', 'spare2387!')
print(result)