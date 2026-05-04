from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def extract_skills(text):
    skills_db = ["python", "java", "c", "c++", "sql", "machine learning", "ai", "html", "css", "javascript"]
    text = text.lower()
    return [skill for skill in skills_db if skill in text]

@app.route("/")
def home():
    return "API Running"

@app.route("/analyze", methods=["POST"])
def analyze():
    resume = request.form.get("resume", "").lower()
    job = request.form.get("job", "").lower()

    resume_skills = extract_skills(resume)
    job_skills = extract_skills(job)

    matched = list(set(resume_skills) & set(job_skills))
    missing = list(set(job_skills) - set(resume_skills))

    score = (len(matched) / len(job_skills) * 100) if job_skills else 0

    return jsonify({
        "score": round(score, 2),
        "skills": matched,
        "missing": missing
    })

if __name__ == "__main__":
    app.run(debug=True)
