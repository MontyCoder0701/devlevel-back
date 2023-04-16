import requests
from bs4 import BeautifulSoup

username = input("Enter your GitHub username: ")

def new_url(username: str, mode:str) -> str:
    if mode == "repos":
        return f"https://github.com/{username}?tab=repositories"
    if mode == "default":
        return f"https://github.com/{username}"

def new_soup(url: str) -> BeautifulSoup:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    return soup

repo_url = new_url(username, "repos")
repo_soup = new_soup(repo_url)

default_url = new_url(username, "default")
default_soup = new_soup(default_url)

backend_lang = ["C#", "C++", "C", "Go", "Java", "PHP", "Python", "Ruby", "Rust", "Perl"]
frontend_lang = ["CSS", "HTML", "JavaScript", "TypeScript", "Kotlin", "Swift"]