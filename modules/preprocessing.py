import pandas as pd
from sklearn.impute import KNNImputer
import os

# Construct the file path relative to the location of the current script (app.py or other script)
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Move up one directory
file_path = os.path.join(base_dir, 'strains.csv')  # Construct the path to 'strains.csv'


# Read the CSV and select required columns
required_columns = ['name', 'type', 'description', 'thc_level', 'anxious', 'aroused', 'creative', 'dizzy',
                    'dry_eyes', 'dry_mouth', 'energetic', 'euphoric', 'focused', 'giggly', 'happy',
                    'hungry', 'paranoid', 'relaxed', 'sleepy', 'talkative', 'tingly', 'uplifted']

df = pd.read_csv(file_path)[required_columns]

# Convert percentage strings to numeric values, preserving NaN
percent_columns = ['thc_level', 'anxious', 'aroused', 'creative', 'dizzy', 'dry_eyes', 'dry_mouth',
                   'energetic', 'euphoric', 'focused', 'giggly', 'happy', 'hungry', 'paranoid',
                   'relaxed', 'sleepy', 'talkative', 'tingly', 'uplifted']

df[percent_columns] = df[percent_columns].replace('%', '', regex=True).astype(float)

# Fill missing values in 'type' and 'description' columns with 'unknown'
df[['type', 'description']] = df[['type', 'description']].fillna('unknown')

# KNN imputation for 'thc_level'
imputer = KNNImputer(n_neighbors=3)
df['thc_level'] = imputer.fit_transform(df[['thc_level']])

# Select features for the model
effects = ['anxious', 'aroused', 'creative', 'dizzy', 'dry_eyes', 'dry_mouth',
                   'energetic', 'euphoric', 'focused', 'giggly', 'happy', 'hungry', 'paranoid',
                   'relaxed', 'sleepy', 'talkative', 'tingly', 'uplifted']
#features = df[effects]