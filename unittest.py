# abg % python -m unittest tests.test_google_api
# from utils.google_utils import get_sheet

# run_tests.py
import unittest
from tests.test_google_api import TestGoogleApi
from tests.test_playwright import TestPlaywright

if __name__ == '__main__':
    # Create a test suite that includes both test cases
    suite = unittest.TestLoader().loadTestsFromTestCase(TestGoogleApi)
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestPlaywright))

    # Run the test suite
    unittest.TextTestRunner(verbosity=2).run(suite)


# test_playwright.py
from playwright.sync_api import sync_playwright, expect
import unittest
import time

class TestPlaywright(unittest.TestCase):
    def setUp(self):
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(headless=True)
        self.page = self.browser.new_page()

    def tearDown(self):
        self.browser.close()
        self.playwright.stop()

    def test_navigation_to_google(self):
        self.page.goto("https://www.google.com")
        expect(self.page).to_have_url("https://www.google.com/")

if __name__ == "__main__":
    unittest.main()
