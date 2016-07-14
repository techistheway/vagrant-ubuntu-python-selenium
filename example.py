#!/usr/bin/env python3
from selenium import webdriver

driver = webdriver.Chrome()

driver.get("http://www.google.com")

try:
    assert "Google" in driver.title
    print("Found Google!")
except:
    print("Google was not found!")
driver.close()
