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


    

def do_course_func():
    
    def next():
        
        first = wait.until(EC.element_to_be_clickable
                            ((By.XPATH, '//*[@id="__next"]/main/div/aside/div[2]/div[2]/button'))).click()
        time.sleep(0.5)
        second = wait.until(EC.element_to_be_clickable
                            ((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/button'))).click()
        
        
    # Path to your ChromeDriver
    driver_path = os.path.join(get_base_path(), 'chromedriver.exe')
    s = Service(driver_path)
    driver = webdriver.Chrome(service=s)  

    stu_amount_str = get_user_input("Insert the amount of students")
    stu_amount_int = int(stu_amount_str)
    
    for _ in range (stu_amount_int):
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
   
        course_id = get_user_input("WHATS THE COURSE ID")
        
        driver.get(f'https://plataforma-mestres-educacao.vercel.app/lesson/{course_id}')

        time.sleep(1.5)

        play_vid = wait.until(EC.element_to_be_clickable
                            ((By.XPATH, '//*[@id="main-wrapper"]/div[2]/div/section/div[2]/article'))).click()
        
        time.sleep(2)
        
        next()
        
        # Text
        next()
        
        # Image
        next()
        pyautogui.press('tab')
        pyautogui.press('enter')
        time.sleep(1.5)
        
        # Audio
        next()
        time.sleep(0.5)
        
        
        # File
        next()
        pyautogui.press('tab')
        pyautogui.press('enter')

        # Code
        next()
        
        # Choice
        choice_inp = get_user_input("1 or 2")
        choice_answ = wait.until(EC.element_to_be_clickable
                            ((By.XPATH, f'//*[@id="main-wrapper"]/div[2]/div/div[2]/div[{choice_inp}]/label/div'))).click()
        
        modal_answ = wait.until(EC.element_to_be_clickable
                            ((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/button'))).click()
        
        next()
        
        # Diss
        text_inp = get_user_input("Text")
        text = wait.until(EC.element_to_be_clickable
                            ((By.XPATH, '//*[@id="main-wrapper"]/div[2]/div/div[2]/textarea'))).send_keys(text_inp)
        
        send = wait.until(EC.element_to_be_clickable
                            ((By.XPATH, '//*[@id="main-wrapper"]/div[2]/div/div[2]/button'))).click()
        
        send_conf = wait.until(EC.element_to_be_clickable
                            ((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/button'))).click()
        
        next()
        
        pyautogui.press('tab')
        pyautogui.press('enter')

        # Ess
        text_inp = get_user_input("Text")
        text = wait.until(EC.element_to_be_clickable
                            ((By.XPATH, '//*[@id="main-wrapper"]/div[2]/div/div[2]/textarea'))).send_keys(text_inp)
        
        send = wait.until(EC.element_to_be_clickable
                            ((By.XPATH, '//*[@id="main-wrapper"]/div[2]/div/div[2]/button'))).click()
        
        send_conf = wait.until(EC.element_to_be_clickable
                            ((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/button'))).click()
        
        next()
        
        third_conf = wait.until(EC.element_to_be_clickable
                            ((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/button'))).click()
        
    driver.quit()        
    
