import customtkinter
from customtkinter import *
from Scripts import *

class CompanyWindow:
    def __init__(self, master):
        self.master = master
        self.window = CTkToplevel(master)
        self.window.geometry("500x240")
        
        # Get the base path for PyInstaller bundled app
        if hasattr(sys, '_MEIPASS'):
            base_path = sys._MEIPASS
        else:
            base_path = os.path.abspath(".")

        # Load the icon
        icon_path = os.path.join(base_path, "Icons", "movie.ico")
        self.window.iconbitmap(icon_path)

        self.go_back_btn = CTkButton(self.window, text="←", height=1, width=50, command=self.go_back,fg_color="#144870", hover_color="#08253b")
        self.go_back_btn.grid(row=0, column=0, padx=0, pady=0, sticky="w")
  
        # COMPANY BUTTONS  
        self.create_account_comp_btn = customtkinter.CTkButton(self.window, text="Create Account", fg_color="#144870", hover_color="#08253b", command=self.btn_create_account_master)
        self.create_account_comp_btn.grid(row=2, column=0, padx=3, pady=20, sticky="nsew")
        
        self.full_creation_btn = customtkinter.CTkButton(self.window, text="Full Creation", fg_color="#144870", hover_color="#08253b", command=self.btn_full_creation)
        self.full_creation_btn.grid(row=2, column=1, padx=3, pady=20, sticky="nsew")
        
        self.config_comp_btn = customtkinter.CTkButton(self.window, text="Configure Account", fg_color="#144870", hover_color="#08253b", command=self.btn_config_master)
        self.config_comp_btn.grid(row=2, column=2, padx=3, pady=20, sticky="nsew")
        
        self.approve_input_btn = customtkinter.CTkButton(self.window, text="Create|Approve|Publish(INPUT)", fg_color="#144870", hover_color="#08253b", command=self.btn_approve_course_input)
        self.approve_input_btn.grid(row=3, column=0, padx=3, pady=20, sticky="nsew")
        
        self.delete_course_btn = customtkinter.CTkButton(self.window, text="Delete Course", fg_color="#144870", hover_color="#08253b", command=self.btn_delete_course)
        self.delete_course_btn.grid(row=3, column=1, padx=3, pady=20, sticky="nsew")
        
        self.dup_course_btn = customtkinter.CTkButton(self.window, text="Duplicate Course", fg_color="#144870", hover_color="#08253b", command=self.btn_duplicate_course)
        self.dup_course_btn.grid(row=3, column=2, padx=3, pady=20, sticky="nsew")
        
        self.imp_aff_btn = customtkinter.CTkButton(self.window, text="Import Affiliate", fg_color="#144870", hover_color="#08253b", command=self.btn_import_affiliate_list)
        self.imp_aff_btn.grid(row=4, column=0, padx=3, pady=20, sticky="nsew")
        
        self.imp_stud_btn = customtkinter.CTkButton(self.window, text="Import Student", fg_color="#144870", hover_color="#08253b", command=self.btn_import_student_list)
        self.imp_stud_btn.grid(row=4, column=1, padx=3, pady=20, sticky="nsew")
        
        self.imp_teach_btn = customtkinter.CTkButton(self.window, text="Import Teacher", fg_color="#144870", hover_color="#08253b", command=self.btn_import_teacher_list)
        self.imp_teach_btn.grid(row=4, column=2, padx=3, pady=20, sticky="nsew")
        
    def go_back(self):
        self.window.destroy()  
        self.master.deiconify()  

    # COMPANY FUNCITONS
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
    app = CompanyWindow(root)
    root.mainloop()
