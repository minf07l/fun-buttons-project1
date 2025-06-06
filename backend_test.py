import requests
import unittest
import random
import sys

class NumberStorageAPITest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Use the public endpoint from frontend/.env
        self.base_url = "https://57d21022-86b2-4084-83c3-ff742fa47d05.preview.emergentagent.com/api"
        self.tests_run = 0
        self.tests_passed = 0

    def setUp(self):
        """Setup before each test"""
        self.tests_run += 1
        print(f"\n🔍 Running test: {self._testMethodName}")

    def test_01_api_root(self):
        """Test the API root endpoint"""
        url = f"{self.base_url}/"
        print(f"Testing API root at: {url}")
        
        try:
            response = requests.get(url)
            self.assertEqual(response.status_code, 200)
            data = response.json()
            self.assertEqual(data["message"], "Number Storage API")
            print("✅ API root endpoint working correctly")
            self.tests_passed += 1
        except Exception as e:
            print(f"❌ API root test failed: {str(e)}")
            raise

    def test_02_save_number(self):
        """Test saving a number"""
        url = f"{self.base_url}/save-number"
        test_number = random.uniform(1, 1000)
        print(f"Testing save number at: {url} with number: {test_number}")
        
        try:
            response = requests.post(url, json={"number": test_number})
            self.assertEqual(response.status_code, 200)
            data = response.json()
            self.assertTrue(data["success"])
            self.assertEqual(data["number"], test_number)
            print(f"✅ Successfully saved number: {test_number}")
            self.tests_passed += 1
            return test_number
        except Exception as e:
            print(f"❌ Save number test failed: {str(e)}")
            raise

    def test_03_get_number(self):
        """Test retrieving the last saved number"""
        # First save a number
        saved_number = self.test_02_save_number()
        
        # Then retrieve it
        url = f"{self.base_url}/get-number"
        print(f"Testing get number at: {url}")
        
        try:
            response = requests.get(url)
            self.assertEqual(response.status_code, 200)
            data = response.json()
            self.assertTrue(data["exists"])
            self.assertEqual(data["number"], saved_number)
            print(f"✅ Successfully retrieved number: {data['number']}")
            self.tests_passed += 1
        except Exception as e:
            print(f"❌ Get number test failed: {str(e)}")
            raise

    def test_04_get_number_when_empty(self):
        """Test retrieving when no number is saved (requires DB reset)"""
        # This test assumes we have a way to clear the database
        # Since we don't have direct DB access, we'll just check the response format
        url = f"{self.base_url}/get-number"
        print(f"Testing get number format at: {url}")
        
        try:
            response = requests.get(url)
            self.assertEqual(response.status_code, 200)
            data = response.json()
            # We can't assert exists=False since we just saved a number
            # But we can check the response structure
            self.assertIn("exists", data)
            self.assertIn("number", data)
            print("✅ Get number endpoint returns correct format")
            self.tests_passed += 1
        except Exception as e:
            print(f"❌ Get number format test failed: {str(e)}")
            raise

    def test_05_save_invalid_number(self):
        """Test saving an invalid number (string instead of number)"""
        url = f"{self.base_url}/save-number"
        print(f"Testing save invalid number at: {url}")
        
        try:
            response = requests.post(url, json={"number": "not-a-number"})
            # Expect a validation error (422 Unprocessable Entity)
            self.assertEqual(response.status_code, 422)
            print("✅ API correctly rejected invalid number format")
            self.tests_passed += 1
        except Exception as e:
            print(f"❌ Save invalid number test failed: {str(e)}")
            raise

    def tearDown(self):
        """Cleanup after each test"""
        print(f"Test {self._testMethodName} completed")

    def print_summary(self):
        """Print test summary"""
        print("\n" + "="*50)
        print(f"📊 Test Summary: {self.tests_passed}/{self.tests_run} tests passed")
        print("="*50)
        return self.tests_passed == self.tests_run

def main():
    """Run all tests"""
    test_suite = unittest.TestSuite()
    test_suite.addTest(NumberStorageAPITest('test_01_api_root'))
    test_suite.addTest(NumberStorageAPITest('test_02_save_number'))
    test_suite.addTest(NumberStorageAPITest('test_03_get_number'))
    test_suite.addTest(NumberStorageAPITest('test_04_get_number_when_empty'))
    test_suite.addTest(NumberStorageAPITest('test_05_save_invalid_number'))
    
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(test_suite)
    
    # Create an instance to print summary
    test_instance = NumberStorageAPITest()
    test_instance.tests_run = len(result.failures) + len(result.errors) + result.testsRun - len(result.failures) - len(result.errors)
    test_instance.tests_passed = test_instance.tests_run - len(result.failures) - len(result.errors)
    success = test_instance.print_summary()
    
    return 0 if success else 1

if __name__ == "__main__":
    sys.exit(main())
