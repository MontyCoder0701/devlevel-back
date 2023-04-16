from model import *

def get_top_languages() -> list:
    elements = repo_soup.select("span[itemprop='programmingLanguage']")
    texts = [element.text for element in elements]
    return texts

def get_contributions_count() -> int:
    contributions_h2 = default_soup.find("h2", class_="f4 text-normal mb-2")
    contributions_count = contributions_h2.get_text(strip=True).split()[0].replace(",", "")
    return int(contributions_count)


def get_years_active() -> int:
    buttons = default_soup.find_all("a", class_="js-year-link")
    count = 0
    for button in buttons:
        if f"/{username}?tab=overview" in button["href"]:
            count += 1
            
    return count
