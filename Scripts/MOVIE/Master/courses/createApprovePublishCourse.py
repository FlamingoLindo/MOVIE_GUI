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

def create_app_pub_func():
    # Path to your ChromeDriver
    driver_path = './chromedriver.exe'
    s = Service(driver_path)
    driver = webdriver.Chrome(service=s)  

    # Sets the banner image
    banner_img = r'C:\Users\josef\Desktop\AfterLifeDeath\MovieCreator\autoMovie\banner.jpg'

    # Sets the audio path
    audio_path = 'https://i.supa.codes/znSGl'

    # Sets the document path
    document_path = 'https://i.supa.codes/jdy5b'

    # Open the web page
    driver.get(os.getenv('MOVIE_URL'))

    # Class for adding a class
    def add_class():
        class_click = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/a/img')))
        class_click.click()

    # Class for doing the finals setps athe concluding the class creation
    def finish_class():
        points = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[2]/section/footer/label/input')))
        points.send_keys(10)

        done_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/header/button/img')))
        done_btn.click()

        confirm = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/button')))
        confirm.click()

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

    # Course creation
    course_page = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[1]/div[2]/ul/li[2]/a')))
    course_page.click()
    create_couse = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[3]/section/div[2]')))
    create_couse.click()

    # Course name
    name = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[2]/div[2]/div/form[1]/div/label/div/input')))
    name.send_keys("Teaching teachers how to teach")

    # Description
    description = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[2]/div[2]/div/form[1]/label/div/label/textarea')))
    description.send_keys("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam eget ligula eu lectus lobortis condimentum. Aliquam nonummy auctor massa. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Nulla at risus. Quisque purus magna, auctor et, sagittis ac, posuere eu, lectus. Nam mattis, felis ut adipiscing")

    # Inputs course category
    course_category = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mainForm"]/div/label[2]/div/div')))
    course_category.click()
    time.sleep(0.5)
    course_category_option = wait.until(EC.element_to_be_clickable((By.XPATH, f"//div[contains(text(), 'Novos')]")))
    course_category_option.click()

    # Tags 
    tags = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[2]/div[2]/div/form[2]/div/label/div/input')))
    tags.send_keys("Lorem ipsum dolor sit amet")
    tags_send = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[2]/div[2]/div/form[2]/div/label/div/div/button')))
    tags_send.click()

    # Total time
    total_time = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mainForm"]/div/div/div/label/div/input')))
    total_time.clear()
    total_time.send_keys("69")

    # Add banner
    for _ in range(22):
        pyautogui.press('tab')
    pyautogui.press('enter')
    time.sleep(1.5)
    pyautogui.write(banner_img)
    time.sleep(1)
    pyautogui.press('enter')
    
    

    for _ in range(8):
        pyautogui.press('tab')
    pyautogui.press('enter')

    time.sleep(1)

    # Module name
    mod_name = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[2]/div[2]/div/form[1]/div/label/div/input')))
    mod_name.send_keys("Module number one (1)")
    pyautogui.press('enter')

    # Select the professor
    course_professor = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[2]/div[2]/div/form[2]/label[1]/div/div')))
    course_professor.click()
    course_professor_option = wait.until(EC.element_to_be_clickable((By.XPATH, f"//div[contains(text(), 'Funcionário Novo 1')]")))
    course_professor_option.click()
    pyautogui.press('enter')

    # Adds video class
    add_class()

    class_name = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[1]/div[2]/label/div/input')))
    class_name.send_keys("Video")

    class_desc = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[1]/div[3]/label/div/label/textarea')))
    class_desc.send_keys("Description")

    video_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[3]/div[2]/button[1]/div')))
    video_btn.click()

    video_url = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[2]/section/div/div/div/div[2]/input')))
    video_url.send_keys("https://youtu.be/dQw4w9WgXcQ")

    video_search = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[2]/section/div/div/div/div[2]/div/button[2]')))
    video_search.click()

    finish_class()

    # Adds text class
    add_class()

    class_name = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[1]/div[2]/label/div/input')))
    class_name.send_keys("Text")

    class_desc = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[1]/div[3]/label/div/label/textarea')))
    class_desc.send_keys("Description")

    text_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[3]/div[2]/button[2]/div')))
    text_btn.click()

    text = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[2]/section/div/div/div/div[2]/label/textarea')))
    text.send_keys("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam eget ligula eu lectus lobortis condimentum. Aliquam nonummy auctor massa. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Nulla at risus. Quisque purus magna, auctor et, sagittis ac, posuere eu, lectus. Nam mattis, felis ut adipiscing")

    finish_class()

    # Adds image class
    add_class()

    class_name = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[1]/div[2]/label/div/input')))
    class_name.send_keys("Image")

    class_desc = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[1]/div[3]/label/div/label/textarea')))
    class_desc.send_keys("Description")

    image_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[3]/div[2]/button[3]/div')))
    image_btn.click()

    image_search = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[2]/section/div/div/div/div[2]/input')))
    image_search.send_keys("https://i.supa.codes/znSGl")

    image_done = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[2]/section/div/div/div/div[2]/div/button[2]')))
    image_done.click()

    finish_class()


    # Adds audio class
    add_class()

    class_name = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[1]/div[2]/label/div/input')))
    class_name.send_keys("Audio")

    class_desc = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[1]/div[3]/label/div/label/textarea')))
    class_desc.send_keys("Description")

    audio_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[3]/div[2]/button[4]/div')))
    audio_btn.click()

    audio_search = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[2]/section/div/div/div/div[2]/input')))
    audio_search.send_keys(audio_path)
    audio_done = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[2]/section/div/div/div/div[2]/div/button[2]')))
    audio_done.click()

    finish_class()

    # Adds document class
    add_class()

    class_name = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[1]/div[2]/label/div/input')))
    class_name.send_keys("Document")

    class_desc = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[1]/div[3]/label/div/label/textarea')))
    class_desc.send_keys("Description")

    document_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[3]/div[2]/button[5]/div')))
    document_btn.click()

    document_search = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[2]/section/div/div/div/div[2]/input')))
    document_search.send_keys(document_path)
    document_done = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[2]/section/div/div/div/div[2]/div/button[2]')))
    document_done.click()

    finish_class()

    # Adds code class (Its a really janky, since for some reason selenium does not want to find the code space and type on it)
    add_class()

    class_name = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[1]/div[2]/label/div/input')))
    class_name.send_keys("Code")

    class_desc = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[1]/div[3]/label/div/label/textarea')))
    class_desc.send_keys("Description")

    code_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[3]/div[2]/button[6]/div')))
    code_btn.click()

    janky_solution = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[2]/section/div/div/div/div[1]/label/div/input')))
    janky_solution.click()
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.hotkey('shift', '1')

    finish_class()

    # Adds choices class
    add_class()

    class_name = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[1]/div[2]/label/div/input')))
    class_name.send_keys("Choices")

    class_desc = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[1]/div[3]/label/div/label/textarea')))
    class_desc.send_keys("Description")

    choices_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[3]/div[2]/button[7]/div')))
    choices_btn.click()

    multiple_choices_class_question = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[2]/section/div/div/div/div[1]/label/div/input')))
    multiple_choices_class_question.send_keys("Choices")
    alternative1 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[2]/section/div/div/div/button')))
    alternative1.click()
    alternative2 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[2]/section/div/div/div/button')))
    alternative2.click()
    is_right = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[2]/section/div/div/div/div[2]/ul/li[1]/div[2]/label[1]/div')))
    is_right.click()
    alt_txt1 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[2]/section/div/div/div/div[2]/ul/li[1]/input')))
    alt_txt1.click()
    alt_txt1.send_keys("Right")
    alt_txt2 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[2]/section/div/div/div/div[2]/ul/li[2]/input')))
    alt_txt2.click()
    alt_txt2.send_keys("Wrong")

    finish_class()

    # Adds dissertative class
    add_class()

    class_name = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[1]/div[2]/label/div/input')))
    class_name.send_keys("Dissertative")

    class_desc = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[1]/div[3]/label/div/label/textarea')))
    class_desc.send_keys("Description")

    dessertative_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[3]/div[2]/button[8]/div')))
    dessertative_btn.click()

    text_field = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[2]/section/div/div/div/div[2]/label/textarea')))
    text_field.send_keys('Lorem ipsum dolor sit amet')

    finish_class()


    # Adds essay class
    add_class()

    class_name = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[1]/div[2]/label/div/input')))
    class_name.send_keys("Essay")

    class_desc = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[1]/div[3]/label/div/label/textarea')))
    class_desc.send_keys("Description")

    essay_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[3]/div[2]/button[9]/div')))
    essay_btn.click()

    text_field = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[2]/section/div/div/div/div[1]/label/div/input')))
    text_field.send_keys('Lorem ipsum dolor sit amet')

    finish_class()

    # Finishes course creation
    finish_course = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/header/button')))
    finish_course.click()

    time.sleep(6)

    # Open course
    open_course = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[3]/section/div[1]/table/tbody/tr[1]/td[8]/div/a')))
    open_course.click()

    # Opens the tests page 
    test_page = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[2]/div[1]/nav/a[3]')))
    test_page.click()

    # Opens the test creation page
    test_creation = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/section/div[2]/div/a/div')))
    test_creation.click()

    # Test name
    test_name = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[1]/div[2]/label/div/input')))
    test_name.send_keys("Test")

    # Test module
    test_module = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[1]/label/div/div')))
    test_module.click()
    test_module_drop = wait.until(EC.element_to_be_clickable((By.XPATH, f"//div[contains(text(), 'Module number one (1)')]")))
    test_module_drop.click()

    # Add test attempts
    attempts = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[1]/div[3]/div/div/div/label/div/input')))
    attempts.send_keys("5")

    # Add test questions
    choices_test = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[4]/button[7]/div')))
    choices_test.click()
    value = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[2]/div/input')))
    value.send_keys(1)
    choices_test_title = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[2]/section/div/div/div/div[1]/label/div/input')))
    choices_test_title.send_keys("Choices Test")
    add_choices = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[2]/section/div/div/div/button')))
    add_choices.click()
    add_choices.click()
    right = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[2]/section/div/div/div/div[2]/ul/li[1]/input')))
    right.send_keys("Right")
    wrong = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[2]/section/div/div/div/div[2]/ul/li[2]/input')))
    wrong.send_keys("Wrong")
    is_right = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[2]/section/div/div/div/div[2]/ul/li[1]/div[2]/label[1]/div')))
    is_right.click()

    dissertative_test = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[4]/button[8]/div')))
    dissertative_test.click()
    value2 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[2]/div[2]/input')))
    value2.send_keys(1)
    dissertative_test_question = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[2]/section[2]/div/div/div/div[2]/label/textarea')))
    dissertative_test_question.send_keys('Lorem ipsum dolor sit amet, consectetur adipiscing elit.')

    essay_test = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[4]/button[9]/div')))
    essay_test.click()
    value3 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[2]/div[3]/input')))
    value3.send_keys(1)
    essay_test_question = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[2]/section[3]/div/div/div/div[1]/label/div/input')))
    essay_test_question.send_keys('Lorem ipsum dolor sit amet, consectetur adipiscing elit.')

    # Finish test creation
    finish_test = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/header/button/img')))
    finish_test.click()

    save = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/div/button[2]')))
    save.click()

    list = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/button')))
    list.click()

    time.sleep(5)

    # Course creation
    course_page = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[1]/div[2]/ul/li[2]/a')))
    course_page.click()

    # Open course
    open_course = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[3]/section/div[1]/table/tbody/tr[1]/td[8]/div/a')))
    open_course.click()

    # Open course dependencies
    dependencies = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[3]/a')))
    dependencies.click()

    # Aprove classes
    for i in range(1, 10):
        approve = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/ul/div/ul/li[1]/div/div/div/button[1]')))
        approve.click()
        time.sleep(1)
        sure = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/div/button[2]')))
        sure.click()
        ok = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/button')))
        ok.click()
        time.sleep(1)

    time.sleep(2)

    # Goes tests approval page and approves it all
    test_approval = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/nav/a[2]')))
    test_approval.click()
    time.sleep(1)
    approve_test = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/ul/div/ul/li/div/div/div/button[1]')))
    approve_test.click()
    time.sleep(1)
    accept = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/div/button[2]')))
    accept.click()
    time.sleep(1)
    list = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/button')))
    list.click() 

    # Publishes the course
    go_back = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[1]/header/button')))
    go_back.click()
    go_back2 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[1]/div[1]/header/button')))
    go_back2.click()
    time.sleep(0.5)
    publish = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[3]/section/div[1]/table/tbody/tr[1]/td[8]/div/button[1]')))
    publish.click()
    time.sleep(1)
    # For free
    free = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-root"]/div[2]/div/form/div/button')))
    free.click()
    save_free = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/div/button[2]')))
    save_free.click()

    time.sleep(6)

    # Close the browser
    driver.quit()
