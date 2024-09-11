import json
import unittest

from tkbl import (
    bps_a1_by_uniformat_code,
    bps_a2_by_uniformat_code,
    bsync_by_uniformat_code,
    federal_bps_by_uniformat_code,
    filter_by_uniformat_code,
)


class TestTkbl(unittest.TestCase):
    def test_filter_by_uniformat_code_valid(self):
        # Example of a valid uniformat code that returns results
        valid_code = 'B202001'
        expected_output = json.loads("""
        [{"category": "Doors and Windows", "subcategory": "Storm Windows", "uniformat code": "B202001", "uniformat description": "WINDOWS", "url": "https://sftool.gov/greenprocurement/green-products/26/doors-windows/1827/storm-windows/0?addon=False", "title": ""}]
        """)
        result = json.loads(filter_by_uniformat_code(valid_code))
        self.assertEqual(result[0]['category'], expected_output[0]['category'])

    def test_filter_by_uniformat_code_invalid(self):
        # Example of an invalid uniformat code that returns no results
        invalid_code = 'XYZ123'
        result = filter_by_uniformat_code(invalid_code)
        self.assertEqual(result, '[]')  # Assuming function returns an empty JSON array for invalid codes

    def test_bsync_by_uniformat_code_d5010(self):
        # Test the bsync_by_uniformat_code function with 'D5010'
        uniformat_code = 'D5010'
        result = bsync_by_uniformat_code(uniformat_code)
        # Define the expected number of matching entries based on the sample provided
        expected_number_of_results = 17
        self.assertEqual(len(result), expected_number_of_results, "The number of matching entries should be 17 for uniformat code 'D5010'")
    
    def test_bsync_by_uniformat_code_d501090(self):
        # Test the bsync_by_uniformat_code function with 'D501090'
        uniformat_code = 'D501090'
        result = bsync_by_uniformat_code(uniformat_code)
        # Define the expected number of matching entries based on the sample provided
        expected_number_of_results = 5
        self.assertEqual(len(result), expected_number_of_results, "The number of matching entries should be 11 for uniformat code 'D5010'")

    def test_federal_bps_by_uniformat_code_d302002(self):
        # Test the federal_bps_by_uniformat_code with 'D302002'
        uniformat_code = 'D302002'
        result = federal_bps_by_uniformat_code(uniformat_code)
        # Define the expected number of matching entries based on the sample provided
        expected_number_of_results = 1
        self.assertEqual(len(result), expected_number_of_results, "The number of matching entries should be 11 for uniformat code 'D5010'")

    def test_bpsa1_by_uniformat_code_d302002(self):
        # Test the bsync_by_uniformat_code function with 'D302002'
        uniformat_code = 'D302002'
        result = bps_a1_by_uniformat_code(uniformat_code)
        # Define the expected number of matching entries based on the sample provided
        expected_number_of_results = 1118
        self.assertEqual(len(result), expected_number_of_results, "The number of matching entries should be 1118 for uniformat code 'D302002'")

    def test_bpsa2_by_uniformat_code_d202003(self):
        # Test the bsync_by_uniformat_code function with 'D202003'
        uniformat_code = 'D202003'
        result = bps_a2_by_uniformat_code(uniformat_code)
        # Define the expected number of matching entries based on the sample provided
        expected_number_of_results = 2041
        self.assertEqual(len(result), expected_number_of_results, "The number of matching entries should be 2041 for uniformat code 'D202003'")        

if __name__ == '__main__':
    unittest.main()
