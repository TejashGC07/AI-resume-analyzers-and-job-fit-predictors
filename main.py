from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

skills_db = {
    "python": 0.3,
    "machine learning": 0.4,
    "sql": 0.2,
    "data analysis": 0.2,
    "java": 0.2,
    "c++": 0.2
}

def extract_skills(text):
    found = []
    for skill in skills_db:
        if skill in text:
            found.append(skill)
    return found

def similarity_score(resume, job):
    vec = TfidfVectorizer()
    tfidf = vec.fit_transform([resume, job])
    return cosine_similarity(tfidf[0], tfidf[1])[0][0] * 100

def weighted_score(skills):
    score = 0
    for s in skills:
        score += skills_db.get(s, 0)
    return min(score * 100, 100)

def missing_skills(resume_skills, job):
    return [s for s in skills_db if s in job and s not in resume_skills]

def suggestions(score, missing):
    tips = []

    if score < 40:
        tips.append("Add more relevant skills")
        tips.append("Improve resume keywords")
    elif score < 70:
        tips.append("Add projects related to job")
        tips.append("Use stronger action words")

    if missing:
        tips.append("Include missing skills: " + ", ".join(missing))

    return tips
