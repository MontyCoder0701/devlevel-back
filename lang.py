import requests
from bs4 import BeautifulSoup

username = input("Enter your username (case sensitive): ")
url = f"https://github.com/{username}?tab=repositories"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

elements = soup.select("span[itemprop='programmingLanguage']")
texts = [element.text for element in elements]

print(f"List of top languages: {texts}")