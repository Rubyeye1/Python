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
    if not website.startswith("https://"):
     website = f"https://{website}"
    response = get(website)
    if response.status_code == 200:
       results[website] = "OK"
    else:
       results[website] = "FAILED"

print(results)

