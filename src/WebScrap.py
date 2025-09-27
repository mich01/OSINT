import requests
from bs4 import BeautifulSoup
response = requests.get("https://kenyan-post.com/category/news/")
soup = BeautifulSoup(response.content, 'html.parser')
titles = soup.findAll("h3")
for title in titles:
    print(title.text)