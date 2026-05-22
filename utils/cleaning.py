# Import Clean Dataset
import pandas as pd
import os
import re

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
file_path = os.path.join(BASE_DIR, 'datasets', 'clean_resume_data.csv')
clean_df = pd.read_csv(file_path)
def cleanResume(text):
    text = text.lower()
    text = re.sub(r'\d+', ' ', text)
    text = re.sub(r'[^a-zA-Z ]', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()
clean_df['Feature'] = clean_df['Feature'].fillna('').apply(cleanResume)
