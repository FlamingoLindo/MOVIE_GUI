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

def landing_page_func():
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

    def text_command():
        pyautogui.keyDown('ctrl')
        pyautogui.press('a')
        pyautogui.keyUp('ctrl')
        pyautogui.press('backspace')
    
    landing_page = wait.until(EC.element_to_be_clickable
                        ((By.XPATH, '//*[@id="__next"]/main/div[2]/div[2]/div/a[4]')
                            )).click()

    landing_amount_str = get_user_input("How many landing pages?  ")
    landing_amount_int = int(landing_amount_str)
    for _ in range(landing_amount_int):
        new_landing = wait.until(EC.element_to_be_clickable
                        ((By.XPATH, '//*[@id="__next"]/main/div[2]/section/div/button')
                            )).click()
        
        text1_inp = get_user_input("Text 1")
        text1 = wait.until(EC.element_to_be_clickable
                        ((By.XPATH, '//*[@id="__next"]/main/div/div[1]/div[1]/div[1]/div[1]/div/div/div/h1')
                            )).click()
        text_command()
        pyautogui.write(text1_inp)
        
        img1_path = get_user_input("Image 1 path")
        img1 = wait.until(EC.element_to_be_clickable
                        ((By.XPATH, '//*[@id="__next"]/main/div/div[1]/div[1]/div[1]')
                            )).click()
        change_img1 = wait.until(EC.element_to_be_clickable
                        ((By.XPATH, '//*[@id="__next"]/main/div/div[1]/div[1]/div[1]/div[2]/label')
                            )).click()
        time.sleep(1.5)
        pyautogui.write(img1_path)
        pyautogui.press('enter')
        
        title1_inp = get_user_input("Title 1")
        title1 = wait.until(EC.element_to_be_clickable
                        ((By.XPATH, '//*[@id="__next"]/main/div/div[1]/div[2]/div[1]/div[2]/div[1]/div/div/h1')
                            )).click()
        text_command()
        pyautogui.write(title1_inp)
        
        text2_inp = get_user_input("Text 2")
        text2 = wait.until(EC.element_to_be_clickable
                        ((By.XPATH, '//*[@id="__next"]/main/div/div[1]/div[2]/div[1]/div[2]/div[2]/div/div/p')
                            )).click()
        text_command()
        pyautogui.write(text2_inp)
        
        img2_path = get_user_input("Image 2 path")
        img2 = wait.until(EC.element_to_be_clickable
                        ((By.XPATH, '//*[@id="__next"]/main/div/div[1]/div[2]/div[1]/div[1]')
                            )).click()
        change_img2 = wait.until(EC.element_to_be_clickable
                        ((By.XPATH, '//*[@id="__next"]/main/div/div[1]/div[2]/div[1]/div[1]/div/label')
                            )).click()
        time.sleep(1.5)
        pyautogui.write(img2_path)
        pyautogui.press('enter')
        
        
        title2_inp = get_user_input("Title 2")
        title2 = wait.until(EC.element_to_be_clickable
                        ((By.XPATH, '//*[@id="__next"]/main/div/div[1]/div[3]/div[1]/div[2]/div[1]/div/div/h1')
                            )).click()
        text_command()
        pyautogui.write(title2_inp)
        
        text3_inp = get_user_input("Text 3")
        text3 = wait.until(EC.element_to_be_clickable
                        ((By.XPATH, '//*[@id="__next"]/main/div/div[1]/div[3]/div[1]/div[2]/div[2]/div/div/p')
                            )).click()
        text_command()
        pyautogui.write(text3_inp)
        
        img3_path = get_user_input("Image 3 path")
        img3= wait.until(EC.element_to_be_clickable
                        ((By.XPATH, '//*[@id="__next"]/main/div/div[1]/div[3]/div[1]/div[1]/img')
                            )).click()
        change_img3 = wait.until(EC.element_to_be_clickable
                        ((By.XPATH, '//*[@id="__next"]/main/div/div[1]/div[3]/div[1]/div[1]/div/label')
                            )).click()
        time.sleep(1.5)
        pyautogui.write(img3_path)
        pyautogui.press('enter')
        
        title3_inp = get_user_input("Title 3")
        title3 = wait.until(EC.element_to_be_clickable
                        ((By.XPATH, '//*[@id="__next"]/main/div/div[1]/div[4]/section/header/div[1]/div/div/div/h1')
                            )).click()
        text_command()
        pyautogui.write(title3_inp)
        
        text4_inp = get_user_input("Text 4")
        text4 = wait.until(EC.element_to_be_clickable
                        ((By.XPATH, '//*[@id="__next"]/main/div/div[1]/div[4]/section/header/div[2]/div/div/div/p')
                            )).click()
        text_command()
        pyautogui.write(text4_inp)
        
        img3_path = get_user_input("Image 3 path")
        img3= wait.until(EC.element_to_be_clickable
                        ((By.XPATH, '//*[@id="__next"]/main/div/div[1]/div[5]/section/ul/li[1]/div/div[1]/div[1]/img')
                            )).click()
        change_img3 = wait.until(EC.element_to_be_clickable
                        ((By.XPATH, '//*[@id="__next"]/main/div/div[1]/div[5]/section/ul/li[1]/div/div[1]/div[1]/div/label')
                            )).click()
        time.sleep(1.5)
        pyautogui.write(img3_path)
        pyautogui.press('enter')
        
        title4_inp = get_user_input("Title 4")
        title4 = wait.until(EC.element_to_be_clickable
                        ((By.XPATH, '//*[@id="__next"]/main/div/div[1]/div[5]/section/ul/li[1]/div/div[1]/div[2]/div/div/h2')
                            )).click()
        text_command()
        pyautogui.write(title4_inp)
        
        text5_inp = get_user_input("Text 5")
        text5 = wait.until(EC.element_to_be_clickable
                        ((By.XPATH, '//*[@id="__next"]/main/div/div[1]/div[5]/section/ul/li[1]/div/div[1]/div[3]/div/div/p')
                            )).click()
        text_command()
        pyautogui.write(text5_inp)
        
        img4_path = get_user_input("Image 4 path")
        img4= wait.until(EC.element_to_be_clickable
                        ((By.XPATH, '//*[@id="__next"]/main/div/div[1]/div[5]/section/ul/li[2]/div/div[1]/div[1]/img')
                            )).click()
        change_img4 = wait.until(EC.element_to_be_clickable
                        ((By.XPATH, '//*[@id="__next"]/main/div/div[1]/div[5]/section/ul/li[2]/div/div[1]/div[1]/div/label')
                            )).click()
        time.sleep(1.5)
        pyautogui.write(img4_path)
        pyautogui.press('enter')
        
        title5_inp = get_user_input("Title 5")
        title5 = wait.until(EC.element_to_be_clickable
                        ((By.XPATH, '//*[@id="__next"]/main/div/div[1]/div[5]/section/ul/li[2]/div/div[1]/div[2]/div/div/h2')
                            )).click()
        text_command()
        pyautogui.write(title5_inp)
        
        text6_inp = get_user_input("Text 6")
        text6 = wait.until(EC.element_to_be_clickable
                        ((By.XPATH, '//*[@id="__next"]/main/div/div[1]/div[5]/section/ul/li[2]/div/div[1]/div[3]/div/div/p')
                            )).click()
        text_command()
        pyautogui.write(text6_inp)
        
        img5_path = get_user_input("Image 5 path")
        img5= wait.until(EC.element_to_be_clickable
                        ((By.XPATH, '//*[@id="__next"]/main/div/div[1]/div[5]/section/ul/li[3]/div/div[1]/div[1]/img')
                            )).click()
        change_img5 = wait.until(EC.element_to_be_clickable
                        ((By.XPATH, '//*[@id="__next"]/main/div/div[1]/div[5]/section/ul/li[3]/div/div[1]/div[1]/div/label')
                            )).click()
        time.sleep(1.5)
        pyautogui.write(img5_path)
        pyautogui.press('enter')
        
        title6_inp = get_user_input("Title 6")
        title6 = wait.until(EC.element_to_be_clickable
                        ((By.XPATH, '//*[@id="__next"]/main/div/div[1]/div[5]/section/ul/li[3]/div/div[1]/div[2]/div/div/h2')
                            )).click()
        text_command()
        pyautogui.write(title6_inp)
        
        text7_inp = get_user_input("Text 7")
        text7 = wait.until(EC.element_to_be_clickable
                        ((By.XPATH, '//*[@id="__next"]/main/div/div[1]/div[5]/section/ul/li[3]/div/div[1]/div[3]/div/div/p')
                            )).click()
        text_command()
        pyautogui.write(text7_inp)
        
        end = wait.until(EC.element_to_be_clickable
                        ((By.XPATH, '//*[@id="__next"]/main/div/header/div[2]/button[2]')
                            )).click()
        
        en2 = wait.until(EC.element_to_be_clickable
                        ((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/div/button[2]')
                            )).click()
        
        driver.get('https://plataforma-mestres-educacao-empresa.vercel.app/configuracoes/venda/landing-pages')
        
    time.sleep(2)
    driver.quit()