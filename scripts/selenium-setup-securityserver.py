# -*- coding: utf-8 -*-
from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Secserv(unittest.TestCase):
    def setUp(self):
        self.display = Display(visible=0, size=(1024,768))
        self.display.start()
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        #todo: move ip to args
        self.base_url = "https://10.1.10.7:4000/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_secserv(self):
        driver = self.driver
        driver.get("https://10.1.10.7:4000/login")
        driver.get_screenshot_as_file("/tmp/screenshots/securityserver-first.png")
        self.assertEqual("Security Server Administration", driver.title)
        driver.find_element_by_id("j_username").clear()
        driver.find_element_by_id("j_username").send_keys("vagrant")
        driver.find_element_by_id("j_password").clear()
        driver.find_element_by_id("j_password").send_keys("vagrant")
        driver.find_element_by_css_selector("button.btn").click()
        self.assertEqual("Security Server Administration", driver.title)
        driver.find_element_by_id("anchor_upload_file").clear()
        # download it from centralserver first
        driver.find_element_by_id("anchor_upload_file").send_keys("/tmp/xroad6-test/anchor")
        driver.find_element_by_id("anchor_upload_submit").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException, e: return False
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
        self.display.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
