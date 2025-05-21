from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from threading import Thread
from pathlib import Path
from ftplib import FTP
import os
import time

# Setup Firefox options (optional)
options = Options()
version_required = input("Enter the version required: ")
print("wait for prompt...... ")

download_dir = str(Path.home() / "Downloads")
driver = webdriver.Firefox(service=Service(), options=options)

driver.get("https://firepower-engfs-sjc.cisco.com/pix-asa-image/")
driver.implicitly_wait(10)

def find_links():
    links = driver.find_elements(By.TAG_NAME, "a")
    return links


def find_version():
    found = False
    link.click()
    driver.implicitly_wait(10)
    sub_links = find_links()
    for sub_link in sub_links:
        href_1 = sub_link.get_attribute("href")
        text_1 = sub_link.text.strip()
        if text_1 == '../':
            back_link_1 = sub_link
        else:
            if href_1 and text_1:
                if version_required in text_1:
                    sub_link.click()
                    driver.implicitly_wait(10)
                    found = True
                    break
    return found,back_link_1





found = False
unique_links = set()
links = find_links()

for i in range(len(links)):
    links = find_links()
    link = links[i]
    href = link.get_attribute("href")
    text = link.text.strip()
    print(f"{text}")
    if href and text:
        if text == '../':
            back_link = link
        if text != '../':
            found,back_link_1 = find_version()
            if found:
                break
            back_link_1.click()
            driver.implicitly_wait(10)
links = find_links()
for link in links:
    href = link.get_attribute("href")
    text = link.text.strip()
    if (href and text):
        print(f"{text}")


file_to_download = input("Enter the file to download: ")



for link in links:
    href = link.get_attribute("href")
    text = link.text.strip()
    if (href and text) and (file_to_download == text):
        link.click()
        print(f"Downloading {text}...")
        time.sleep(5)
        break


def wait_for_downloads(folder, timeout=1000):
    seconds = 0
    while seconds < timeout:
        time.sleep(1)
        if not any(fname.endswith(".part") for fname in os.listdir(folder)):
            return True
        time.sleep(1)
        seconds += 1
    return False

wait_var = wait_for_downloads(download_dir)

if wait_var:
    print("Download completed successfully.")



FTP_HOST = "10.126.211.161"
FTP_USER = "admin"
FTP_PASS = "roZes123"

ftp = FTP(FTP_HOST)
ftp.login(FTP_USER, FTP_PASS)
ftp.cwd('/test_data/common/')

ASA_file = Path(rf'{download_dir}\{file_to_download}')

with open(ASA_file, "rb") as file:
    ftp.storbinary(f"STOR " + os.path.basename(ASA_file), file)
print("------------ Uploaded ASA  file Successfully!!! ----------------")