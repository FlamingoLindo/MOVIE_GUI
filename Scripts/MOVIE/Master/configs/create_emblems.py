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

def create_emblem_func():
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

    achivements_page = wait.until(EC.element_to_be_clickable
                       ((By.XPATH, '//*[@id="__next"]/main/div[2]/div[5]/div[2]/a[1]')
                        )).click()

    pencil = 1
    while pencil <= 7:
        time.sleep(1)
        open_emblem = wait.until(EC.element_to_be_clickable
                        ((By.XPATH, f'//*[@id="__next"]/main/div[2]/div[3]/ul/li[{pencil}]/div/a/img')
                            )).click()
        time.sleep(1)
        one = wait.until(EC.element_to_be_clickable
                        ((By.XPATH, '//*[@id="__next"]/main/div[2]/div[4]/div[1]/div[2]/ul/li[2]/button/div/img')
                            )).click()
        time.sleep(1)
        next = wait.until(EC.element_to_be_clickable
                        ((By.XPATH, '//*[@id="__next"]/main/div[2]/footer/button')
                            )).click()
        time.sleep(1)
        two = wait.until(EC.element_to_be_clickable
                        ((By.XPATH, '//*[@id="__next"]/main/div[2]/div[4]/div[1]/div[2]/ul/li[2]/button/div/img')
                            )).click()
        time.sleep(1)
        next2 = wait.until(EC.element_to_be_clickable
                        ((By.XPATH, '//*[@id="__next"]/main/div[2]/footer/button[2]')
                            )).click()
        time.sleep(1)
        name_input = get_user_input("Emblem name      ")
        name = wait.until(EC.element_to_be_clickable
                        ((By.XPATH, '//*[@id="__next"]/main/div[2]/div[4]/div[1]/div[2]/div/label/div/input')
                            ))
        name.clear()
        name.send_keys(name_input)
        time.sleep(1)
        next3 = wait.until(EC.element_to_be_clickable
                        ((By.XPATH, '//*[@id="__next"]/main/div[2]/footer/button[2]')
                            )).click()
        time.sleep(1)
        pencil += 1
        driver.get('https://plataforma-mestres-educacao-empresa.vercel.app/configuracoes/gamificacao/conquistas')
        
        
    time.sleep(2)
    driver.quit()