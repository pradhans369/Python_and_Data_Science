from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


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

# Tell Selenium exactly where the Brave browser is installed
brave_path = r"C:\Users\mudar\AppData\Local\BraveSoftware\Brave-Browser\Application\brave.exe"
options.binary_location = brave_path

# Initialize the WebDriver using Selenium Manager (built-in)
driver = webdriver.Chrome(options=options)

# Navigate to a test website
driver.get("https://www.google.com")

# Typing into search bar
input_element = driver.find_element(By.CLASS_NAME, "gLFyf")
input_element.send_keys("Hello world", Keys.ENTER) 
# input_element.submit()        # this also works as enter button


input_element = driver.find_element(By.CLASS_NAME, "zReHs")
input_element.click()
