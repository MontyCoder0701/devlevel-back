import requests
from bs4 import BeautifulSoup

username = input("Enter your username (case sensitive): ")
url = f"https://github.com/{username}"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

contributions_h2 = soup.find("h2", class_="f4 text-normal mb-2")
contributions_count = contributions_h2.get_text(strip=True).split()[0]

print(f"Number of contributions in the last year: {contributions_count}")


buttons = soup.find_all("a", class_="js-year-link")
count = 0
for button in buttons:
    if f"/{username}?tab=overview" in button["href"]:
        count += 1

print(f"Number of years active on Github: {count}")
