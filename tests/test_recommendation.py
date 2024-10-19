import unittest 
from sklearn.neighbors import NearestNeighbors
from app import df

class RecommendationLogicTests(unittest.TestCase):
    def setUp(self):
        # Set up the feature matrix for NearestNeighbors
        self.features = df.drop(['name', 'type', 'description'], axis=1).values
        self.model = NearestNeighbors(n_neighbors=5)
        self.model.fit(self.features)

    def test_kneighbors_output(self):
        # Sample user input (make sure this has the correct number of features)
        user_input = [[0.2, 0.5, 0.7, 0.1, 0.3, 0.4, 0.6, 0.8, 0.5, 0.2, 0.9, 0.1, 0.0, 0.7, 0.3, 0.6, 0.4, 0.7, 0.5]]  
        
        distances, indices = self.model.kneighbors(user_input)
        
        # Ensure that the output contains 5 recommendations
        self.assertEqual(len(indices[0]), 5)

        # Check if the distances are valid
        self.assertTrue(all(d >= 0 for d in distances[0]))

if __name__ == '__main__':
    unittest.main()

