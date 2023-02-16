from requests import get

websites = (       
    "google.com",
    "airbnb.com",
    "https://twitter.com",
    "facebook.com",
    "https://tiktok.com"
)

results = {}

for website in websites:  # 리스트도 똑같이 동작가능
    if not website.startswith("https://"): # if not문 사용
     website = f"https://{website}"   # 문자열을 바꾸고 싶을때 f사용!
    response = get(website)           # requests 라이브러리로부터 가져온 get
    if response.status_code == 200:   # 상태코드 비교
       results[website] = "OK"        # 딕셔너리에 키와 밸류를 저장
    else:
       results[website] = "FAILED"

print(results)