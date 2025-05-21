from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

import time

# Setup Firefox options (optional)
options = Options()
version_required = input("Enter the version required: ")
image_type = input("Enter the image type (e.g., 'yemen','zambia'): ")
device_type = input("Enter the device type (e.g., 'BS','KP','TPK): ")

if device_type == "BS":
    device_name = ".SPA.csp"
elif device_type == "KP":
    device_name = f"cisco-asa-fp2k.{version_required}.SPA"
elif device_type == "TPK":
    device_name = f"cisco-asa-fp3k.{version_required}.SPA"

print(f"Device name: {device_name}")
driver = webdriver.Firefox(service=Service(), options=options)

driver.get("https://firepower-engfs-sjc.cisco.com/pix-asa-image/")
time.sleep(2)

def find_links():
    links = driver.find_elements(By.TAG_NAME, "a")
    return links

# Use a set to store unique (text, href) pairs
unique_links = set()
links = find_links()
# Loop through all found <a> tags
for link in links:
    href = link.get_attribute("href")
    text = link.text.strip()
    if href and text:  # Avoid empty text or href
        unique_links.add((text, href))
        # print(f"{text}: {href}")
        if image_type in text.lower():
            # print(f"Found link with 'yemen': {text}: {href}")
            link.click()
            break
links = find_links()

for link in links:
    href = link.get_attribute("href")
    text = link.text.strip()
    if href and text:  # Avoid empty text or href
        unique_links.add((text, href))
        if version_required in text.lower():
            print(f"Found link with 'yemen': {text}: {href}")
            link.click()
            break

links = find_links()
for link in links:
    href = link.get_attribute("href")
    text = link.text.strip()
    if href and text:  # Avoid empty text or href
        if device_name == text:
            print(f"Found link with '{device_name}': {text}: {href}")
            link.click()
            break


# Close the browser
time.sleep(5)