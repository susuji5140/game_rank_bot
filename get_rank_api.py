import requests
import json
import time  # 시간 관련 기능 추가
import datetime

# --- 무한 반복 시작 ---
while True:
    try:
        print(f"\n[ {datetime.datetime.now()} ] 데이터 업데이트 시작...")

        # 1. 아까 짠 코드 내용 그대로...
        url = "https://www.thelog.co.kr/api/common/getCommonState.do?gameDataType=S"
        headers = { "User-Agent": "Mozilla/5.0..." } # (아까 그 헤더 내용)
        
        response = requests.get(url, headers=headers)
        data = response.json()
        rank_list = data.get('gameRank', [])

        clean_data = []
        for item in rank_list[:20]:
            clean_data.append({
                "rank": item['gameRank'],       
                "name": item['gameName'],       
                "share": item['gameShares'],    
                "updown": item['gameRankUpDown'] 
            })

        with open('game_data.json', 'w', encoding='utf-8') as f:
            json.dump(clean_data, f, ensure_ascii=False, indent=4)
            
        print("✅ 업데이트 완료! 24시간 뒤에 다시 실행됩니다.")

    except Exception as e:
        print(f"❌ 에러 발생: {e}")

    # 2. 24시간(86400초) 동안 잠자기 (대기)
    time.sleep(86400)