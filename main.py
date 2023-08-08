import requests
from bs4 import BeautifulSoup

# 從網址獲取 HTML 內容
url = 'https://hang5888.github.io/EWSPTEST/'
response = requests.get(url)

# 確保請求成功
response.raise_for_status()

# 使用 BeautifulSoup 解析 HTML 內容
soup = BeautifulSoup(response.text, 'html.parser')

# 查找並提取特定的資料
# 此範例提取所有 <h1> 標籤的文字
h1_tags = soup.find_all('pre')
for tag in h1_tags:
    print(tag.get_text())
