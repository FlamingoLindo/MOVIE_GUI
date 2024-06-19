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

def create_student_account_func():
    
    # Path to your ChromeDriver
    driver_path = os.path.join(get_base_path(), 'chromedriver.exe')
    s = Service(driver_path)
    driver = webdriver.Chrome(service=s)  

    # Open the web page
    driver.get(os.getenv('STUDENT_URL'))

    # Initialize WebDriverWait
    wait = WebDriverWait(driver, 5)
    time.sleep(2)
    
    amount_str = get_user_input("Amount of accounts to be created")
    amount_int = int(amount_str)
    
    for _ in range(amount_int):
        # Click at the new account button 
        new_account_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/main/div/div/a')))
        new_account_btn.click()

        # Email input
        email = get_user_input("Student's email")
        email_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/main/div/form/div[1]/label/input')))
        email_input.send_keys(email)

        # Full name input
        fullName = get_user_input("Student's full name")
        fullName_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/main/div/form/div[2]/label/input')))
        fullName_input.send_keys(fullName)

        # CPF input
        cpf_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/main/div/form/div[3]/label/input')))
        cpf = gera_e_valida_cpf()
        cpf_input.send_keys(cpf)
        time.sleep(0.2)

        # Phone number input
        phone = get_user_input("Student's phone-number")
        phone_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/main/div/form/div[4]/label/input')))
        phone_input.send_keys(phone)

        # Password input
        password = get_user_input("Student's password")
        password_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/main/div/form/div[5]/label/input')))
        password_input.send_keys(password)

        # Password confirmation input
        passwordConf_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/main/div/form/div[6]/label/input')))
        passwordConf_input.send_keys(password)

        # Clicks the next button
        next_btn = wait.until(EC.element_to_be_clickable
                                        ((By.XPATH, '//*[@id="__next"]/main/main/div/form/button'))).click()
        
        next_page = wait.until(EC.element_to_be_clickable
                                        ((By.XPATH, '//*[@id="__next"]/main/main/div/div[4]/ul/li[4]/a/img'))).click()
        
        # Finds the company button (will be the last one from the first page)
        los_fernandos_btn = wait.until(EC.element_to_be_clickable
                                        ((By.XPATH, '//*[@id="__next"]/main/main/div/div[3]/div[1]/button'))).click()
        
        # Finishes the account
        make_acc_btn = wait.until(EC.element_to_be_clickable
                                        ((By.XPATH, '/html/body/div[1]/main/main/div/div[5]/button'))).click()

        

    # Close the browser
    time.sleep(6)
    driver.quit()
