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

load_dotenv()

def get_user_input(prompt):
    root = tk.CTk()
    root.withdraw()  # Hide the main window

    user_input = simpledialog.askstring("Input", prompt)

    return user_input

def duplicate_course_func():
    print("""
        ____  ______   _________    ____  ______________  ____
       / __ )/ ____/  / ____/   |  / __ \/ ____/ ____/ / / / /
      / __  / __/    / /   / /| | / /_/ / __/ / /_  / / / / /
     / /_/ / /___   / /___/ ___ |/ _, _/ /___/ __/ / /_/ / /___
    /_____/_____/   \____/_/  |_/_/ |_/_____/_/    \____/_____/
    """)


    # Path to your ChromeDriver
    driver_path = './chromedriver.exe'
    s = Service(driver_path)
    driver = webdriver.Chrome(service=s)  

    # Open the web page
    driver.get(os.getenv('MOVIE_URL'))

    # Initialize WebDriverWait
    wait = WebDriverWait(driver, 5)
    time.sleep(2)

    # Wait for email input to be clickable
    email = get_user_input("Company's email")
    email_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/main/form/div[2]/div[1]/label/input')))
    email_input.send_keys(email)

    # Wait for password input to be clickable
    password = get_user_input("Company's password")
    password_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/main/form/div[2]/div[2]/label/input')))
    password_input.send_keys(password)
    pyautogui.press('enter')

    courses = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[1]/div[2]/ul/li[2]/a')))
    courses.click()

    open_course = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[3]/section/div[1]/table/tbody/tr[1]/td[8]/div/a')))
    open_course.click()

    for i in range(999999999):
        print(f"Iteration number: {i + 1}")

        dup = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[1]/div[2]/button')))
        dup.click()
        ok = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/button')))
        ok.click()
        
        

    # Close the browser
    driver.quit()
