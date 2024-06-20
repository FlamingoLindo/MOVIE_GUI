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

def create_affiliate_account_func():
    # Create a CPF (it might not be valid sometimes)
    def gera_cpf():
        cpf = [random.randint(0, 9) for _ in range(9)]
        soma1 = sum(x * y for x, y in zip(cpf, range(10, 1, -1)))
        digito1 = (soma1 * 10 % 11) % 10
        cpf.append(digito1)
        
        soma2 = sum(x * y for x, y in zip(cpf, range(11, 1, -1)))
        digito2 = (soma2 * 10 % 11) % 10
        cpf.append(digito2)
        
        cpf_formatado = ''.join(map(str, cpf))
        return cpf_formatado[:3] + '.' + cpf_formatado[3:6] + '.' + cpf_formatado[6:9] + '-' + cpf_formatado[9:]

    def valida_cpf(cpf):
        cpf_numeros = [int(char) for char in cpf if char.isdigit()]
        
        if len(cpf_numeros) != 11:
            return False
        
        # Validar primeiro dígito
        soma1 = sum(x * y for x, y in zip(cpf_numeros[:9], range(10, 1, -1)))
        digito1 = (soma1 * 10 % 11) % 10
        if cpf_numeros[9] != digito1:
            return False
        
        # Validar segundo dígito
        soma2 = sum(x * y for x, y in zip(cpf_numeros[:10], range(11, 1, -1)))
        digito2 = (soma2 * 10 % 11) % 10
        if cpf_numeros[10] != digito2:
            return False
        
        return True

    def gera_e_valida_cpf():
        while True:
            cpf = gera_cpf()
            if valida_cpf(cpf):
                return cpf

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
    login = get_user_input("Company's login")
    email_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/main/form/div[2]/div[1]/label/input')))
    email_input.send_keys(login)

    # Wait for password input to be clickable
    password = get_user_input("Company's password")
    password_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/main/form/div[2]/div[2]/label/input')))
    password_input.send_keys(password)
    pyautogui.press('enter')

    # Clicks at the login button
    login_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/main/form/div[2]/button')))
    login_btn.click()

    time.sleep(2)

    # Goes to user management page
    user_management = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[1]/div[2]/ul/li[4]/a')))
    user_management.click()

    aff = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[2]/div/a[3]/div[1]')))
    aff.click()

    new_aff = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/section/div[2]/div[2]/div[1]/a')))
    new_aff.click()

    email = get_user_input("Affiliate's email address")
    email_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/form/div/div[1]/div[2]/label/div/input')))
    email_input.send_keys(email)
    time.sleep(0.2)
    cpf_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/form/div/div[2]/div/label/div/input')))
    cpf = gera_e_valida_cpf()
    cpf_input.send_keys(cpf)
    time.sleep(0.2)
    password = get_user_input("Affiliate's password")
    password_conf = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/form/div/div[3]/div[2]/label/div/input')))
    password_conf.send_keys(password)
    time.sleep(0.2)
    password_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/form/div/div[3]/div[1]/label/div/input')))
    password_input.send_keys(password)
    time.sleep(0.2)
    fullName = get_user_input("Affiliate's full name")
    name_input = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/main/div[2]/form/div/div[1]/div[1]/label/div/input')))
    name_input.send_keys(fullName)

    pyautogui.press('enter')

    time.sleep(6)

    # Close the browser
    driver.quit()
