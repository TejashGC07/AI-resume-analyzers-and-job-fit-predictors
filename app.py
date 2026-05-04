from flask import Flask, request, jsonify
from flask_cors import CORS
from main import extract_skills, similarity_score, missing_skills, suggestions, weighted_score

app = Flask(__name__)
CORS(app)

@app.route("/analyze", methods=["POST"])
def analyze():
    resume = request.form["resume"].lower()
    job = request.form["job"].lower()

    skills = extract_skills(resume)
    score = similarity_score(resume, job)
    weight = weighted_score(skills)
    missing = missing_skills(skills, job)
    tips = suggestions(score, missing)

    final_score = round((score * 0.6 + weight * 0.4), 2)

    return jsonify({
        "score": final_score,
        "skills": skills,
        "missing": missing,
        "tips": tips
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
