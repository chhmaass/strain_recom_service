import unittest
import pandas as pd
from sklearn.impute import KNNImputer
import sys
import os
from modules.preprocessing import df, percent_columns

# Include the parent directory in sys.path
#sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))



class DataPreprocessingTests(unittest.TestCase):
    def test_percentage_conversion(self):
        # Check if percentage columns have been converted to float
        for col in percent_columns:
            self.assertTrue(pd.api.types.is_float_dtype(df[col]))

    def test_missing_values_imputation(self):
        # Test if KNN imputation has filled missing values in the 'thc_level'
        imputer = KNNImputer(n_neighbors=3)
        thc_values = df[['thc_level']].copy()
        imputed_values = imputer.fit_transform(thc_values)
        # Ensure no NaN values remain after imputation
        self.assertFalse(pd.isnull(imputed_values).any())

    def test_type_description_fillna(self):
        # Ensure 'type' and 'description' columns have no missing values
        self.assertFalse(df['type'].isnull().any())
        self.assertFalse(df['description'].isnull().any())

if __name__ == '__main__':
    unittest.main()
