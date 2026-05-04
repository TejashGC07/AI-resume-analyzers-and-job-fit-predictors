from flask import Flask, request, jsonify
from flask_cors import CORS
from main import extract_skills, similarity_score, missing_skills

app = Flask(__name__)
CORS(app)

@app.route("/analyze", methods=["POST"])
def analyze():
    resume = request.form["resume"]
    job = request.form["job"]

    skills = extract_skills(resume.lower())
    score = similarity_score(resume.lower(), job.lower())
    missing = missing_skills(skills, job.lower())

    return jsonify({
        "score": round(score,2),
        "skills": skills,
        "missing": missing
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
