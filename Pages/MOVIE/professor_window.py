import customtkinter
from customtkinter import *
from Scripts import *


class ProfessorWindow:
    def __init__(self, master,on_close_callback):

        self.master = master
        self.on_close_callback = on_close_callback
        self.window = CTkToplevel(master)
        self.window.geometry("500x240")
        self.window.title("Professor Window")
        
        if hasattr(sys, '_MEIPASS'):
            base_path = sys._MEIPASS
        else:
            base_path = os.path.abspath(".")

        icon_path = os.path.join(base_path, "Icons", "movie.ico")
        self.master.iconbitmap(icon_path)
        
        # PROFESSOR BUTTONS
        self.create_account_prof_btn = customtkinter.CTkButton(self.window, text="Create Account", fg_color="#144870", hover_color="#08253b", command=self.btn_create_account_professor)
        self.create_account_prof_btn.grid(row=0, column=0, padx=3, pady=20, sticky="nsew")
        
        self.delete_course_prof_btn = customtkinter.CTkButton(self.window, text="Delete Course", fg_color="#144870", hover_color="#08253b", command=self.btn_delete_course_teacher)
        self.delete_course_prof_btn.grid(row=0, column=1, padx=3, pady=20, sticky="nsew")
        
        self.create_course_prof_btn = customtkinter.CTkButton(self.window, text="Create Course", fg_color="#144870", hover_color="#08253b", command=self.btn_create_course_professor)
        self.create_course_prof_btn.grid(row=1, column=0, padx=3, pady=20, sticky="nsew")
 
        # Override the close button
        self.window.protocol("WM_DELETE_WINDOW", self.on_close)    
    
    def on_close(self):
        self.on_close_callback()
        self.window.destroy()
        
    # PROFESSOR FUNCTIONS    
    def btn_create_account_professor(self):
        create_account_professor()
        
    def btn_delete_course_teacher(self):
        delete_course_teacher_func()
        
    def btn_create_course_professor(self):
        create_course_professor_func()
        
if __name__ == "__main__":
    root = CTk()  
    app = ProfessorWindow()
    root.mainloop()
