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


def get_years_active(default_soup):
    buttons = default_soup.find_all("a", class_="js-year-link")
    return len(buttons)


def analyze_stack(languages):
    if not languages:
        return None
    else:
        backend_count, frontend_count, _ = count_languages(languages)
        
        if abs(backend_count - frontend_count)/ len(languages) <= 0.2:
            return "Fullstack"
        elif backend_count > frontend_count:
            return "Backend" 
        else:
            return "Frontend"


def analyze_languages(languages):
    if not languages:
        return None
    else:
        _, _, top_languages = count_languages(languages)
        
        return top_languages


def count_languages(languages):
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
    
    return backend_count, frontend_count, top_languages

def analyze_contributions(contributions):
    if not contributions:
        return None
    else:
        if contributions <= 50:
            return "Ghost"
        elif contributions <= 100:
            return "Low"
        elif contributions <= 300:
            return "Medium"
        else:
            return "High"


def analyze_expertise(years_active):
    if not years_active:
        return None
    else:
        if years_active <= 1:
            return "Newbie"
        elif years_active <= 5:
            return "Junior"
        else:
            return "Senior"

def analyze_years_active(years_active):
    if not years_active:
        return None
    else:
        return years_active 
