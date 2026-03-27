from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Setup ChromeOptions
options = Options()
options.add_experimental_option("detach", True) # Keeps browser open

# --- ADDING THESE LINES TO BYPASS BOT DETECTION ---
# if you dont put the lines below then the browser will detect that the browser is being controlled by automated software and will not allow you to access the website and will show you a captcha to solve

# Removes the "Chrome is being controlled by automated software" banner
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

# Disables the flag that tells websites you are using an automated webdriver
options.add_argument("--disable-blink-features=AutomationControlled")

# (Optional) Set a realistic User-Agent so Google thinks you are a normal user
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
# -----------------------------------------------


brave_path = r"C:\Users\biswa\AppData\Local\BraveSoftware\Brave-Browser\Application\brave.exe"
options.binary_location = brave_path


driver = webdriver.Chrome(options=options)

driver.get("https://www.python.org")
assert 'Python' in driver.title


elem = driver.find_element(By.NAME, 'q')
elem.clear()                # By running elem.clear() first, it acts like pressing Backspace repeatedly until the box is completely empty.
elem.send_keys('jsighseoigjhoahs', Keys.ENTER)
assert 'NO RESULTS FOUND' not in driver.page_source

# time.sleep(5)
# driver.close()
