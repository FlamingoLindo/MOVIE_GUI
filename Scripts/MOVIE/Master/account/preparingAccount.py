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

def preparig_master_account_func():
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

    # Inputs the email
    email = get_user_input("Company's email")
    email_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/main/form/div[2]/div[1]/label/input')))
    email_input.send_keys(email)

    # Inputs the password
    password = get_user_input("Company's password")
    passoword_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/main/form/div[2]/div[2]/label/input')))
    passoword_input.send_keys(password)

    # Clicks at the login button
    login_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/main/form/div[2]/button')))
    login_btn.click()

    time.sleep(2)

    # Open profile manager
    driver.get("https://plataforma-mestres-educacao-empresa.vercel.app/perfil/informacoes-gerais")

    # Address configuration
    address = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/nav/a[4]')))
    address.click()
    open_address = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[2]/div/a')))
    open_address.click()

    cep = get_user_input("Company's CEP(only numbers)")
    cep_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/form/div/div[1]/label/div/input')))
    cep_input.send_keys(cep)

    number_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/form/div/div[5]/label/div/input')))
    number_input.send_keys(1)
    time.sleep(1.5)
    submit = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/form/button')))
    submit.click()
    done = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/button')))
    done.click()

    # Open payment configuration
    payment_conf =  wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/nav/a[3]')))
    payment_conf.click()

    add_card = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[2]/div/div[1]/a')))
    add_card.click()
    add_again = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div/a/div')))
    add_again.click()

    name = get_user_input("Company's credict card name")
    name_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/form/div/div[1]/label/div/input')))
    name_input.send_keys(name)

    expiration = get_user_input("Company's credict card expiration date (only numbers)")
    expiration_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/form/div/div[2]/div[1]/label/div/input')))
    expiration_input.send_keys(expiration)

    cvv = get_user_input("Company's credict card expiration CVV (only numbers)")
    cvv_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/form/div/div[2]/div[2]/label/div/input')))
    cvv_input.send_keys(cvv)

    card_num = get_user_input("Company's credict card number (only numbers)")
    card_num_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/form/div/div[3]/label/div/input')))
    card_num_input.send_keys(card_num)

    cpf_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/form/div/div[4]/label/div/input')))
    cpf = gera_e_valida_cpf()
    cpf_input.send_keys(cpf)
    time.sleep(0.2)

    add_card = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/form/button')))
    add_card.click()

    time.sleep(3)

    done = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/button')))
    done.click()

    # Open plan manager
    driver.get("https://plataforma-mestres-educacao-empresa.vercel.app/meu-plano/planos?plan=")

    # See plans
    see_plans = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div/div/div/div/a')))
    see_plans.click()

    # Clicks at a plan 
    plan = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[2]/div[1]')))
    plan.click()

    time.sleep(2)

    contract_plan = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/button')))
    contract_plan.click()

    buy_now = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/div/button')))
    buy_now.click()

    confirm = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/div[2]/button[2]')))
    confirm.click()

    time.sleep(6)

    # Close the browser
    driver.quit()
