from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self) -> None:
        self.browser = webdriver.Edge()
    
    def tearDown(self) -> None:
        self.browser.quit()
    
    def test_can_start_a_list_and_retriver_it_later(self):
        self.browser.get("http://localhost:8000")

        self.assertIn("To-Do", self.browser.title)
        self.fail("Finish the test!")
    
if __name__ == '__main__':
    unittest.main(warnings="ignore")
