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


def analyze_languages() -> str:
    languages = get_top_languages()
    if len(languages) == 0:
        return "Not enough languages to analyze"
    else:
        backend_count = 0
        frontend_count = 0
        for language in languages:
            if language in backend_lang:
                backend_count += 1
            if language in frontend_lang:
                frontend_count += 1

        if abs(backend_count - frontend_count) < 3:
            return "Fullstack"
        else:
            if backend_count > frontend_count:
                return "Backend"
            if frontend_count > backend_count:
                return "Frontend"
            

def analyze_contributions() -> str:
    contributions = get_contributions_count()
    if contributions <= 100:
        return "Low activity"
    elif contributions <= 300:
        return "Medium activity"
    else:
        return "High activity"
 

def analyze_years_active() -> str:
    years_active = get_years_active()
    if years_active <= 1:
        return "Newbie"
    elif years_active <= 5:
        return "Junior"
    else:
        return "Senior"

