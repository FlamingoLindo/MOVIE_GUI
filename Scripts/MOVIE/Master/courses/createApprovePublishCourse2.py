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

def create_app_pub_input_func():
    # Path to your ChromeDriver
    driver_path = load_chromedriver()
    s = Service(driver_path)
    driver = webdriver.Chrome(service=s)  

    # Open the web page
    driver.get(os.getenv('MOVIE_URL'))

    # Class for adding a class
    def add_class():
        class_click = wait.until(EC.element_to_be_clickable
                                 ((By.XPATH, '//*[@id="__next"]/main/div[2]/a/img'))).click()
        
    def pick_module():
        if mod_amount_int == 1:
            pass
        else:
            module_input = get_user_input("Choose the module (1,2,3,..)")
            
            module_dropdown = wait.until(EC.element_to_be_clickable
                                    ((By.XPATH, '//*[@id="__next"]/main/div[2]/div[2]/div/label/div/div'))).click()
            
            module_select = wait.until(EC.element_to_be_clickable
                                    ((By.XPATH, f"//label/div/div[2]/div/div[{module_input}]"))).click()

    # Class for doing the finals setps athe concluding the class creation
    def finish_class():
        points = wait.until(EC.element_to_be_clickable
                            ((By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[2]/section/footer/label/input'))).send_keys(10)

        done_btn = wait.until(EC.element_to_be_clickable
                              ((By.XPATH, '//*[@id="__next"]/main/div[2]/header/button/img'))).click()

        confirm = wait.until(EC.element_to_be_clickable
                             ((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/button'))).click()

    # Initialize WebDriverWait
    wait = WebDriverWait(driver, 5)
    time.sleep(2)

    # Wait for email input to be clickable
    email = get_user_input("Company's email")
    email_input = wait.until(EC.element_to_be_clickable
                             ((By.XPATH, '//*[@id="__next"]/main/div/main/form/div[2]/div[1]/label/input'))).send_keys(email)

    # Wait for password input to be clickable
    password = get_user_input("Company's password")
    password_input = wait.until(EC.element_to_be_clickable
                                ((By.XPATH, '//*[@id="__next"]/main/div/main/form/div[2]/div[2]/label/input'))).send_keys(password)
    pyautogui.press('enter')

    time.sleep(3)

    # Course creation
    course_page = wait.until(EC.element_to_be_clickable
                             ((By.XPATH, '//*[@id="__next"]/main/div[1]/div[2]/ul/li[2]/a'))).click()

    repeat_amount_str = get_user_input("HOW MANY COURSES?")
    repeat_amount_int = int(repeat_amount_str)
    for _ in range(repeat_amount_int):
        create_couse = wait.until(EC.element_to_be_clickable
                                ((By.XPATH, '//*[@id="__next"]/main/div[2]/div[3]/section/div[2]'))).click()

        # Total time
        courseTime = get_user_input("Course total time (only numbers): ")
        total_time = wait.until(EC.element_to_be_clickable
                                ((By.XPATH, '//*[@id="mainForm"]/div/div/div/label/div/input')))
        total_time.clear()
        total_time.send_keys(courseTime)

        

        # Description
        courseDescription = get_user_input("Course description: ")
        description = wait.until(EC.element_to_be_clickable
                                ((By.XPATH, '//*[@id="__next"]/main/div[2]/div[2]/div[2]/div/form[1]/label/div/label/textarea'))).send_keys(courseDescription)
        
        # Inputs course category
        courseCategory = get_user_input("Course category (Mais Vistos, Melhores Avaliados, Top de Vendas, Novos): ")
        course_category = wait.until(EC.element_to_be_clickable
                                    ((By.XPATH, '//*[@id="mainForm"]/div/label[2]/div/div'))).click()
        time.sleep(0.5)
        course_category_option = wait.until(EC.element_to_be_clickable
                                            ((By.XPATH, f"//div[contains(text(), '{courseCategory}')]"))).click()

        # Tags 
        tag_amount_str = get_user_input("How many tags?")
        tag_amount_int = int(tag_amount_str)
        
        for _ in range (tag_amount_int):
            courseTag = get_user_input("Course tag: ")
            tags = wait.until(EC.element_to_be_clickable
                            ((By.XPATH, '//*[@id="__next"]/main/div[2]/div[2]/div[2]/div/form[2]/div/label/div/input')
                             )).send_keys(courseTag)
            tags_send = wait.until(EC.element_to_be_clickable
                                ((By.XPATH, '//*[@id="__next"]/main/div[2]/div[2]/div[2]/div/form[2]/div/label/div/div/button')
                                 )).click()

        time.sleep(1.2)

        # Add banner
        banner_input = wait.until(EC.element_to_be_clickable
                            ((By.XPATH, '//*[@id="mainForm"]/div/label[1]'))).click()
    
        time.sleep(1)
        
        banner_img = get_user_input("BANNER IMAGE PATH")
        pyautogui.write(banner_img)
        time.sleep(1)
        pyautogui.press('enter')
        
        # Course name
        courseName = get_user_input("Course name: ")
        name = wait.until(EC.element_to_be_clickable
                        ((By.XPATH, '//*[@id="__next"]/main/div[2]/div[2]/div[2]/div/form[1]/div/label/div/input')))
        name.send_keys(courseName)
        pyautogui.press('enter')
        
        # Module name
        mod_amount_str = get_user_input("How many modules would you like?")
        mod_amount_int = int(mod_amount_str)
        for _ in range(mod_amount_int):
            modName = get_user_input("Course module name: ")
            mod_name = wait.until(EC.element_to_be_clickable
                                ((By.XPATH, '//*[@id="__next"]/main/div[2]/div[2]/div[2]/div/form[1]/div/label/div/input'))).send_keys(modName)

            pyautogui.press('tab')
            pyautogui.press('enter')

        # Select the professor
        course_professor = wait.until(EC.element_to_be_clickable
                                    ((By.XPATH, '//*[@id="__next"]/main/div[2]/div[2]/div[2]/div/form[2]/label[1]/div/div'))).click()
        time.sleep(0.6)
        course_professor_option = wait.until(EC.element_to_be_clickable
                                            ((By.XPATH, "//div[@id='react-select-3-listbox']/div/div"))).click()
        nextPage_btn = wait.until(EC.element_to_be_clickable
                                ((By.XPATH, '//*[@id="__next"]/main/div[2]/div[2]/div[2]/form/button'))).click()


        
        pick_module()
        
        
        # Adds video class
        add_class()
        videoName = get_user_input("Video class name: ")
        class_name = wait.until(EC.element_to_be_clickable
                                ((By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[1]/div[2]/label/div/input'))).send_keys(videoName)

        videoDesc = get_user_input("Video class description: ")
        class_desc = wait.until(EC.element_to_be_clickable
                                ((By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[1]/div[3]/label/div/label/textarea'))).send_keys(videoDesc)
        
        video_amount_str = get_user_input("How many videos")
        video_amount_int = int(video_amount_str)
        video = 1
        for _ in range (video_amount_int):
            video_btn = wait.until(EC.element_to_be_clickable
                                ((By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[3]/div[2]/button[1]/div'))).click()

            videoURL = get_user_input("Video URL: ")
            video_url = wait.until(EC.element_to_be_clickable
                                ((By.XPATH, f'//*[@id="__next"]/main/div[2]/div/div[2]/section[{video}]/div/div/div/div[2]/input')
                                 )).send_keys(videoURL)
            
            video_search = wait.until(EC.element_to_be_clickable
                                    ((By.XPATH, f'//*[@id="__next"]/main/div[2]/div/div[2]/section[{video}]/div/div/div/div[2]/div/button[2]')
                                     )).click()
            video += 1
            
        finish_class()

        pick_module()

        
        # Adds text class
        add_class()

        textName = get_user_input("Text class name: ")
        class_name = wait.until(EC.element_to_be_clickable
                                ((By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[1]/div[2]/label/div/input'))).send_keys(textName)

        textDesc = get_user_input("Text class description: ")
        class_desc = wait.until(EC.element_to_be_clickable
                                ((By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[1]/div[3]/label/div/label/textarea'))).send_keys(textDesc)

        text_amount_str = get_user_input("How many text blocks")
        text_amount_int = int(text_amount_str)
        text_ = 1
        for _ in range (text_amount_int):
            text_btn = wait.until(EC.element_to_be_clickable
                                ((By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[3]/div[2]/button[2]/div'))).click()

            textText = get_user_input("Text class text: ")
            text = wait.until(EC.element_to_be_clickable
                            ((By.XPATH, f'//*[@id="__next"]/main/div[2]/div/div[2]/section[{text_}]/div/div/div/div[2]/label/textarea')
                             )).send_keys(textText)
            text_ += 1

        finish_class()

        pick_module()

        # Adds image class
        add_class()
        imageName = get_user_input("Image class name: ")
        class_name = wait.until(EC.element_to_be_clickable
                                ((By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[1]/div[2]/label/div/input')
                                )).send_keys(imageName)

        imgaeDesc = get_user_input("Image class description: ")
        class_desc = wait.until(EC.element_to_be_clickable
                                ((By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[1]/div[3]/label/div/label/textarea')
                                )).send_keys(imgaeDesc)

        image_amount_str = get_user_input("How many images")
        image_amount_int = int(image_amount_str)
        image = 1
        for _ in range (image_amount_int):
            image_btn = wait.until(EC.element_to_be_clickable
                                ((By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[3]/div[2]/button[3]/div'))).click()

            imageURL = get_user_input("Image URL: ")
            image_search = wait.until(EC.element_to_be_clickable
                                    ((By.XPATH, f'//*[@id="__next"]/main/div[2]/div/div[2]/section[{image}]/div/div/div/div[2]/input')
                                    )).send_keys(imageURL)

            image_done = wait.until(EC.element_to_be_clickable
                                    ((By.XPATH, f'//*[@id="__next"]/main/div[2]/div/div[2]/section[{image}]/div/div/div/div[2]/div/button[2]')
                                    )).click()
            image += 1

        finish_class()

        pick_module()

        
        # Adds audio class
        add_class()

        audioName = get_user_input("Audio class name: ")
        class_name = wait.until(EC.element_to_be_clickable
                                ((By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[1]/div[2]/label/div/input')
                                )).send_keys(audioName)
            
        audioDesc = get_user_input("Audio class description: ")
        class_desc = wait.until(EC.element_to_be_clickable
                                ((By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[1]/div[3]/label/div/label/textarea')
                                )).send_keys(audioDesc)
            
        #audio_amount_str = get_user_input("How many audios")
        #audio_amount_int = int(audio_amount_str)
        audio_num = 1
        #for _ in range (audio_amount_int):    
        audio_btn = wait.until(EC.element_to_be_clickable
                               ((By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[3]/div[2]/button[4]/div'))).click()

        audio_path = get_user_input("Audio path: ")
        audio_search = wait.until(EC.element_to_be_clickable
                                ((By.XPATH, f'//*[@id="__next"]/main/div[2]/div/div[2]/section/div/div/div/div[1]/label/div/input')
                                )).send_keys(f"Audio {audio_num}")
            
        for _ in range(2):
            pyautogui.press('tab')
        pyautogui.press('enter')
        time.sleep(1.5)
        pyautogui.write(audio_path)
        pyautogui.press('enter')
        time.sleep(1)
        audio_num + 1
        
        finish_class()

        pick_module()

        # Adds file class
        add_class()

        docName = get_user_input("Document class name: ")
        class_name = wait.until(EC.element_to_be_clickable
                                ((By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[1]/div[2]/label/div/input')
                                 )).send_keys(docName)

        docDesc = get_user_input("Document class description: ")
        class_desc = wait.until(EC.element_to_be_clickable
                                ((By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[1]/div[3]/label/div/label/textarea')
                                 )).send_keys(docDesc)
    
        file_amount_str = get_user_input("How many document blocks?")
        file_amount_int = int(file_amount_str)
        file = 1 
        for _ in range (file_amount_int):
            document_btn = wait.until(EC.element_to_be_clickable
                                    ((By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[3]/div[2]/button[5]/div'))).click()

            document_path = get_user_input("File path           ")
            file_click = wait.until(EC.element_to_be_clickable
                                    ((By.XPATH, f'//*[@id="__next"]/main/div[2]/div/div[2]/section[{file}]/div/div/div/div[1]/label/div/input')
                                    )).send_keys("File")
            
            time.sleep(0.5)
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.press('enter')
            time.sleep(1.5)
            pyautogui.write(document_path)
            pyautogui.press('enter')
            time.sleep(2)
            
            file += 1
        
        finish_class()

        pick_module()

        # Adds code class (Its a really janky, since for some reason selenium does not want to find the code space and type on it)
        add_class()

        codeName = get_user_input("Code class name: ")
        class_name = wait.until(EC.element_to_be_clickable
                                ((By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[1]/div[2]/label/div/input'))).send_keys(codeName)
        
        codeDesc = get_user_input("Code class description: ")
        class_desc = wait.until(EC.element_to_be_clickable
                                ((By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[1]/div[3]/label/div/label/textarea'))).send_keys(codeDesc)

        code_amount_str = get_user_input("How many code blocks?")
        code_amount_int = int(code_amount_str)
        code = 1 
        for _ in range (code_amount_int):
            code_btn = wait.until(EC.element_to_be_clickable
                                ((By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[3]/div[2]/button[6]/div'))).click()

            janky_solution = wait.until(EC.element_to_be_clickable
                                        ((By.XPATH, f'//*[@id="__next"]/main/div[2]/div/div[2]/section[{code}]/div/div/div/div[1]/label/div/input')
                                         )).click()

            #get_user_input("Alt Tab now!")
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.press('tab')
            codeText = get_user_input("Code class text: ")
            pyautogui.write(codeText)
            
            code += 1

        finish_class()

        pick_module()

        # Adds choices class
        add_class()

        choicesName = get_user_input("Choices class name: ")
        class_name = wait.until(EC.element_to_be_clickable
                                ((By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[1]/div[2]/label/div/input'))).send_keys(choicesName)

        choisesDesc = get_user_input("Choices class description: ")
        class_desc = wait.until(EC.element_to_be_clickable
                                ((By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[1]/div[3]/label/div/label/textarea'))).send_keys(choisesDesc)

        choices_btn = wait.until(EC.element_to_be_clickable
                                ((By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[3]/div[2]/button[7]/div'))).click()

        multiple_choices_class_question = wait.until(EC.element_to_be_clickable
                                                    ((By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[2]/section/div/div/div/div[1]/label/div/input'))).send_keys(choicesName)

        choice_amount_str = get_user_input("How many choices?")
        choice_amount_int = int(choice_amount_str)
        choice_ = 1
        for _ in range (choice_amount_int):
            alternatives = wait.until(EC.element_to_be_clickable
                                    ((By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[2]/section/div/div/div/button'))).click()

            choice = get_user_input("Choice Text")
            choice_txt = wait.until(EC.element_to_be_clickable
                                ((By.XPATH, f'//*[@id="__next"]/main/div[2]/div/div[2]/section/div/div/div/div[2]/ul/li[{choice_}]/input')
                                 )).send_keys(choice)
            choice_ += 1

        # input the right one?
        right_input = get_user_input("Which choice is correct? (1,2,3,...)")
        is_right = wait.until(EC.element_to_be_clickable
                            ((By.XPATH, f'//*[@id="__next"]/main/div[2]/div/div[2]/section/div/div/div/div[2]/ul/li[{right_input}]/div[2]/label[1]/div')
                             )).click()

        finish_class()

        pick_module()

        # Adds dissertative class
        add_class()

        dissName = get_user_input("Dissertative class name: ")
        class_name = wait.until(EC.element_to_be_clickable
                                ((By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[1]/div[2]/label/div/input')
                                 )).send_keys(dissName)

        dissDesc = get_user_input("Dissertative class description: ")
        class_desc = wait.until(EC.element_to_be_clickable
                                ((By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[1]/div[3]/label/div/label/textarea')
                                 )).send_keys(dissDesc)

        diss_amount_str = get_user_input("How many dissertatives text blocks?")
        diss_amount_int = int(diss_amount_str)
        diss = 1 
        for _ in range (code_amount_int):
            dessertative_btn = wait.until(EC.element_to_be_clickable
                                        ((By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[3]/div[2]/button[8]/div')
                                         )).click()

            dissText = get_user_input("Dissertative text: ")
            text_field = wait.until(EC.element_to_be_clickable
                                    ((By.XPATH, f'//*[@id="__next"]/main/div[2]/div/div[2]/section[{diss}]/div/div/div/div[2]/label/textarea')
                                     )).send_keys(dissText)
            
            diss += 1 
        finish_class()

        pick_module()

        # Adds essay class
        add_class()

        essName = get_user_input("Essay class name: ")
        class_name = wait.until(EC.element_to_be_clickable
                                ((By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[1]/div[2]/label/div/input'))).send_keys(essName)
        
        essDesc = get_user_input("Essay class description: ")
        class_desc = wait.until(EC.element_to_be_clickable
                                ((By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[1]/div[3]/label/div/label/textarea'))).send_keys(essDesc)

        ess_amount_str = get_user_input("How many essays text blocks?")
        ess_amount_int = int(ess_amount_str)
        ess = 1 
        for _ in range (ess_amount_int):
            essay_btn = wait.until(EC.element_to_be_clickable
                                ((By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[3]/div[2]/button[9]/div')
                                 )).click()

            essText = get_user_input("Essay text:")
            text_field = wait.until(EC.element_to_be_clickable
                                    ((By.XPATH, f'//*[@id="__next"]/main/div[2]/div/div[2]/section[{ess}]/div/div/div/div[1]/label/div/input')
                                     )).send_keys(essText)
            
            ess += 1 
            
        finish_class()

        # Finishes course creation
        finish_course = wait.until(EC.element_to_be_clickable
                                ((By.XPATH, '//*[@id="__next"]/main/header/button'))).click()

        time.sleep(6)

        # Open course
        open_course = wait.until(EC.element_to_be_clickable
                                ((By.XPATH, '//*[@id="__next"]/main/div[2]/div[3]/section/div[1]/table/tbody/tr[1]/td[8]/div/a'))).click()

        # Opens the tests page 
        test_page = wait.until(EC.element_to_be_clickable
                            ((By.XPATH, '//*[@id="__next"]/main/div[2]/div[2]/div[1]/nav/a[3]'))).click()

        # Opens the test creation page
        test_creation = wait.until(EC.element_to_be_clickable
                                ((By.XPATH, '//*[@id="__next"]/main/div[2]/section/div[2]/div/a/div'))).click()

        # Test name
        testName = get_user_input("Test name: ")
        test_name = wait.until(EC.element_to_be_clickable
                            ((By.XPATH, '//*[@id="__next"]/main/div[2]/div[1]/div[2]/label/div/input'))).send_keys(testName)

        # Test module
        test_module = wait.until(EC.element_to_be_clickable
                                ((By.XPATH, '//*[@id="__next"]/main/div[2]/div[1]/label/div/div'))).click()

        test_module_drop = wait.until(EC.element_to_be_clickable
                                    ((By.XPATH, "//label/div/div[2]/div/div"))).click()

        # Add test attempts
        testAttemp = get_user_input("Number of attemps for the test (only numbers): ")
        attempts = wait.until(EC.element_to_be_clickable
                            ((By.XPATH, '//*[@id="__next"]/main/div[2]/div[1]/div[3]/div/div/div/label/div/input'))).send_keys(testAttemp)

        # Add video?
        video_choice = get_user_input("Add a video on the test (Y)/(N)?").title()
        if video_choice == "Y":
            video_test_amount_str = get_user_input("How many videos?")
            video_test_amount_int = int(video_test_amount_str)
            banana = 1
            for _ in range(video_test_amount_int):
                video_test = wait.until(EC.element_to_be_clickable
                                    ((By.XPATH, '//*[@id="__next"]/main/div[2]/div[4]/button[1]/div')
                                     )).click()
                
                video_test_url_input = get_user_input("Video url    ")
                video_url = wait.until(EC.element_to_be_clickable
                                    ((By.XPATH, f'//*[@id="__next"]/main/div[2]/div[2]/section[{banana}]/div/div/div/div[2]/input')
                                     )).send_keys(video_test_url_input)
                
                video_search_btn = wait.until(EC.element_to_be_clickable
                                    ((By.XPATH, f'//*[@id="__next"]/main/div[2]/div[2]/section[{banana}]/div/div/div/div[2]/div/button[2]')
                                     )).click()
        else:
            pass
               
        # Add video?
        text_choice = get_user_input("Add text on the test (Y)/(N)?").title()
        banana2 = 1
        if text_choice == "Y":
            text_test_amount_str = get_user_input("How many text blocks?")
            text_test_amount_int = int(text_test_amount_str)
            if text_test_amount_int == 1:
                test_text_btn = wait.until(EC.element_to_be_clickable
                                    ((By.XPATH, '//*[@id="__next"]/main/div[2]/div[4]/button[2]/div')
                                     )).click()
                
                test_text_input = get_user_input("Text")
                test_text = wait.until(EC.element_to_be_clickable
                                    ((By.XPATH, f'//*[@id="__next"]/main/div[2]/div[2]/section/div/div/div/div[2]/label/textarea')
                                     )).send_keys(test_text_input)
                
            else:
                for _ in range(text_test_amount_int):
                    test_text_btn = wait.until(EC.element_to_be_clickable
                                        ((By.XPATH, '//*[@id="__next"]/main/div[2]/div[4]/button[2]/div')
                                        )).click()
                    
                    test_text_input = get_user_input("Text")
                    test_text = wait.until(EC.element_to_be_clickable
                                        ((By.XPATH, f'//*[@id="__next"]/main/div[2]/div[2]/section[{banana2}]/div/div/div/div[2]/label/textarea')
                                        )).send_keys(test_text_input)
                    banana += 1
        else:
            pass
        
        # Add image?
        image_choice = get_user_input("Add image on the test (Y)/(N)?").title()
        banana3 = 1
        if image_choice == "Y":
            image_test_amount_str = get_user_input("How many images?")
            image_test_amount_int = int(image_test_amount_str)
            if image_test_amount_int == 1:
                image_test_btn = wait.until(EC.element_to_be_clickable
                                    ((By.XPATH, '//*[@id="__next"]/main/div[2]/div[4]/button[3]/div')
                                     )).click()
                
                image_test_path = get_user_input("Image url")
                image_test = wait.until(EC.element_to_be_clickable
                                    ((By.XPATH, '//*[@id="__next"]/main/div[2]/div[2]/section/div/div/div/div[2]/input')
                                     )).send_keys(image_test_path)
                
                image_test_search = wait.until(EC.element_to_be_clickable
                                    ((By.XPATH, '//*[@id="__next"]/main/div[2]/div[2]/section/div/div/div/div[2]/div/button[2]')
                                     )).click()
            else:
                for _ in range(image_test_amount_int):
                    image_test_btn = wait.until(EC.element_to_be_clickable
                                        ((By.XPATH, '//*[@id="__next"]/main/div[2]/div[4]/button[3]/div')
                                        )).click()
                    
                    image_test_path = get_user_input("Image url")
                    image_test = wait.until(EC.element_to_be_clickable
                                        ((By.XPATH, f'//*[@id="__next"]/main/div[2]/div[2]/section[{banana3}]/div/div/div/div[2]/input')
                                        )).send_keys(image_test_path)
                    
                    image_test_search = wait.until(EC.element_to_be_clickable
                                        ((By.XPATH, f'//*[@id="__next"]/main/div[2]/div[2]/section[{banana3}]/div/div/div/div[2]/div/button[2]')
                                        )).click()
        else:
            pass
        
        # Add audio?
        audio_choice = get_user_input("Add audio (Y)/(N)?").title()
        banana4 = 1
        if audio_choice == "Y":
            audio_test_str = get_user_input("How many audios?")
            audio_test_int = int(audio_test_str)
            if audio_test_int == 1:
                audio_test_btn = wait.until(EC.element_to_be_clickable
                                    ((By.XPATH, '//*[@id="__next"]/main/div[2]/div[4]/button[4]/div')
                                     )).click()
                
                audio_test_path = get_user_input("Audio path")
                audio_test = wait.until(EC.element_to_be_clickable
                                    ((By.XPATH, '//*[@id="__next"]/main/div[2]/div[2]/section/div/div/div/div[2]/input')
                                     )).send_keys("a")
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('enter')
                time.sleep(1.3)
                pyautogui.write(audio_test_path)
                pyautogui.press('enter')
            else:
                for _ in range(audio_test_int):
                    audio_test_btn = wait.until(EC.element_to_be_clickable
                                        ((By.XPATH, '//*[@id="__next"]/main/div[2]/div[4]/button[4]/div')
                                        )).click()
                    
                    audio_test_path = get_user_input("Audio path")
                    audio_test = wait.until(EC.element_to_be_clickable
                                        ((By.XPATH, f'//*[@id="__next"]/main/div[2]/div[2]/section[{banana4}]/div/div/div/div[2]/input')
                                        )).send_keys("a")
                    pyautogui.press('tab')
                    pyautogui.press('tab')
                    pyautogui.press('tab')
                    pyautogui.press('enter')
                    time.sleep(1.3)
                    pyautogui.write(audio_test_path)
                    pyautogui.press('enter')
                    
                    banana4 += 1
        else:
            pass
                
        # Add file?
        file_choice = get_user_input("Add file (Y)/(N)?").title()
        if file_choice == "Y":
            file_test_amount_str = get_user_input("How many files?")
            file_test_amount_int = int(file_test_amount_str)
            banana5 = 1
            if file_test_amount_int == 1:
                file_test_btn = wait.until(EC.element_to_be_clickable
                                ((By.XPATH, '//*[@id="__next"]/main/div[2]/div[4]/button[5]/div')
                                 )).click()
                
                file_test_path = get_user_input("File path")
                file_test = wait.until(EC.element_to_be_clickable
                                ((By.XPATH, '//*[@id="__next"]/main/div[2]/div[2]/section/div/div/div/div[2]/input')
                                 )).send_keys("a")
                
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('enter')
                time.sleep(1.3)
                pyautogui.write(file_test_path)
                pyautogui.press('enter')
            else:
                for _ in range(file_test_amount_int):
                    file_test_btn = wait.until(EC.element_to_be_clickable
                                    ((By.XPATH, '//*[@id="__next"]/main/div[2]/div[4]/button[5]/div')
                                    )).click()
                    
                    file_test_path = get_user_input("File path")
                    file_test = wait.until(EC.element_to_be_clickable
                                    ((By.XPATH, f'//*[@id="__next"]/main/div[2]/div[2]/section[{banana5}]/div/div/div/div[2]/input')
                                    )).send_keys("a")
                    
                    pyautogui.press('tab')
                    pyautogui.press('tab')
                    pyautogui.press('tab')
                    pyautogui.press('enter')
                    time.sleep(1.3)
                    pyautogui.write(file_test_path)
                    pyautogui.press('enter')
                    
                    banana5 += 1
        else:
            pass
           
        # Add code?
        code_choice = get_user_input("Add code block (Y)/(N)?").title()
        if code_choice == "Y":
            code_test_amount_str = get_user_input("How many code block?")
            code_test_amount_int = int(code_test_amount_str)
            banana6 = 1
            if code_test_amount_int == 1:
                code_test_btn = wait.until(EC.element_to_be_clickable
                                ((By.XPATH, '//*[@id="__next"]/main/div[2]/div[4]/button[6]/div')
                                 )).click()
                
                code_test_title = wait.until(EC.element_to_be_clickable
                                ((By.XPATH, '//*[@id="__next"]/main/div[2]/div[2]/section/div/div/div/div[1]/label/div/input')
                                 )).send_keys('Code')
                
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                
                code_test_input = get_user_input("Code text")
                pyautogui.write(code_test_input)
            else:
                for _ in range(code_test_amount_int):
                    code_test_btn = wait.until(EC.element_to_be_clickable
                                    ((By.XPATH, '//*[@id="__next"]/main/div[2]/div[4]/button[6]/div')
                                    )).click()
                    
                    code_test_title = wait.until(EC.element_to_be_clickable
                                    ((By.XPATH, f'//*[@id="__next"]/main/div[2]/div[2]/section[{banana6}]/div/div/div/div[1]/label/div/input')
                                    )).send_keys(f'Code {banana6}')
                    
                    pyautogui.press('tab')
                    pyautogui.press('tab')
                    pyautogui.press('tab')
                    
                    code_test_input = get_user_input("Code text")
                    pyautogui.write(code_test_input)
                    
                    banana6 += 1
        else:
            pass
                                  
        # Add choices?
        choices_choice = get_user_input("Add chooices question (Y)/(N)?").title()
        banana7 = 1 
        if choices_choice == "Y":
            choices_teste_btn = wait.until(EC.element_to_be_clickable
                                ((By.XPATH, '//*[@id="__next"]/main/div[2]/div[4]/button[7]/div')
                                 )).click()
            
            choices_points = get_user_input("How many points?")
            choices_points_type = wait.until(EC.element_to_be_clickable
                                ((By.XPATH, '//*[@id="__next"]/main/div[2]/div[2]/div/input')
                                 )).click()
            pyautogui.write(choices_points)
            
            choices_title = wait.until(EC.element_to_be_clickable
                                ((By.XPATH, '//*[@id="__next"]/main/div[2]/div[2]/section[2]/div/div/div/div[1]/label/div/input')
                                 )).send_keys("Choices")
            
            choices_amount_str = get_user_input("How many choices")
            choices_amount_int = int(choices_amount_str)
            for _ in range(choices_amount_int):
                add_choice = wait.until(EC.element_to_be_clickable
                                ((By.XPATH, '//*[@id="__next"]/main/div[2]/div[2]/section/div/div/div/button')
                                 )).click() 
                
                choices_title_input = get_user_input("Title")
                choice_title = wait.until(EC.element_to_be_clickable
                                ((By.XPATH, f'//*[@id="__next"]/main/div[2]/div[2]/section/div/div/div/div[2]/ul/li[{banana7}]/input')
                                 )).send_keys(choices_title_input) 
                
                banana7 += 1
            
            right = get_user_input('Which option is correct (1,2,3,...)')     
            right_click = wait.until(EC.element_to_be_clickable
                                ((By.XPATH, f'//*[@id="__next"]/main/div[2]/div[2]/section/div/div/div/div[2]/ul/li[{right}]/div[2]/label[1]/div')
                                )).click()      
        else:
            pass
        
        # Add dissertative?
        dissertative_choice = get_user_input("Add dissertative question (Y)/(N)?").title()
        banana8 = 1 
        if dissertative_choice == "Y":
            diss_test_amount_str = get_user_input("How many dissertative questions?")
            diss_test_amount_int = int(diss_test_amount_str)
            if diss_test_amount_int == 1:
                diss_btn = wait.until(EC.element_to_be_clickable
                                    ((By.XPATH, '//*[@id="__next"]/main/div[2]/div[4]/button[8]/div')
                                    )).click()
                
                diss_point_input = get_user_input("How many points?")
                diss_point = wait.until(EC.element_to_be_clickable
                                    ((By.XPATH, '//*[@id="__next"]/main/div[2]/div[2]/div/input')
                                    )).click()
                pyautogui.write(diss_point_input)
                
                diss_test_text_input = get_user_input("Dissertative text")
                diss_test = wait.until(EC.element_to_be_clickable
                                    ((By.XPATH, '//*[@id="__next"]/main/div[2]/div[2]/section[3]/div/div/div/div[2]/label/textarea')
                                    )).send_keys(diss_test_text_input)
            else:
                for _ in range(diss_test_amount_int):
                    diss_btn = wait.until(EC.element_to_be_clickable
                                        ((By.XPATH, '//*[@id="__next"]/main/div[2]/div[4]/button[8]/div')
                                        )).click()
                    
                    diss_point_input = get_user_input("How many points?")
                    diss_point = wait.until(EC.element_to_be_clickable
                                        ((By.XPATH, f'//*[@id="__next"]/main/div[2]/div[2]/div[{banana8}]/input')
                                        )).click()
                    pyautogui.write(diss_point_input)
                    
                    diss_test_text_input = get_user_input("Dissertative text")
                    diss_test = wait.until(EC.element_to_be_clickable
                                        ((By.XPATH, f'//*[@id="__next"]/main/div[2]/div[2]/section[{banana8}]/div/div/div/div[2]/label/textarea')
                                        )).send_keys(diss_test_text_input)
                    
                    banana8 += 1
        else:
            pass
                
        # Add Essay?
        essay_choice = get_user_input("Add essay (Y)/(N)?").title()
        if essay_choice == "Y":
            essay_test_amount_str = get_user_input("How many essay block?")
            essay_test_amount_int = int(essay_test_amount_str)
            banana9 = 1
            if essay_test_amount_int == 1:
                essa_test_btn = wait.until(EC.element_to_be_clickable
                                    ((By.XPATH, '//*[@id="__next"]/main/div[2]/div[4]/button[9]/div')
                                    )).click()
                
                ess_point_input = get_user_input("How many points?")
                ess_point = wait.until(EC.element_to_be_clickable
                                    ((By.XPATH, '//*[@id="__next"]/main/div[2]/div[2]/div/input')
                                    )).click()
                pyautogui.write(ess_point_input)
                
                ess_test_text_input = get_user_input("Dissertative text")
                ess_test = wait.until(EC.element_to_be_clickable
                                    ((By.XPATH, '//*[@id="__next"]/main/div[2]/div[2]/section/div/div/div/div[1]/label/div/input')
                                    )).send_keys(ess_test_text_input)
            else:   
                for _ in range(essay_test_amount_int):
                    essa_test_btn = wait.until(EC.element_to_be_clickable
                                        ((By.XPATH, '//*[@id="__next"]/main/div[2]/div[4]/button[9]/div')
                                        )).click()
                    
                    ess_point_input = get_user_input("How many points?")
                    ess_point = wait.until(EC.element_to_be_clickable
                                        ((By.XPATH, f'//*[@id="__next"]/main/div[2]/div[2]/div[{banana9}]/input')
                                        )).click()
                    pyautogui.write(ess_point_input)
                    
                    ess_test_text_input = get_user_input("Dissertative text")
                    ess_test = wait.until(EC.element_to_be_clickable
                                        ((By.XPATH, f'//*[@id="__next"]/main/div[2]/div[2]/section[{banana9}]/div/div/div/div[3]/label/textarea')
                                        )).send_keys(ess_test_text_input)
                    
                    banana9 += 1
        else:
            pass
               
        # Finish test creation
        finish_test = wait.until(EC.element_to_be_clickable
                                ((By.XPATH, '//*[@id="__next"]/main/header/button/img'))).click()

        save = wait.until(EC.element_to_be_clickable
                        ((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/div/button[2]'))).click()

        list = wait.until(EC.element_to_be_clickable
                        ((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/button'))).click()

        time.sleep(5)

        # Course creation
        course_page = wait.until(EC.element_to_be_clickable
                                ((By.XPATH, '//*[@id="__next"]/main/div[1]/div[2]/ul/li[2]/a'))).click()

        # Open course
        open_course = wait.until(EC.element_to_be_clickable
                                ((By.XPATH, '//*[@id="__next"]/main/div[2]/div[3]/section/div[1]/table/tbody/tr[1]/td[8]/div/a'))).click()

        # Open course dependencies
        dependencies = wait.until(EC.element_to_be_clickable
                                ((By.XPATH, '//*[@id="__next"]/main/div[2]/div[3]/a'))).click()

        # Aprove classes
        for i in range(1, 10):
            approve = wait.until(EC.element_to_be_clickable
                                ((By.XPATH, '//*[@id="__next"]/main/div[2]/ul/div/ul/li[1]/div/div/div/button[1]'))).click()

            time.sleep(1)
            sure = wait.until(EC.element_to_be_clickable
                            ((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/div/button[2]'))).click()

            ok = wait.until(EC.element_to_be_clickable
                            ((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/button'))).click()

            time.sleep(1)

        time.sleep(2)

        # Goes tests approval page and approves it all
        test_approval = wait.until(EC.element_to_be_clickable
                                ((By.XPATH, '//*[@id="__next"]/main/div[2]/nav/a[2]'))).click()

        time.sleep(1)
        approve_test = wait.until(EC.element_to_be_clickable
                                ((By.XPATH, '//*[@id="__next"]/main/div[2]/ul/div/ul/li/div/div/div/button[1]'))).click()

        time.sleep(1)
        accept = wait.until(EC.element_to_be_clickable
                            ((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/div/button[2]'))).click()

        time.sleep(1)
        list = wait.until(EC.element_to_be_clickable
                        ((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/button'))).click()

        go_back = wait.until(EC.element_to_be_clickable
                            ((By.XPATH, '//*[@id="__next"]/main/div[2]/div[1]/header/button'))).click()

        time.sleep(1)
        
        go_back2 = wait.until(EC.element_to_be_clickable
                            ((By.XPATH, '//*[@id="__next"]/main/div[2]/div[1]/div[1]/header/button'))).click()
        
        # Course analyis
        analy = wait.until(EC.element_to_be_clickable
                        ((By.XPATH, '//*[@id="__next"]/main/div[2]/div[2]/a[2]'))).click()
        
        appr = wait.until(EC.element_to_be_clickable
                        ((By.XPATH, '//*[@id="__next"]/main/div[2]/div[3]/div[2]/div[11]/div/button[1]'))).click()
        
        acc = wait.until(EC.element_to_be_clickable
                        ((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/div[2]/button[2]'))).click()
        
        done = wait.until(EC.element_to_be_clickable
                        ((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/button'))).click()

        # Publishes the course
        info = wait.until(EC.element_to_be_clickable
                        ((By.XPATH, '//*[@id="__next"]/main/div[2]/div[2]/a[1]'))).click()
        
        time.sleep(0.5)
        
        publish = wait.until(EC.element_to_be_clickable
                            ((By.XPATH, '//*[@id="__next"]/main/div[2]/div[3]/section/div[1]/table/tbody/tr[1]/td[8]/div/button[1]'))).click()

        time.sleep(1)
        
        # For free
        free = wait.until(EC.element_to_be_clickable
                        ((By.XPATH, '//*[@id="modal-root"]/div[2]/div/form/div/button'))).click()

        save_free = wait.until(EC.element_to_be_clickable
                            ((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/div/button[2]'))).click()
        
        ok = wait.until(EC.element_to_be_clickable
                            ((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/button'))).click()
        
    time.sleep(6)

    # Close the browser
    driver.quit()