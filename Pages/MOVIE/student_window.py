import customtkinter
from customtkinter import *
from Scripts import *

class StudentWindow:
    def __init__(self, master):
        self.master = master
        self.window = CTkToplevel(master)
        self.window.geometry("500x240")
        self.window.iconbitmap(".\\Icons\\movie.ico")
        self.window.title("Student Window")

        self.go_back_btn = CTkButton(self.window, text="←", height=1, width=50, command=self.go_back,fg_color="#144870", hover_color="#08253b")
        self.go_back_btn.grid(row=0, column=0, padx=0, pady=0, sticky="w")

        # STUDENT BUTTONS 
        self.create_account_stu_btn = customtkinter.CTkButton(self.window, text="Create Account", fg_color="#144870", hover_color="#08253b", command=self.btn_create_student_account)
        self.create_account_stu_btn.grid(row=1, column=0, padx=3, pady=20, sticky="nsew")
        
        self.prepare_account_stu_btn = customtkinter.CTkButton(self.window, text="Prepare Account", fg_color="#144870", hover_color="#08253b", command=self.btn_prep_account_client)
        self.prepare_account_stu_btn.grid(row=1, column=1, padx=3, pady=20, sticky="nsew")
        
        self.buy_course_btn = customtkinter.CTkButton(self.window, text="Buy course", fg_color="#144870", hover_color="#08253b", command=self.btn_buy_course_client)
        self.buy_course_btn.grid(row=2, column=0, padx=3, pady=20, sticky="nsew")
        
    def go_back(self):
        self.window.destroy()  
        self.master.deiconify()  

    # STUDENT FUNCTIONS 
    def btn_create_student_account(self):
        create_student_account_func()
    
    def btn_prep_account_client(self):
        prep_account_client_func()
        
    def btn_buy_course_client(self):
        buy_course_func()
        
if __name__ == "__main__":
    root = CTk()  
    app = StudentWindow(root)
    root.mainloop()
