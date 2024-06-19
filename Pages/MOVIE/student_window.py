import customtkinter
from customtkinter import *
from Scripts import *

class StudentWindow:
    def __init__(self, master, on_close_callback):
        self.master = master
        self.on_close_callback = on_close_callback
        self.window = CTkToplevel(master)
        self.window.geometry("500x240")
        self.window.title("Student Window")
        
        # Get the base path for PyInstaller bundled app
        if hasattr(sys, '_MEIPASS'):
            base_path = sys._MEIPASS
        else:
            base_path = os.path.abspath(".")

        icon_path = os.path.join(base_path, "Icons", "movie.ico")
        self.master.iconbitmap(icon_path)

        # STUDENT BUTTONS 
        self.create_account_stu_btn = customtkinter.CTkButton(self.window, text="Create Account", fg_color="#144870", hover_color="#08253b", command=self.btn_create_student_account)
        self.create_account_stu_btn.grid(row=0, column=0, padx=3, pady=20, sticky="nsew")
        
        self.prepare_account_stu_btn = customtkinter.CTkButton(self.window, text="Prepare Account", fg_color="#144870", hover_color="#08253b", command=self.btn_prep_account_client)
        self.prepare_account_stu_btn.grid(row=0, column=1, padx=3, pady=20, sticky="nsew")
        
        self.buy_course_btn = customtkinter.CTkButton(self.window, text="Buy course", fg_color="#144870", hover_color="#08253b", command=self.btn_buy_course_client)
        self.buy_course_btn.grid(row=0, column=2, padx=3, pady=20, sticky="nsew")
        
        self.buy_course_btn = customtkinter.CTkButton(self.window, text="Do course", fg_color="#144870", hover_color="#08253b", command=self.btn_do_course_client)
        self.buy_course_btn.grid(row=1, column=0, padx=3, pady=20, sticky="nsew")
     
     # Override the close button
        self.window.protocol("WM_DELETE_WINDOW", self.on_close)    
    
    def on_close(self):
        self.on_close_callback()
        self.window.destroy()
     
    # STUDENT FUNCTIONS 
    def btn_do_course_client(self):
        do_course_func()
    
    def btn_create_student_account(self):
        create_student_account_func()
    
    def btn_prep_account_client(self):
        prep_account_client_func()
        
    def btn_buy_course_client(self):
        buy_course_func()
        
if __name__ == "__main__":
    root = CTk()  
    app = StudentWindow()
    root.mainloop()
