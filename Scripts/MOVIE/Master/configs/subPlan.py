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

def subscription_plan_func():
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

    # Sales subscription button
    subscription_plan = wait.until(EC.element_to_be_clickable
                        ((By.XPATH, '//*[@id="__next"]/main/div[2]/div[2]/div/a[2]'))).click()

    new_plan = wait.until(EC.element_to_be_clickable
                        ((By.XPATH, '//*[@id="__next"]/main/div[2]/div[2]/a'))).click()

    plan_amount_str = get_user_input("How many plans?  ")
    plan_amount_int = int(plan_amount_str)
    for _ in range(plan_amount_int):
        name = get_user_input("Plan name               ")
        plan_name = wait.until(EC.element_to_be_clickable
                            ((By.XPATH, '//*[@id="__next"]/main/div[2]/form[1]/div[1]/div[1]/label/div/input')
                                )).send_keys(name)

        value = get_user_input("Plan value               ")
        plan_value = wait.until(EC.element_to_be_clickable
                            ((By.XPATH, '//*[@id="__next"]/main/div[2]/form[1]/div[1]/div[2]/label/div/input')
                                )).send_keys(value)

        desc = get_user_input("Plan description        ")
        plan_desc = wait.until(EC.element_to_be_clickable
                            ((By.XPATH, '//*[@id="__next"]/main/div[2]/form[1]/div[2]/label/textarea')
                                )).send_keys(desc)

        diff_amount_str = get_user_input("How many differentials")
        diff_amount_int = int(diff_amount_str)
        for _ in range(diff_amount_int):
            diff = get_user_input("Plan differential      ")
            plan_differentials = wait.until(EC.element_to_be_clickable
                                ((By.XPATH, '//*[@id="__next"]/main/div[2]/form[2]/div/label/div/input')
                                    )).send_keys(diff)
            send_diff = wait.until(EC.element_to_be_clickable
                                ((By.XPATH, '//*[@id="__next"]/main/div[2]/form[2]/div/label/div/div/button')
                                    )).click()

        frequency_input = get_user_input("Mensal, Bimestral, Trimestral, Semestral, Anual")
        frequency = wait.until(EC.element_to_be_clickable
                                ((By.XPATH, '//*[@id="__next"]/main/div[2]/form[3]/div[1]/div[1]/label/div/div')
                                    )).click()
        frequency_select = wait.until(EC.element_to_be_clickable
                                ((By.XPATH, f"//div[contains(text(), '{frequency_input}')]")
                                    )).click()

        renew_input = get_user_input("Automatic (Y)/(N)?").title()
        if renew_input == "Y":
            yes = wait.until(EC.element_to_be_clickable
                                ((By.XPATH, '//*[@id="__next"]/main/div[2]/form[3]/div[1]/div[2]/label[1]/div')
                                    )).click()
        else:
            pass 

        allow_insatallemnts = get_user_input("Allow installments (Y)/(N)?").title()
        if allow_insatallemnts == "Y":
            allow_installment = wait.until(EC.element_to_be_clickable
                                ((By.XPATH, '//*[@id="__next"]/main/div[2]/form[3]/div[1]/div[3]/label')
                                    )).click()
            installments_value = get_user_input("How many installments?")
            installments = wait.until(EC.element_to_be_clickable
                                ((By.XPATH, '//*[@id="__next"]/main/div[2]/form[3]/div[1]/div[3]/div/label/input')
                                    )).send_keys(installments_value)
        else:
            pass

        allow_discount = get_user_input("Allow discount (Y)/(N)?").title()
        if allow_discount == "Y":
            allow_dicount = wait.until(EC.element_to_be_clickable
                                ((By.XPATH, '//*[@id="__next"]/main/div[2]/form[3]/div[2]/div/label[2]/div')
                                    )).click()
            discount_value = get_user_input("Discount value?")
            discount = wait.until(EC.element_to_be_clickable
                                ((By.XPATH, '//*[@id="__next"]/main/div[2]/form[3]/div[2]/div/div/div/label/input')
                                    )).send_keys(discount_value)
        else:
            pass

        allow_free_trail = get_user_input("Allow free trail (Y)/(N)?").title()
        if allow_free_trail == "Y":
            free = wait.until(EC.element_to_be_clickable
                                    ((By.XPATH, '//*[@id="__next"]/main/div[2]/form[3]/div[3]/label/label')
                                        )).click()
        else:
            pass

        save = wait.until(EC.element_to_be_clickable
                                    ((By.XPATH, '//*[@id="__next"]/main/div[2]/form[3]/button')
                                        )).click()

        save_2 = wait.until(EC.element_to_be_clickable
                                    ((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/div/button[2]')
                                        )).click()

        time.sleep(2)

        driver.get('https://plataforma-mestres-educacao-empresa.vercel.app/configuracoes/venda/plano-de-assinatura/criar')

    driver.quit()
    