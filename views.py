from flask import jsonify
from model import *
from collections import Counter

def get_top_languages(repo_soup):
    elements = repo_soup.select("span[itemprop='programmingLanguage']")
    texts = [element.text for element in elements]
    return texts


def get_contributions_count(default_soup):
    contributions_h2 = default_soup.find("h2", class_="f4 text-normal mb-2")
    contributions_count = contributions_h2.get_text(strip=True).split()[0].replace(",", "")
    return int(contributions_count)


def get_years_active(default_soup, username):
    buttons = default_soup.find_all("a", class_="js-year-link")
    count = 0
    for button in buttons:
        if f"/{username}?tab=overview" in button["href"]:
            count += 1
    return count


def analyze_languages(languages):
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
    
        if len(languages) >=  3:
            top_languages = Counter(languages).most_common(3)
        else:
            top_languages = Counter(languages).most_common(len(languages))
        top_languages = [language[0] for language in top_languages]

        if abs(backend_count - frontend_count)/ len(languages) <= 0.2:
            return "🎩 Fullstack with " + ", ".join(top_languages)
        else:
            if backend_count > frontend_count:
                return "🛠️ Backend with " + ", ".join(top_languages)
            if frontend_count > backend_count:
                return "🖥️ Frontend  with " + ", ".join(top_languages)
            

def analyze_contributions(contributions):
    if contributions <= 50:
        return "👻 Ghost user"
    elif contributions <= 100:
        return "💤 Low activity"
    elif contributions <= 300:
        return "🏃🏻 Medium activity"
    else:
        return "🤸🏼‍♀️ High activity"
 

def analyze_years_active(years_active):
    if years_active <= 1:
        return f"🐥 Newbie for {years_active} year"
    elif years_active <= 5:
        return f"🌱 Junior for {years_active} years"
    else:
        return f"👨‍🎓 Senior for {years_active} years"

