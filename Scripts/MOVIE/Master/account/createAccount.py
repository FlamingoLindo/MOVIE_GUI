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

def create_account_master_func():
    
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
    driver_path = os.path.join(get_base_path(), 'chromedriver.exe')
    s = Service(driver_path)
    driver = webdriver.Chrome(service=s)  

    # Open the web page
    driver.get(os.getenv('MOVIE_URL'))

    # Initialize WebDriverWait
    wait = WebDriverWait(driver, 5)
    time.sleep(2)

    # Clicks at the register link on the login page
    register_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/main/form/div[4]/a')))
    register_btn.click()

    # Inputs the name 
    fullName = get_user_input("Company's full name")
    name_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/main/form/div[2]/div[1]/label/input')))
    name_input.send_keys(fullName)
    time.sleep(0.2)

    # Inputs the phone number
    phoneNumber = get_user_input("Master's phone-number (only numbers)")
    phone_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/main/form/div[2]/div[3]/label/input')))
    phone_input.send_keys(phoneNumber)
    time.sleep(0.2)

    # Inputs the cpf (may not work sometimes)
    cpf_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/main/form/div[2]/div[4]/label/input')))
    cpf = gera_e_valida_cpf()
    cpf_input.send_keys(cpf)
    time.sleep(0.2)

    # Inputs the password
    password = get_user_input("Company's password")
    passoword_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/main/form/div[2]/div[5]/label/input')))
    passoword_input.send_keys(password)
    time.sleep(0.2)

    # Inputs the password confirmation
    passowordConf_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/main/form/div[2]/div[6]/label/input')))
    passowordConf_input.send_keys(password)

    time.sleep(0.2)
    # Inputs the email
    email = get_user_input("Company's email")
    email_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/main/form/div[2]/div[2]/label/input')))
    email_input.send_keys(email)

    # Clicks at the register button
    pyautogui.press('enter')

    # IF YOU WANT TO MAKE AN EXTERNAL ACCOUNT JUST COMMENT THE LINES 82 AND 83

    # Selects "INTERNAL" option
    #internal_opt = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/main/form/div/div[1]/div/label[2]/div')))
    #internal_opt.click()

    create_account = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/main/form/div/button')))
    create_account.click()

    time.sleep(6)

    # Close the browser
    driver.quit()
