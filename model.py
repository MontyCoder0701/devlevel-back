import requests
from bs4 import BeautifulSoup

class Developer:
  def __init__(self, lang, activity, years):
    self.lang = lang
    self.activity = activity
    self.years = years


def new_url(username: str, mode:str) -> str:
    if mode == "repos":
        return f"https://github.com/{username}?tab=repositories"
    if mode == "default":
        return f"https://github.com/{username}"

def new_soup(url: str) -> BeautifulSoup:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    return soup


backend_lang = ["C#", "C++", "C", "Go", "Java", "PHP", "Python", "Ruby", "Rust", "Perl", "Jupyter Notebook"]
frontend_lang = ["CSS", "HTML", "JavaScript", "TypeScript", "Kotlin", "Swift"]
