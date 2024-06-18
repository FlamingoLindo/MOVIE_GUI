import pandas as pd
import pyautogui
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import random
import time
from dotenv import load_dotenv
import os
load_dotenv()

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

def create_affiliate_request_func():
    # Load the Excel file
    df = pd.read_excel(r'C:\Users\josef\Desktop\AfterLifeDeath\UMC\Scripts\MOVIE\Affiliate\Files\create_affiliates.xlsx')
    print(df)

    # Path to your ChromeDriver
    driver_path = './chromedriver.exe'
    s = Service(driver_path)
    driver = webdriver.Chrome(service=s)  

    # Open the web page
    driver.get('https://afiliado-mestreseducacao.vercel.app/')

    # Initialize WebDriverWait
    wait = WebDriverWait(driver, 5)
    time.sleep(2)

    for index, row in df.iterrows():

        # Show what index its currently inputing (Just for debuging)
        print(index)

        # Clicks at the register link on the login page
        register_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/main/form/div[4]/a')))
        register_btn.click()

        # Inputs name
        name_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/main/div[2]/div[2]/div[1]/form/div[1]/label/input')))
        name_input.send_keys(row['username'])
        
        # Inputs email
        email_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/main/div[2]/div[2]/div[1]/form/div[2]/label/input')))
        email_input.send_keys(row['email'])

        # Inputs the cpf (may not work sometimes)
        cpf_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/main/div[2]/div[2]/div[1]/form/div[3]/label/input')))
        cpf = gera_e_valida_cpf()
        cpf_input.send_keys(cpf)
        time.sleep(0.2)

        # Inputs password
        password_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/main/div[2]/div[2]/div[1]/form/div[4]/label/input')))
        password_input.send_keys(row['password'])

        # Inputs password confirmation
        password_conf_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/main/div[2]/div[2]/div[1]/form/div[5]/label/input')))
        password_conf_input.send_keys(row['passwordConfirmation'])

        # Register
        register_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/main/div[2]/div[2]/div[1]/form/button')))
        register_btn.click()

        # About me 
        about_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/main/div[2]/div[2]/div[2]/form/div[1]/label/textarea')))
        about_input.send_keys("ABOUT ME =)")

        # Link 1
        link1 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/main/div[2]/div[2]/div[2]/form/div[2]/div/label/input')))
        link1.send_keys("https://afiliado-mestreseducacao.vercel.app/register")

        # Link 2
        link2 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/main/div[2]/div[2]/div[2]/form/div[3]/div/label/input')))
        link2.send_keys("https://afiliado-mestreseducacao.vercel.app/register")

        # Next 
        next = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/main/div[2]/div[2]/div[2]/form/button')))
        next.click()

        time.sleep(2)

        # Next page
        next_page = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/main/div[2]/div[2]/div[3]/form/div[1]/div[2]/ul/li[7]/a/img')))
        next_page.click()
 
        # Find instituision
        instituision = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/main/div[2]/div[2]/div[3]/form/div[1]/div[1]/label[1]')))
        instituision.click()

        # Create account 
        create_account2 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/main/div[2]/div[2]/div[3]/form/button')))
        create_account2.click()
        
        time.sleep(6)

        # Open profile manager
        driver.get("https://afiliado-mestreseducacao.vercel.app/")

    # Clicks at the register button
    pyautogui.press('enter')

    # IF YOU WANT TO MAKE AN EXTERNAL ACCOUNT JUST COMMENT THE LINES 82 AND 83

    # Selects "INTERNAL" option
    internal_opt = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/main/form/div/div[1]/div/label[2]/div')))
    internal_opt.click()

    create_account = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/main/form/div/button')))
    create_account.click()

    time.sleep(6)

    # Close the browser
    driver.quit()
