from flask import Flask, request, jsonify, render_template
from modules.recommendation import get_recommendations, extract_strain_info
from modules.preprocessing import df

app = Flask(__name__)

# Route to render the homepage
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle the strain recommendation logic
@app.route('/recommend', methods=['POST'])
def recommend():
    user_preferences = request.get_json()

    # Get recommendations using the get_recommendations function
    # Assuming get_recommendations returns distances and indices
    distances, indices = get_recommendations(user_preferences)

    # Extract strain information using the imported function
    recommended_strains = extract_strain_info(df, indices)

    return jsonify(recommended_strains)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
