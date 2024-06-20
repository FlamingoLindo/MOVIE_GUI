import customtkinter as tk
from tkinter import simpledialog
from dotenv import *
import os
load_dotenv()

def set_paths():
    def get_user_input(prompt):
        root = tk.CTk()
        root.withdraw()  # Hide the main window

        user_input = simpledialog.askstring("Input", prompt)

        return user_input

    # SETS .ENV VARIABLES
    aff_path = os.getenv('AFF_PATH')
    stu_pat = os.getenv('STU_PATH')
    pro_path = os.getenv('PRO_PATH')


    # affiliate
    if aff_path == "":
        aff = get_user_input("PLEASE INSERT AFFILIATE EXCEL PATH")
        set_key(".env", "AFF_PATH", aff)
    else:
        pass

    # student
    if stu_pat == "":
        stu = get_user_input("PLEASE INSERT YOUR STUDENT EXCEL PATH")
        set_key(".env", "STU_PATH", stu)
    else:
        pass

    # professor
    if pro_path == "":
        pro = get_user_input("PLEASE INSERT YOUR PROFESSOR EXCEL PATH")
        set_key(".env", "PRO_PATH", pro)
    else:
        pass



