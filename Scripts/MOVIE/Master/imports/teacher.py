import pandas as pd
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

def import_teacher_list_func():
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

    # Load the Excel file
    df = pd.read_excel(r'C:\Users\josef\Desktop\AfterLifeDeath\UMC\Scripts\MOVIE\Master\imports\Files\import_teachers.xlsx')
    print(df)

    # Path to your ChromeDriver
    driver_path = './chromedriver.exe'
    s = Service(driver_path)
    driver = webdriver.Chrome(service=s)  

    # Open the web page
    driver.get(os.getenv("MOVIE_URL"))

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

    # Goes user control page
    hidrant_btn = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#__next > main > div.sc-ae760ff-2.dvaOJQ > div.sc-ae760ff-4.gQKZVq > ul > li:nth-child(4) > a')))
    hidrant_btn.click()

    # Opens the register a student page 
    register_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[2]/div/a[2]')))
    register_btn.click()


    for index, row in df.iterrows():

        # Show what index its currently inputing (Just for debuging)
        print(index)

        # Redirects to the register a student page for the loop
        driver.get("https://plataforma-mestres-educacao-empresa.vercel.app/controle-de-usuario/professor-coordenador/criar")
        
        # Inputs email
        email_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/form/div/div[1]/div[2]/label/div/input')))
        email_input.send_keys(row['email'])
        
        # Inputs random CPF (Might not be valid)
        cpf_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/form/div/div[2]/div/label/div/input')))
        cpf = gera_e_valida_cpf()
        cpf_input.send_keys(cpf)

        # Inputs password
        password_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/form/div/div[3]/div[1]/label/div/input')))
        password_input.send_keys(row['password'])

        # Inputs password confirmation
        passwordConfirmation_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/form/div/div[3]/div[2]/label/div/input')))
        passwordConfirmation_input.send_keys(row['passwordConfirmation'])

        # Inputs the student name (Has to be last, because for some reason it erases if its in any other position)
        name_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/form/div/div[1]/div[1]/label/div/input')))
        name_input.send_keys(row['username'])

        #Finishes the register
        finish_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/form/button')))
        finish_btn.click()

    # Close the browser
    driver.quit()
