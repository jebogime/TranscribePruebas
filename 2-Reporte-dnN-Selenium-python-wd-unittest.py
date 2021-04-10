# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class PaiwebReporteDnn(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.blazedemo.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_paiweb_reporte_dnn(self):
        driver = self.driver
        # Label: Test
        # ERROR: Caught exception [ERROR: Unsupported command [resizeWindow | 1366,568 | ]]
        driver.get("https://otranscribe.com/")
        driver.find_element_by_css_selector("div.ext-input-field > label > input[type=\"text\"]").clear()
        driver.find_element_by_css_selector("div.ext-input-field > label > input[type=\"text\"]").send_keys("https://www.youtube.com/watch?v=OwGG5fX7bxY")
        driver.find_element_by_css_selector("div.ext-input-field > label > input[type=\"text\"]").send_keys(Keys.ENTER)
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=3 | ]]
        driver.find_element_by_css_selector("button.ytp-play-button.ytp-button").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | relative=parent | ]]
        driver.find_element_by_css_selector("i.fa.fa-pause").click()
        driver.find_element_by_css_selector("i.fa.fa-play").click()
        driver.find_element_by_css_selector("div.title").click()
        driver.find_element_by_css_selector("i.fa.fa-pause").click()
        driver.find_element_by_css_selector("i.fa.fa-play").click()
        driver.find_element_by_css_selector("span").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
