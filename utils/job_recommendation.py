import pandas as pd
import pickle
from sklearn.metrics.pairwise import cosine_similarity

# load
job_df = pd.read_csv("datasets/job_dataset.csv")
vectorizer = pickle.load(open("model/category_vectorizer.pkl", "rb"))

def recommend_job(resume_text,category):

    resume_vec = vectorizer.transform([resume_text])
    job_vec = vectorizer.transform(job_df['Feature'])

    similarity = cosine_similarity(resume_vec, job_vec)[0]

    #  threshold filter (important)
    threshold = 0.15
    valid_idx = [i for i, s in enumerate(similarity) if s > threshold]

    # fallback
    if len(valid_idx) == 0:
        valid_idx = similarity.argsort()[-5:]

    # sort
    top_idx = sorted(valid_idx, key=lambda i: similarity[i], reverse=True)[:5]

    return list(job_df.iloc[top_idx]['Role'].unique())[:3]