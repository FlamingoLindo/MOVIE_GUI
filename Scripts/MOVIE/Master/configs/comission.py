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

def affiliate_comission_func():
    # Path to your ChromeDriver
    driver_path = load_chromedriver()
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

    # Open the configurations page
    config_page = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[1]/div[2]/div/div[1]/a')))
    config_page.click()

    time.sleep(1)
    comission = wait.until(EC.element_to_be_clickable
                        ((By.XPATH, '//*[@id="__next"]/main/div[2]/div[3]/div/a[3]')
                            )).click()

    first_payment_input = get_user_input("Comission for the first payment (Y)/(N)?").title()
    if first_payment_input == "Y":
        first_comission_input = get_user_input("How much?                          ")
        first_comission = wait.until(EC.element_to_be_clickable
                        ((By.XPATH, '//*[@id="__next"]/main/div[2]/form/div[1]/div[1]/div[1]/div[2]/input')
                            )).clear()
        
        first_comission = wait.until(EC.element_to_be_clickable
                        ((By.XPATH, '//*[@id="__next"]/main/div[2]/form/div[1]/div[1]/div[1]/div[2]/input')
                            )).send_keys(first_comission_input)
    else:
        disable_first_comission = wait.until(EC.element_to_be_clickable
                        ((By.XPATH, '//*[@id="__next"]/main/div[2]/form/div[1]/div[1]/div[1]/div[1]/label')
                            )).click()

    second_payment_input = get_user_input("Comission for the second payment and beyond (Y)/(N)?").title()
    if second_payment_input == "Y":
        second_comission_input = get_user_input("How much?                          ")
        second_comission = wait.until(EC.element_to_be_clickable
                        ((By.XPATH, '//*[@id="__next"]/main/div[2]/form/div[1]/div[2]/div/div[2]/input')
                            )).send_keys(second_comission_input)

        active_input = get_user_input("Affiliate will get paid only when active (Y)/(N)?").title()
        if active_input == "Y":
            only_active = wait.until(EC.element_to_be_clickable
                            ((By.XPATH, '//*[@id="__next"]/main/div[2]/form/label')
                                )).click()
        else:
            pass
        
        comission_duration = get_user_input("Ilimitado ou Limitado")
        if comission_duration == "Ilimitado":
            ilimited = wait.until(EC.element_to_be_clickable
                            ((By.XPATH, '//*[@id="__next"]/main/div[2]/form/div[2]/div/label[1]/div')
                                )).click()
        else:
            limited = wait.until(EC.element_to_be_clickable
                            ((By.XPATH, '//*[@id="__next"]/main/div[2]/form/div[2]/div/label[2]/div')
                                )).click()
            months_input = get_user_input("How many months?")
            months = wait.until(EC.element_to_be_clickable
                            ((By.XPATH, '/html/body/div[1]/main/div[2]/form/div[2]/div/div/div/label/div/input')
                                )).send_keys(months_input)
            
        auto_input = get_user_input("Automatic payment (Y)/(N)?").title()
        if active_input == "N":
            only_active = wait.until(EC.element_to_be_clickable
                            ((By.XPATH, '//*[@id="__next"]/main/div[2]/form/div[2]/label[2]')
                                )).click()
        else:
            pass
        
        save = wait.until(EC.element_to_be_clickable
                            ((By.XPATH, '//*[@id="__next"]/main/div[2]/form/button')
                                )).click()
        
    else:
        disable_second_comission = wait.until(EC.element_to_be_clickable
                        ((By.XPATH, '//*[@id="__next"]/main/div[2]/form/div[1]/div[2]/div/div[1]/label')
                            )).click()
        
        active_input = get_user_input("Affiliate will get paid only when active (Y)/(N)?").title()
        if active_input == "Y":
            only_active = wait.until(EC.element_to_be_clickable
                            ((By.XPATH, '//*[@id="__next"]/main/div[2]/form/label')
                                )).click()
        else:
            pass
        
        auto_input = get_user_input("Automatic payment (Y)/(N)?").title()
        if active_input == "N":
            only_active = wait.until(EC.element_to_be_clickable
                            ((By.XPATH, '//*[@id="__next"]/main/div[2]/form/div[2]/label[2]')
                                )).click()
        else:
            pass
        
        save = wait.until(EC.element_to_be_clickable
                            ((By.XPATH, '//*[@id="__next"]/main/div[2]/form/button')
                                )).click()
        
        save2 = wait.until(EC.element_to_be_clickable
                            ((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/div/button[2]')
                                )).click()
        
    time.sleep(2)
    driver.quit()