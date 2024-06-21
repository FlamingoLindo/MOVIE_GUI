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
from selenium.common.exceptions import TimeoutException

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

def create_item_func():
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

    prize = wait.until(EC.element_to_be_clickable
                       ((By.XPATH, '//*[@id="__next"]/main/div[2]/div[5]/div[2]/a[2]')
                        )).click()

    items_amount_str = get_user_input("How many items?")
    items_amount_int = int(items_amount_str)
    for _ in range(items_amount_int):
        
        try:
            first = wait.until(EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="__next"]/main/div[2]/div[3]/a')
                )).click()
        except TimeoutException:
            second = wait.until(EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="__next"]/main/div[2]/section/div/a')
                )).click()
            
        type = get_user_input("Interno or Externo?").capitalize()
        print(type)
        if type == "Interno":
            click = wait.until(EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="__next"]/main/div[2]/form/div[1]/div[1]/div/label[1]/div')
                )).click()
            item_type = get_user_input("Avatar, Banner, Item").capitalize()
            dropdown = wait.until(EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="__next"]/main/div[2]/form/div[1]/div[2]/label/div/div')
                )).click()
            dropdown_select = wait.until(EC.element_to_be_clickable(
                (By.XPATH, f"//div[contains(text(), '{item_type}')]")
                )).click()
            
            name_input = get_user_input("Item name     ")
            name = wait.until(EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="__next"]/main/div[2]/form/div[2]/label/div/input')
                )).send_keys(name_input)
            
            price_input = get_user_input("Item price  ")
            price = wait.until(EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="__next"]/main/div[2]/form/div[3]/div[1]/div/label/div/input')
                )).send_keys(price_input)
            
            image_path = get_user_input("Image path")
            pyautogui.press('tab')
            pyautogui.press('enter')
            time.sleep(1)
            pyautogui.write(image_path)
            pyautogui.press('enter')
            
            rules_input = get_user_input("Item rule")
            rules = wait.until(EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="__next"]/main/div[2]/form/div[5]/label/textarea')
                )).send_keys(rules_input)
            
            done = wait.until(EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="__next"]/main/div[2]/form/footer/button')
                )).click() 
            
            time.sleep(1.3)
            driver.get('https://plataforma-mestres-educacao-empresa.vercel.app/configuracoes/gamificacao/loja-de-premios')
        elif type == "Externo":
            click = wait.until(EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="__next"]/main/div[2]/form/div[1]/div[1]/div/label[2]/div')
                )).click()
            dropdown = wait.until(EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="__next"]/main/div[2]/form/div[1]/div[2]/label/div/div')
                )).click()
            dropdown_select = wait.until(EC.element_to_be_clickable(
                (By.XPATH, f"//div[contains(text(), 'Voucher')]")
                )).click()
            
            name_input = get_user_input("Item name     ")
            name = wait.until(EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="__next"]/main/div[2]/form/div[2]/label/div/input')
                )).send_keys(name_input)
            
            price_input = get_user_input("Item price  ")
            price = wait.until(EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="__next"]/main/div[2]/form/div[3]/div[1]/div/label/div/input')
                )).send_keys(price_input)
            
            image_path = get_user_input("Image path")
            pyautogui.press('tab')
            pyautogui.press('enter')
            time.sleep(1)
            pyautogui.write(image_path)
            pyautogui.press('enter')
            
            code_input = get_user_input("Item code")
            code = wait.until(EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="__next"]/main/div[2]/form/div[4]/label/div/input')
                )).send_keys(code_input) 
            
            rules_input = get_user_input("Item rule")
            rules = wait.until(EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="__next"]/main/div[2]/form/div[5]/label/textarea')
                )).send_keys(rules_input)
            
            done = wait.until(EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="__next"]/main/div[2]/form/footer/button')
                )).click() 
            
            time.sleep(1)
            driver.get('https://plataforma-mestres-educacao-empresa.vercel.app/configuracoes/gamificacao/loja-de-premios')
        
    time.sleep(2)
    driver.quit()