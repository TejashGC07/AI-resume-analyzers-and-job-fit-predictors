from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

skills_db = ["python","c++","java","machine learning","nlp","sql","iot"]

def extract_skills(text):
    return [s for s in skills_db if s in text]

def similarity_score(resume, job):
    vec = TfidfVectorizer()
    tfidf = vec.fit_transform([resume, job])
    return cosine_similarity(tfidf[0], tfidf[1])[0][0] * 100

def missing_skills(resume_skills, job):
    return [s for s in skills_db if s in job and s not in resume_skills]
