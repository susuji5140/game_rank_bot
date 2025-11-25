import requests
import json
import os

# 1. API 주소
url = "https://www.thelog.co.kr/api/common/getCommonState.do?gameDataType=S"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
    "Referer": "https://www.thelog.co.kr/index.do"
}

try:
    print("데이터 요청 중...")
    
    # 2. 데이터 가져오기
    response = requests.get(url, headers=headers)
    data = response.json()
    rank_list = data.get('gameRank', [])

    print(f"총 {len(rank_list)}개의 게임 순위를 찾았습니다.")
    
    # 3. 필요한 정보만 골라내기 (1위~20위)
    clean_data = []
    for item in rank_list[:20]:
        clean_data.append({
            "rank": item['gameRank'],       
            "name": item['gameName'],       
            "share": item['gameShares'],    
            "updown": item['gameRankUpDown'] 
        })

    # 4. JSON 파일 저장
    with open('game_data.json', 'w', encoding='utf-8') as f:
        json.dump(clean_data, f, ensure_ascii=False, indent=4)
        
    print("✅ 업데이트 완료!")

except Exception as e:
    print(f"❌ 에러 발생: {e}")
    exit(1)
