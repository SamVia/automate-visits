import time
import random
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

# Initialize the Chrome webdriver
driver = webdriver.Chrome()

# Navigate to the website
driver.get("https:/clockino.streamlit.app")

# Wait for the page to load
time.sleep(10)

# Get the dimensions of the window
window_width = driver.execute_script("return window.innerWidth;")
window_height = driver.execute_script("return window.innerHeight;")

# Perform random clicks on the screen
for _ in range(5):
    x = random.randint(0, window_width)
    y = random.randint(0, window_height)
    actions = ActionChains(driver)
    actions.move_to_element_with_offset(driver.find_element_by_tag_name('body'), x, y).click().perform()
    time.sleep(1)

# Close the browser
driver.quit()
