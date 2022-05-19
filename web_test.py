import selenium
import time
from selenium import webdriver
path="C:/Users/CSC/Desktop/Selenium testing/chromedriver.exe"
driver=webdriver.Chrome(executable_path=path)
driver.get("https://www.google.com/")