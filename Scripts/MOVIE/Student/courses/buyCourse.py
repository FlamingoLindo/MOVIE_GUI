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

def buy_course_func():

    # Path to your ChromeDriver
    driver_path = os.path.join(get_base_path(), 'chromedriver.exe')
    s = Service(driver_path)
    driver = webdriver.Chrome(service=s)  

    # Open the web page
    driver.get(os.getenv('STUDENT_URL'))

    # Initialize WebDriverWait
    wait = WebDriverWait(driver, 5)
    time.sleep(2)

    # Login
    login = get_user_input("Student's login")
    email_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/main/div/form/div[1]/label/input')))
    email_input.send_keys(login)

    password = get_user_input("Student's password")
    password_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/main/div/form/div[2]/label/input')))
    password_input.send_keys(password)
    pyautogui.press('enter')
    
    
    a = wait.until(EC.element_to_be_clickable
                        ((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/div[3]/div[2]/button'))).click()

    time.sleep(3)
    
    buy_amount_str = get_user_input("BUY THIS COURSE HOW MANY TIMES")
    buy_amount_int = int(buy_amount_str)
    
    course_id = get_user_input("WHATS THE COURSE ID")
    
    for _ in range(buy_amount_int):
        
        driver.get(f'https://plataforma-mestres-educacao.vercel.app/curso/{course_id}/subscription')

        time.sleep(2.5)

        buy = wait.until(EC.element_to_be_clickable
                        ((By.XPATH, '//*[@id="__next"]/main/div[2]/form/section/div[3]/button'))).click()

        buy_now = wait.until(EC.element_to_be_clickable
                            ((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/div/button'))).click()
        
        time.sleep(0.5)
