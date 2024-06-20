import pandas as pd
import customtkinter as tk
from tkinter import simpledialog
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from dotenv import load_dotenv
import os
import random
import pyautogui
import sys
from Scripts.MOVIE.load_paths import load_chromedriver
load_dotenv()

def get_base_path():
    # Get the base path for PyInstaller bundled app
    if hasattr(sys, '_MEIPASS'):
        return sys._MEIPASS
    else:
        return os.path.abspath(".")
    
# Load environment variables from .env file
load_dotenv(os.path.join(get_base_path(), '.env'))

def get_user_input(prompt):
    root = tk.CTk()
    root.withdraw()  # Hide the main window

    user_input = simpledialog.askstring("Input", prompt)

    return user_input

def delete_course_teacher_func():
    # Path to your ChromeDriver
    driver_path = load_chromedriver()
    s = Service(driver_path)
    driver = webdriver.Chrome(service=s)  

    # Open the web page
    driver.get(os.getenv('PROFESSOR_URL'))

    # Initialize WebDriverWait
    wait = WebDriverWait(driver, 5)
    time.sleep(2)

    # Wait for email input to be clickable
    email = get_user_input("Email")
    email_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/main/form/div[2]/div[1]/label/input')))
    email_input.send_keys(email)

    # Wait for password input to be clickable
    password = get_user_input("Password")
    password_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/main/form/div[2]/div[2]/label/input')))
    password_input.send_keys(password)
    pyautogui.press('enter')

    time.sleep(3)

    courses = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/header/div/div[1]/nav/a[2]')))
    courses.click()





    for i in range(999999999):
        print("""
                     __     __     __           __
                ____/ /__  / /__  / /____  ____/ /
               / __  / _ \/ / _ \/ __/ _ \/ __  /
              / /_/ /  __/ /  __/ /_/  __/ /_/ /
              \__,_/\___/_/\___/\__/\___/\__,_/


                """)
        print(f"Iteration number: {i + 1} 🥸👍")
        delete_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/table/tbody/tr[1]/td[9]/div/img[2]')))
        delete_btn.click()

        ok = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/div/button[2]')))
        ok.click()
        ok2 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/button')))
        ok2.click()
        time.sleep(1.5)

    # Close the browser
    driver.quit()
