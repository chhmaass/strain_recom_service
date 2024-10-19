import unittest
import json
from app import app

class FlaskAppTests(unittest.TestCase):
    def setUp(self):
        # Set up the test client
        self.app = app.test_client()
        self.app.testing = True

    def test_homepage(self):
        # Test if the homepage loads correctly
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)
        self.assertIn(b'Strain Recommendation', result.data)  # Check for specific content in the response

    def test_recommend(self):
        # Test recommendation route with sample user input
        sample_input = {
            'anxious': 0.2,
            'aroused': 0.5,
            'creative': 0.7,
            'dizzy': 0.1,
            'dry_eyes': 0.3,
            'dry_mouth': 0.4,
            'energetic': 0.6,
            'euphoric': 0.8,
            'focused': 0.5,
            'giggly': 0.2,
            'happy': 0.9,
            'hungry': 0.1,
            'paranoid': 0.0,
            'relaxed': 0.7,
            'sleepy': 0.3,
            'talkative': 0.6,
            'tingly': 0.4,
            'uplifted': 0.7
        }

        result = self.app.post('/recommend', 
                               data=json.dumps(sample_input), 
                               content_type='application/json')
        
        self.assertEqual(result.status_code, 200)  # Check for successful response
        self.assertEqual(result.content_type, 'application/json')  # Check Content-Type
        
        data = json.loads(result.data)  # Load JSON response
        
        self.assertIsInstance(data, list)  # Ensure the response is a list
        self.assertEqual(len(data), 5)  # Ensure 5 recommendations are returned

        # Additional checks for the recommended strains
        for strain in data:
            self.assertIn('name', strain)  # Ensure 'name' is in the recommended strain
            self.assertIn('type', strain)  # Ensure 'type' is in the recommended strain
            self.assertIn('description', strain)  # Ensure 'description' is in the recommended strain
            self.assertIn('thc_level', strain)  # Ensure 'thc_level' is in the recommended strain
            self.assertIsInstance(strain['thc_level'], (int, float))  # Ensure 'thc_level' is a number

if __name__ == '__main__':
    unittest.main()

