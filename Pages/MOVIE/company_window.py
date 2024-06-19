import customtkinter
from customtkinter import *
from Scripts import *

class CompanyWindow:
    def __init__(self, master, on_close_callback):
        self.master = master
        self.on_close_callback = on_close_callback
        self.window = CTkToplevel(master)
        self.window.title("Company Window")
        self.window.geometry("500x300")
        
        if hasattr(sys, '_MEIPASS'):
            base_path = sys._MEIPASS
        else:
            base_path = os.path.abspath(".")

        icon_path = os.path.join(base_path, "Icons", "movie.ico")
        self.master.iconbitmap(icon_path)

        # COMPANY BUTTONS  
        self.create_account_comp_btn = customtkinter.CTkButton(self.window, text="Create Account", fg_color="#144870", hover_color="#08253b", command=self.btn_create_account_master)
        self.create_account_comp_btn.grid(row=0, column=0, padx=3, pady=20, sticky="nsew")
        
        self.full_creation_btn = customtkinter.CTkButton(self.window, text="Full Creation", fg_color="#144870", hover_color="#08253b", command=self.btn_full_creation)
        self.full_creation_btn.grid(row=0, column=1, padx=3, pady=20, sticky="nsew")
        
        self.config_comp_btn = customtkinter.CTkButton(self.window, text="Configure Account", fg_color="#144870", hover_color="#08253b", command=self.btn_config_master)
        self.config_comp_btn.grid(row=0, column=2, padx=3, pady=20, sticky="nsew")
        
        self.approve_input_btn = customtkinter.CTkButton(self.window, text="Create|Approve|Publish(INPUT)", fg_color="#144870", hover_color="#08253b", command=self.btn_approve_course_input)
        self.approve_input_btn.grid(row=1, column=0, padx=3, pady=20, sticky="nsew")
        
        self.delete_course_btn = customtkinter.CTkButton(self.window, text="Delete Course", fg_color="#144870", hover_color="#08253b", command=self.btn_delete_course)
        self.delete_course_btn.grid(row=1, column=1, padx=3, pady=20, sticky="nsew")
        
        self.dup_course_btn = customtkinter.CTkButton(self.window, text="Duplicate Course", fg_color="#144870", hover_color="#08253b", command=self.btn_duplicate_course)
        self.dup_course_btn.grid(row=1, column=2, padx=3, pady=20, sticky="nsew")
        
        self.imp_aff_btn = customtkinter.CTkButton(self.window, text="Import Affiliate", fg_color="#144870", hover_color="#08253b", command=self.btn_import_affiliate_list)
        self.imp_aff_btn.grid(row=2, column=0, padx=3, pady=20, sticky="nsew")
        
        self.imp_stud_btn = customtkinter.CTkButton(self.window, text="Import Student", fg_color="#144870", hover_color="#08253b", command=self.btn_import_student_list)
        self.imp_stud_btn.grid(row=2, column=1, padx=3, pady=20, sticky="nsew")
        
        self.imp_teach_btn = customtkinter.CTkButton(self.window, text="Import Teacher", fg_color="#144870", hover_color="#08253b", command=self.btn_import_teacher_list)
        self.imp_teach_btn.grid(row=2, column=2, padx=3, pady=20, sticky="nsew")
    
        # Override the close button
        self.window.protocol("WM_DELETE_WINDOW", self.on_close)    
    
    def on_close(self):
        self.on_close_callback()
        self.window.destroy()
        
    # COMPANY FUNCITONS
    def btn_create_course_auto(self):
        create_course_func()
    
    def btn_create_account_master(self):
        create_account_master_func()
        
    def btn_config_master(self):
        config_master_func()

    def btn_create_app_pub(self):
        create_app_pub_func()   
    
    def btn_approve_course(self):
        approve_course_func()     
        
    def btn_approve_course_input(self):
        create_app_pub_input_func() 
    
    def btn_create_course(self):
        create_course_func()   
    
    def btn_delete_course(self):
        delete_course_func()
        
    def btn_duplicate_course(self):
        duplicate_course_func()
        
    def btn_import_affiliate_list(self):
        import_affiliate_list_func()    
        
    def btn_import_student_list(self):
        import_student_list_func()
        
    def btn_import_teacher_list(self):
        import_teacher_list_func()

    def btn_full_creation(self):
        full_account_creation_master()    
    
        
# Example usage:
if __name__ == "__main__":
    root = CTk()  
    app = CompanyWindow()
    root.mainloop()
