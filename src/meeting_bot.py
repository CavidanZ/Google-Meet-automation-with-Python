from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config import CHROME_DRIVER_PATH, PROFILE_PATH

def get_driver():
    options = Options()
    options.add_argument("--disable-infobars")
    options.add_argument("--start-maximized")
    options.add_argument("--disable-extensions")
    options.add_argument(f"user-data-dir={PROFILE_PATH}")  # reuse login session
    options.add_experimental_option("prefs", {
        "profile.default_content_setting_values.media_stream_mic": 2,
        "profile.default_content_setting_values.media_stream_camera": 2,
        "profile.default_content_setting_values.notifications": 2
    })
    return webdriver.Chrome(service=Service(CHROME_DRIVER_PATH), options=options)

def join_meet(link):
    driver = get_driver()
    driver.get(link)

    wait = WebDriverWait(driver, 20)

    # Turn off camera
    try:
        cam_button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "div[aria-label*='Turn off camera']"))
        )
        cam_button.click()
    except:
        print("Camera toggle not found")

    # Turn off mic
    try:
        mic_button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "div[aria-label*='Turn off microphone']"))
        )
        mic_button.click()
    except:
        print("Mic toggle not found")

    # Click "Join now"
    try:
        join_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='Join now']/.."))
        )
        join_button.click()
        print("Joined the class.")
    except:
        print("Join button not found")

    return driver  # Keep driver open so class stays connected