
import os
import pickle
from flask import Flask, render_template, request
#  Utils import
from utils.cleaning import cleanResume
from utils.job_recommendation import recommend_job
from utils.resume_parser import extract_text
from utils.skill_extractor import extract_skills
from utils.scoring import calculate_score
from utils.suggestions import get_suggestions


app = Flask(__name__)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# Upload folder
UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# Load model
model = pickle.load(open(os.path.join(BASE_DIR, 'model', 'category_model.pkl'), 'rb'))
vectorizer = pickle.load(open(os.path.join(BASE_DIR, 'model', 'category_vectorizer.pkl'), 'rb'))
#  Home
@app.route('/')
def home():
    return render_template("index.html")
#  Prediction
@app.route('/predict', methods=['POST'])
def predict():

    if 'resume' not in request.files:
        return "No file uploaded"

    file = request.files['resume']

    if file.filename == '':
        return "No file selected"

    #  Save file
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)

    #  Extract text (PDF/DOCX/TXT handled in parser)
    text = extract_text(filepath)

    #  Clean text
    cleaned = cleanResume(text)

    #  Predict Category
    vector = vectorizer.transform([cleaned])
    category = model.predict(vector)[0]

    #  Job Recommendation
    jobs = recommend_job(cleaned, category)

    #  Skill Extraction
    skills = extract_skills(cleaned)

    #  Resume Score
    score = calculate_score(cleaned, skills)

    #  Suggestions
    suggestions = get_suggestions(cleaned, skills)

    return render_template(
        "result.html",
        category=category,
        jobs=jobs,
        skills=skills,
        score=score,
        suggestions=suggestions
    )

if __name__ == "__main__":
   import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)