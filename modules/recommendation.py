import pandas as pd
from sklearn.neighbors import NearestNeighbors
from modules.preprocessing import df, effects

# Extract features and initialize model
features = df.drop(['name', 'type', 'description', 'thc_level'], axis=1)
model = NearestNeighbors(n_neighbors=5)
model.fit(features)

def get_recommendations(user_preferences):
    # Prepare the user input based on the sliders
    user_input = [[
        user_preferences['anxious'],
        user_preferences['aroused'],
        user_preferences['creative'],
        user_preferences['dizzy'],
        user_preferences['dry_eyes'],
        user_preferences['dry_mouth'],
        user_preferences['energetic'],
        user_preferences['euphoric'],
        user_preferences['focused'],
        user_preferences['giggly'],
        user_preferences['happy'],
        user_preferences['hungry'],
        user_preferences['paranoid'],
        user_preferences['relaxed'],
        user_preferences['sleepy'],
        user_preferences['talkative'],
        user_preferences['tingly'],
        user_preferences['uplifted']
    ]]
    
    # Prepare user input as a DataFrame with correct feature names
    user_input_df = pd.DataFrame(user_input, columns=effects)
    
    # Get the 5 nearest strains
    distances, indices = model.kneighbors(user_input_df)

    return distances, indices  # Ensure you return these values

def extract_strain_info(df, indices):
    recommended_strains = []
    for idx in indices[0]:  # Assuming indices is a 2D array
        strain_info = {
            'name': df.iloc[idx]['name'],
            'type': df.iloc[idx]['type'],
            'description': df.iloc[idx]['description'],
            'thc_level': round(df.iloc[idx]['thc_level'], 1)
        }
        recommended_strains.append(strain_info)
    return recommended_strains