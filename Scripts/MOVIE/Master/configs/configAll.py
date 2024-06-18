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




def config_master_func():
    
    def go_back():
        go_back = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[1]/header/button')))
        go_back.click()
        
    # Sets the midia path
    midia_img = r'C:\Users\josef\Desktop\AfterLifeDeath\MovieCreator\autoMovie\banner.jpg'

    # Path to your ChromeDriver
    driver_path = './chromedriver.exe'
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

    """# Sales method
    sales_method = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[2]/div/a[1]/div[1]')))
    sales_method.click()

    activate_sales_method = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/form/div/div[2]/div/label')))
    activate_sales_method.click()

    # Single payment
    single_payment_opt = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/form/div/div[3]/div/div[1]/div[1]/label/div')))
    single_payment_opt.click()

    acess_period = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/form/div/div[4]/div/label/div/div')))
    acess_period.click()
    acess_period_option = wait.until(EC.element_to_be_clickable((By.XPATH, f"//div[contains(text(), '12 meses')]")))
    acess_period_option.click()

    #Motnhly payment (Uncomment this code below if you want the monthly option and comment the lines 46,47,49,50,51 and 52)
    #monthly_payment_opt = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/form/div/div[3]/div/div[1]/div[2]/label/div')))
    #monthly_payment_opt.click()


    # Adds the cost 
    pyautogui.press("1")

    # Save payment method
    save_payment = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/form/div/button')))
    save_payment.click()

    go_back()"""

    # Open the signature plan
    signature_plan_page = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[2]/div/a[2]/div[1]')))
    signature_plan_page.click()

    new_plan = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[2]/a')))
    new_plan.click()

    plan_name = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/form[1]/div[1]/div[1]/label/div/input')))
    plan_name.send_keys("THE PLAN")

    plan_value = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/form[1]/div[1]/div[2]/label/div/input')))
    plan_value.send_keys(9999)

    plan_desc = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/form[1]/div[2]/label/textarea')))
    plan_desc.send_keys("Plan description")

    plan_tag = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/form[2]/div/label/div/input')))
    plan_tag.send_keys("Plan tag")
    pyautogui.press('enter')

    plan_frequency = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/form[3]/div[1]/div[1]/label/div/div')))
    plan_frequency.click()
    plan_frequency_option = wait.until(EC.element_to_be_clickable((By.XPATH, f"//div[contains(text(), 'Mensal')]")))
    plan_frequency_option.click()

    # Automatic renew (IF YOU WANT IT TO NO AUTOMATILY RENEW THEN JUST COMMENT THE LINES 98 AND 99)
    auto_renew = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/form[3]/div[1]/div[2]/label[1]/div')))
    auto_renew.click()

    # Allow installments (IF YOU DONT WANT IT TO HAVE INSTALLMENTS THEN JUST COMMENT THE LINES 102, 103, 104 AND 105)
    allow_inst = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/form[3]/div[1]/div[3]/label')))
    allow_inst.click()
    inst_value = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/form[3]/div[1]/div[3]/div/label/input')))
    inst_value.send_keys(9)

    # Allow disccount (COMMENT 108, 109, 110 AND 111)
    allow_disc = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/form[3]/div[2]/div/label[2]/div')))
    allow_disc.click()
    disc_value = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/form[3]/div[2]/div/div/div/label/input')))
    disc_value.send_keys(90)

    # 15 free days (YAP)
    free_days = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/form[3]/div[3]/label')))
    free_days.click()

    save_payment_method = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/form[3]/button')))
    save_payment_method.click()
    confirm_payment = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/div/button[2]')))
    confirm_payment.click()
    time.sleep(1)
    back_payment = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/button')))
    back_payment.click()

    time.sleep(1)

    go_back()

    # Course category
    category_page = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[2]/div/a[3]/div[1]')))
    category_page.click()

    new_catg = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/button')))
    new_catg.click()

    catg_name_input = get_user_input("Category name")
    catg_name = wait.until(EC.element_to_be_clickable
                           ((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/form/div[1]/label/div/input'))).send_keys(catg_name_input)
    

    # Active category (COMMENT 137 and 138)
    active_catg = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/form/div[2]/div/label')))
    active_catg.click()

    create_catg = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/form/div[3]/button[2]')))
    create_catg.click()

    view_catg = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/button')))
    view_catg.click()

    go_back()

    # Landing page
    landing_page = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[2]/div/a[4]/div[1]')))
    landing_page.click()

    new_landing = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/section/div/button')))
    new_landing.click()

    landing_text = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/div[1]/div[1]/div[1]/div[1]/div/div/div/h1')))
    landing_text.click()
    pyautogui.keyDown('ctrl')
    pyautogui.press('a')
    pyautogui.keyUp('ctrl')
    pyautogui.press('backspace')
    lading_input = get_user_input("Landing Page Text")
    pyautogui.write(lading_input)

    end_landing = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/header/div[2]/button[2]')))
    end_landing.click()

    save_landing = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/div/button[2]')))
    save_landing.click()

    ok_page = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/button')))
    ok_page.click()

    go_back()

    # Payment methods
    #payment_method_page = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[3]/div/a[1]/div[1]')))
    #payment_method_page.click()

    # go_back()

    # Coupon
    coupon_page = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[3]/div/a[2]/div[1]')))
    coupon_page.click()

    new_coupon = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[3]/div/div/a')))
    new_coupon.click()

    coupon_code = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/form/div[1]/div[1]/label/div/input')))
    coupon_code.send_keys("COUPON1")

    coupon_percent = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/form/div[1]/div[2]/label/div/input')))
    coupon_percent.send_keys(90)

    add_expiring_date = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/form/div[2]/label[1]/div')))
    add_expiring_date.click()
    add_date = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/form/div[3]/div/label/div/input')))
    add_date.send_keys("10052026")

    add_coupon = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/form/button')))
    add_coupon.click()
    coupon_list = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/button')))
    coupon_list.click()

    go_back()

    # Affiliete comission (DONT KNOW IF THERES ANYTHING THAT I SHOULD CHANGE OVER HERE)

    # Defaulters suspension (SAME THING HERE LULE)

    # Classes
    clases_page = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[4]/div/a[1]/div[1]')))
    clases_page.click()
    add_class = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/section/div[2]/div/a')))
    add_class.click()

    class_name_input = get_user_input("Class Name")
    class_name = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/form/div[1]/div/label/div/input')))
    class_name.send_keys(class_name_input)

    period_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/form/div[1]/label/div/div')))
    period_dropdown.click()
    period_option = wait.until(EC.element_to_be_clickable((By.XPATH, f"//div[contains(text(), 'Matutino')]")))
    period_option.click()

    save_class = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/form/button')))
    save_class.click()
    classes_list = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/button')))
    classes_list.click()

    go_back()

    # Midia kit
    kit_midia_page = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[4]/div/a[3]/div[1]')))
    kit_midia_page.click()

    open_kit = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/section/div[2]/div[2]/div/button')))
    open_kit.click()

    midia_title = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/form/div[1]/div[1]/label/div/input')))
    midia_title.send_keys("KITMIDIA!")

    pyautogui.press('tab')
    time.sleep(1)
    pyautogui.press('enter')

    time.sleep(1.5)

    pyautogui.write(midia_img)
    time.sleep(1.3)
    pyautogui.press('enter')

    ok_midia = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/form/div[2]/button[2]')))
    ok_midia.click()

    time.sleep(6)

    go_back()

    # Aproval rule (DONT WHAT TO CHANGE HERE)

    # Achiviements
    achiviements_page = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[5]/div[2]/a[1]/div[1]')))
    achiviements_page.click()

    achv_edit1 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[3]/ul/li[1]/div/a/img')))
    achv_edit1.click()
    time.sleep(1)
    pick_emblem = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[4]/div[1]/div[2]/ul/li[2]/button')))
    pick_emblem.click()
    time.sleep(1)                                                            
    emblem_next_step = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/footer/button')))
    emblem_next_step.click()
    time.sleep(1)
    emblem_icon = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[4]/div[1]/div[2]/ul/li[2]/button/div/img')))
    emblem_icon.click()

    emblem_next_step = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/footer/button[2]')))
    emblem_next_step.click()
    
    emblem_name_input = get_user_input("Emblem name")
    
    emblem_name = wait.until(EC.element_to_be_clickable
                             ((By.XPATH, '//*[@id="__next"]/main/div[2]/div[4]/div[1]/div[2]/div/label/div/input'))).send_keys(emblem_name_input)
    

    emblem_save = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/footer/button[2]')))
    emblem_save.click()

    view_emblems = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/button')))
    view_emblems.click()

    go_back()

    # Item store
    store_page = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[5]/div[2]/a[2]/div[1]')))
    store_page.click()

    add_prise = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[3]/a')))
    add_prise.click()

    internal_prise = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/form/div[1]/div[1]/div/label[1]/div')))
    internal_prise.click()

    prise_type = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/form/div[1]/div[2]/label/div/div')))
    prise_type.click()
    prise_type_option = wait.until(EC.element_to_be_clickable((By.XPATH, f"//div[contains(text(), 'Avatar')]")))
    prise_type_option.click()

    prise_name = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/form/div[2]/label/div/input')))
    prise_name.send_keys("Yeah")

    prise_price = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/form/div[3]/div[1]/div/label/div/input')))
    prise_price.send_keys(9999)

    wait = WebDriverWait(driver, 10)  
    file_input = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/main/div[2]/form/div[3]/div[2]/label/input')))
    file_path = midia_img
    file_input.send_keys(file_path)

    prise_rules = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/form/div[5]/label/textarea')))
    prise_rules.send_keys('Use it wisely!')

    add_prise = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/form/footer/button')))
    add_prise.click()

    time.sleep(3)

    go_back()

    time.sleep(6)
    # Close the browser
    driver.quit()