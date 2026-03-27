from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

options = Options()
options.add_experimental_option("detach", True) 

# -----------------------------------------------
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

options.add_argument("--disable-blink-features=AutomationControlled")

options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
# -----------------------------------------------


brave_path = r"C:\Users\biswa\AppData\Local\BraveSoftware\Brave-Browser\Application\brave.exe"
options.binary_location = brave_path


driver = webdriver.Chrome(options=options)

search = "i phones"
driver.get(f"https://www.amazon.in/s?k={search}&ref=nb_sb_noss")

elements = driver.find_elements(By.CLASS_NAME, "puisg-row")
for element in elements:
    print(element.text)         # will print all the elements inside the designated class

# print(element.get_attribute("outerHTML"))       # will give entire html of the mentioned class

# innerHTML gives you everything inside the element (but excludes the element itself). outerHTML gives you everything inside the element, plus the element itself.


driver.close()


