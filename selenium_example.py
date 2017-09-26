# Must: import unittest library
import unittest

# Must: import 'webdriver' library
from selenium import webdriver

# Optional: import 'By' for ease of use
from selenium.webdriver.common.by import By

# Optional: import 'sleep' for browser's time issues
from time import sleep

# Global 'url' variable to set the relevant website where we run our tests
url = "http://blazedemo.com"

"""Create a class 'purchaseTicketTest' that includes:

1. setUp - ChromeDriver initiation
2. functions - that can be used throughout the project
3. test steps - that run one after another
4. tearDown - Closing ChromeDriver

"""

class purchaseTicketTest(unittest.TestCase):

   def setUp(self):

       """ Create ChromeDriver instance with blank page, wait policy of 10 seconds and maximize the window"""

       # Initiate ChromeDriver instance
       self.driver = webdriver.Chrome()

       # Open 'blazedemo.com' home page
       self.driver.get("http://blazedemo.com")

       # Set default timeout for locating and element in the DOM (10 seconds)
       self.driver.implicitly_wait(10)

       # Maximize window
       self.driver.maximize_window()



   def save_screenshot(self):
       """ Save screenshot """
       name = "Blazedemo_screenshot"
       self.driver.get_screenshot_as_file(name + ".png")

   def verify_url(self, actual_url, expected_url):
       """ Compare 2 arguments """
       unittest.TestCase.assertEquals(self, actual_url, expected_url,
                                      "Actual url: " + actual_url + " is not equal to expected url: " + expected_url)

   def find_flight_ticket(self):
       """ Find flight tickets """

       # Choose departure city
       self.driver.find_element(By.XPATH, "//select[@name='fromPort']/option[text()='Mexico City']").click()

       # Choose destination city
       self.driver.find_element(By.XPATH, "//select[@name='toPort']/option[text()='New York']").click()

       # Find Flights
       self.driver.find_element(By.CLASS_NAME, 'btn-primary').click()

       # For debugging purpose
       sleep(3)

       actual_url = self.driver.current_url
       # Verify the actual URL is equal to the expected URL
       self.verify_url(actual_url=actual_url, expected_url="http://blazedemo.com/reserve.php")

   def choose_flights(self):
       """ Choose the relevant flight """

       self.driver.find_element(By.CLASS_NAME, "btn-small").click()

       # For debugging purpose
       sleep(3)

       actual_url = self.driver.current_url
       # Verify the actual URL is equal to the expected URL
       self.verify_url(actual_url=actual_url, expected_url="http://blazedemo.com/purchase.php")

   def purchase_flight(self):
       """ Purchase flight and fill out form"""
       self.driver.find_element(By.ID, 'inputName').send_keys("Michael Jordan")
       self.driver.find_element(By.ID, 'address').send_keys("75th Avenue")
       self.driver.find_element(By.ID, 'city').send_keys("Chicago")
       self.driver.find_element(By.ID, 'state').send_keys("Illinois")
       self.driver.find_element(By.ID, 'zipCode').send_keys("12345")
       self.driver.find_element(By.ID, 'creditCardNumber').send_keys("4580123412341234")
       self.driver.find_element(By.ID, 'nameOnCard').send_keys("Air Mike")

       # Click purchase flight
       self.driver.find_element(By.CLASS_NAME, 'btn-primary').click()

       # For debugging purpose
       sleep(3)

       actual_url = self.driver.current_url
       # Verify the actual URL is equal to the expected URL
       self.verify_url(actual_url=actual_url, expected_url="http://blazedemo.com/confirmation.php")

   def capture_flight_ticket_confirmation(self):
       """ Capture flight ticket order screenshot """
       sleep(3)
       self.save_screenshot()

   def test_method(self):

       # Test step #1
       self.find_flight_ticket()

       # Test step #2
       self.choose_flights()

       # Test step #3
       self.purchase_flight()

       # Test step #4
       self.capture_flight_ticket_confirmation()

   def tearDown(cls):
       """ Close ChromeDriver """
       cls.driver.quit()